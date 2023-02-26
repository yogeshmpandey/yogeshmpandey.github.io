---
layout: post
title:  "Benchmarking Databases Using Sysbench"
date:   2018-10-05 03:52:38
categories: Tech
hidden: true
tags: [DIY, Coding]
image:
  background: witewall_3.png
---

I was working on a project in which we had to create a storage engine for MariaDB ( similar to MySQL). After completing the development the request came from the client to benchmark the Storage engine. In order to provide information on the overall improvement on the execution cycle/workflows/Transactions over the default InnoDB Database. While doing this, I realized that there is not much documentation online on how to properly use SysBench for benchmarking the databases.

SysBench is a scriptable multi-threaded benchmark tool based on LuaJIT. It is most frequently used for database benchmarks. In the Latest version of SysBench (>1.0) you can create you own custom benchmarks using a custom lua scripts. Apart from CPU, Memory, IO benchmarks SysBench comes with a collection of OLTP-like database benchmarks in the oltp_*.lua scripts.

The OLTP (online transaction processing) mimic an online transaction in an ecommerce website. These scripts support the following OLTP like transactions.

- bulk_insert.lua
- oltp_delete.lua
- oltp_point_select.lua
- oltp_update_non_index.lua
- select_random_points.lua
- oltp_insert.lua
- oltp_read_only.lua
- oltp_update_index.lua
- select_random_ranges.lua
- oltp_write_only.lua
- oltp_read_write.lua

Running these custom scripts is really very simple. We will go through the steps one by one starting from installation of SysBench. I am using Fedora 27 in this example, but this should work in any other distribution of linux as well.

#### Installation

On Debian/Ubuntu, SysBench can be installed as follows:

- sudo apt-get install sysbench

On Fedora

- dnf install sysbench

Once SysBench is installed you can see the command line options by running
- man sysbench

Now that we have SysBench installed, we will now proceed with the database Benchmark.

#### Benchmarking

Benchmarking is a way of discovering the performance of your infrastructure (databases/networks/Memory/etc). Here we will talk specifically about MariaDB database.

Benchmarking using SysBench is mainly 3 step process.
- Prepare: Prepare the Infrastructure for benchmarking
- Run: Run the Benchmark
- Cleanup:  Clean the Infrastructure created in Prepare Phase

During Prepare phase we can play around with a lot of command line parameters. You can get the list of those paremeters Using the following commands
- sysbench --help
- sysbench "Test Script name" --help

With these parameters you can change the complexity/timing of your tests.

To give an example, I will run the prepare phase will 100 tables with 100 rows with threads =1 without auto increment and secondary indexes. One thing to note here is you need to create a database first named "sbtest" in the database for SysBench to create the proper testing infrastructure.


```
[root@localhost yogi]#  sysbench --test=/usr/share/sysbench/oltp_write_only.lua --db-driver=mysql --mysql-socket=/tmp/mysql.sock --threads=1 --mysql-db=sbtest --mysql-user=root --mysql-password=mypass  --secondary=off --auto_inc=off --create_secondary=off  --debug=on --tables=1 --table-size=100 --db-ps-mode=disable prepare
WARNING: the --test option is deprecated. You can pass a script name or path on the command line without any options.
sysbench 1.0.9 (using system LuaJIT 2.1.0-beta3)

Creating table 'sbtest1'...
Inserting 100 records into 'sbtest1'
```


In the run phase, just change the last line in the command to run

```
[root@localhost yogi]# sysbench --test=/usr/share/sysbench/oltp_write_only.lua --db-driver=mysql --mysql-socket=/tmp/mysql.sock --threads=1 --mysql-db=sbtest --mysql-user=root --mysql-password=mypass  --secondary=off --auto_inc=off --create_secondary=off  --debug=on --tables=1 --table-size=100 --db-ps-mode=disable run
WARNING: the --test option is deprecated. You can pass a script name or path on the command line without any options.
sysbench 1.0.9 (using system LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 1
Debug mode enabled.

Initializing random number generator from current time


Initializing worker threads...

DEBUG: Worker thread (#0) started
DEBUG: Worker thread (#0) initialized
Threads started!

Time limit exceeded, exiting...
Done.

SQL statistics:
    queries performed:
        read:                            0
        write:                           4496
        other:                           2248
        total:                           6744
    transactions:                        1124   (112.23 per sec.)
    queries:                             6744   (673.40 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

General statistics:
    total time:                          10.0102s
    total number of events:              1124

Latency (ms):
         min:                                  6.87
         avg:                                  8.90
         max:                                 21.43
         95th percentile:                      9.91
         sum:                              10005.40

Threads fairness:
    events (avg/stddev):           1124.0000/0.00
    execution time (avg/stddev):   10.0054/0.00

DEBUG: Verbose per-thread statistics:

DEBUG:     thread #  0: min: 0.0069s  avg: 0.0089s  max: 0.0214s  events: 1124
DEBUG:                  total time taken by event execution: 10.0054s
```

Similarly, for cleanup, change the last line to cleanup and it will drop all the tables.


```
[root@localhost yogi]#  sysbench --test=/usr/share/sysbench/oltp_write_only.lua --db-driver=mysql --mysql-socket=/tmp/mysql.sock --threads=1 --mysql-db=sbtest --mysql-user=root --mysql-password=mypass  --secondary=off --auto_inc=off --create_secondary=off  --debug=on --tables=1 --table-size=100 --db-ps-mode=disable cleanup

Dropping table 'sbtest1'...

```


Likewise you can run all the OLTP tests and get the benchmarks for your database environment.
