---
layout: post
title:  "Ovs Commands"
date:   2015-03-23 23:52:38
categories: ovs
---

Here is a list of ovs commands that i use on everyday basis. Jotting them down so that i don't have to do history | grep 'ovs' everytime.

Basic commands : Most day to day used commands in ovs.

`ovs-vsctl : Used for configuring ovs-db`

`ovs-ofctl : A command line tool for monitoring and administering OpenFlow switches`

`ovs-dpctl : Used to administer Open vSwitch datapaths`

`ovs-appctl : Used for querying and controlling Open vSwitch daemons`

Below are the most useful ovs-vsctl commands:

`ovs-vsctl -V : Prints the current version of openvswitch.`

`ovs-vsctl show : Prints a brief overview of the switch database configuration.`

`ovs-vsctl list-br : Prints a list of configured bridges`

`ovs-vsctl list-ports <bridge> : To see all the OVS ports and their settings.`

`ovs-vsctl list interface : Prints a list of interfaces.`

For configuring ovs Bridges use this commands.

But first you need to pull up some interfaces by these commands

`ip tuntap add mode tap veth0`

`ip link set veth0 up`

Attach the ports to bridge.

`ovs-vsctl add-br <bridge> : Creates a bridge in the switch database.`

`ovs-vsctl add-port <bridge> <interface> : Binds an interface (physical or virtual) to a bridge.`

For internet connectivty in ovs bind the physical port to the ovs bridge.

`ifconfig eth0 0 && ifconfig br0 <ip address> netmask <subnet mask>`

ovs-ofctl

The  ovs-ofctl program is a command line tool for monitoring and admin listering OpenFlow switches. It can also show the current state of an OpenFlow  switch, including features, configuration, and table entries.

Below are common openflow show commands:

`ovs-ofctl show <bridge> : Shows OpenFlow features and port descriptions.`

`ovs-ofctl snoop <bridge> : Snoops traffic to and from the bridge and prints to console.`

`ovs-ofctl dump-flows <bridge> <flow> : Prints flow entries of specified bridge. With the flow specified, only the matching flow will be printed to console. If the flow is omitted, all flow entries of the bridge will be printed. `

`ovs-ofctl queue-stats <bridge> : SPrints the queue stats on the bridge.`

`ovs-ofctl dump-ports-desc <bridge> : Prints port statistics. This will show detailed information about interfaces in this bridge, include the state, peer, and speed information. Very useful`

How to add/ delete a flow in Ovs:

`ovs-ofctl add-flow <bridge> <flow> : Add a static flow to the specified bridge. Useful in defining conditions for a flow (i.e. prioritize, drop, etc).`

`ovs-ofctl del-flows <bridge> <flow> : Delete the flow entries from flow table of stated bridge. If the flow is omitted, all flows in specified bridge will be deleted.`


Will Expand this section after more insights and hands on ovs.

-Forked from [here](http://therandomsecurityguy.com/openvswitch-cheat-sheet/ "blog") 