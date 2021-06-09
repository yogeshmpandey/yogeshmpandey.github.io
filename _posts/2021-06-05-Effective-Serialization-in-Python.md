---
layout: post
title:  "Effective Serialization in Python"
date:   2021-06-05 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.linkedin.com/learning/effective-serialization-with-python)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).


The process of transferring the data from one module to another is called serialization. Serialization happens at the edge of your program (Making HTTP Calls, saving to disk) ex: Python list to 1s and 0s. There are many formats, the right format will save you time, money, function calls. In this course, we will learn how to pick the right serialization for your code.


- How to choose the format? 
  
  - How many programming languages support the format.
  - How many types can you support. JSON does not support DateTime Format but protobuf does. 
  - Message Schema. Schemas define the dataformat. Choose Message format with schema or without schema. 
  - Performance. Although with the current CPU we can use any format still it makes sense to choose the best performance wrt CPU and bandwidth.
  - Is the schema format is a part of the standard library. 
  - Don't invent your Schema.
  - Mostly Companies use JSON for External APIs and Protocol Buffers for Internal Communication. 

- General Rules
  
  - Design and document your data. 
  - Before choosing the format make sure you know your object.
  - Serialize only in the edges.
  - Make sure the format is Secure. 
  - Learn the format correctly. 

- Formats Overview
  
  - Pickel: Python only format, Mostly for internal communication. 
  - JSON: Most popular Format, but the time field is a limit, and we cannot add comments so it is tricky to use it in configuration. 
  - YAML: Support wider variety, Slow serialization types.
  - CSV: Not as cool but handy. No schema specification, Does not support hierarchical data.
  - XML: DTD can be used to define types. 
  - msgpack and BSON: Open Schema formats
  - protocol Buffers: Define the data file and generate the serialization files. Very efficient. Used for internal communication between servers.
  - SQL: Invented schema, built-in Python.

- Pickle

```
# serialize to file
with open('saved.pkl', 'wb') as out:
    pickle.dump(move1, out)


# de-serialize from file
with open('saved.pkl', 'rb') as fp:
    move1f = pickle.load(fp)
print(f'move1f (from file) = {move1f}'

```

  - The repr() function returns a printable representation of the given object.
  - Using repr we can log objects. Very helpful in debugging.
  - Python data class is used for storing (not much as logic)
  - exec and eval can be used to load config files. You can write any valid python code in config.py.


-JSON

  - JSON uses dump and load to dump and load the data. dump if we have the file.

```
data = json.dumps(data_val)

val = json.loads(data_val)

```
  - JSON data time is not serializable, Instead, you need to explicitly tell JSON to convert the unknown data type.
  - 

- Protocol Buffer

  - protoc compiler based on gRPC, can be used to communicate with different microservices based on different languages. 

```
// Sample Proto File

syntax = "proto3"

import "timestamp.proto"

message test{ string test = 1}

```

  - protoc generates the python code. To use this code we will use the python protobuf package.
  - To serialize use message.SerializeToString()

- msgpack can be used if you have data constraints on JSON.

- XML can be used in 2 ways DOM and SAX mode. 

- We need to make sure that our strings are normalized in the same way.

- How can you know the encoding? The data channel will provide the way to encoding (charset=utf-8). If the channel does not provide the encoding you can use the chardet package. 

Need to do more hands-on on how to use and send the data. Try different formats in serialization and figure out the best possible way. 