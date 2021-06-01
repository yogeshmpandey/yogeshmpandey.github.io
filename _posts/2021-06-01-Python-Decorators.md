---
layout: post
title:  "Python Decorators"
date:   2021-06-01 03:52:38
categories: Tech
hidden: true
tags: [DIY, Coding]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.linkedin.com/learning/learning-python-generators)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

The course is based on an older python version and the code is incompatible with the latest version. 

## Python Generators

- Used for creating iterator operator. Not using a loop for interaction. 
- It maintains the state of the last operation. 
- Has a lazy evaluation
- Iterators have the next () function, even the for loop uses iterators in the backed
- Use of keyword yield. (Not return as other functions)
- Generator function return the generator object which we can use in our code. 
- Generator objects cannot be reused.

Example as a list comprehension: (item for item in collection), we use () to create a generator object.

```
# Create Generator 

intg = (n for n in [1,2,3,1,3])

print (intg)

# Get Generated Objects
print (intg.next())
print (intg.next())
print (intg.next())

# Get Remaining Items
print (list(intg))

# This will run into issues as now there nothing left in the generator
print (intg.next())

```


Example: Fibonacci  Series using Generators. 

```
def fibb():
    tail, lead = 0,1
    while True:
        yield lead
        tail, lead = lead, tail + lead
        
fib = fibb()  
print(fib.next())
print(fib.next())
print(fib.next())
print(fib.next())
print(fib.next())
```

Generators pipelines: We can use package multiple generator objects to create a pipeline.

### Context Manager: 

Python Object that acts as a control manager. Python snippet _with open (file)_ is a Content manager. This _with open_ clause can be implemented as below.

Basic Framework for Context Manager

```
# Context Manager Decorator
@contextmanager
def simple_context_manager(gen_obj):
    try:
        # Change the Object Value
        obj.prop +=1
        # Yield Control back to Caller 
        yield
    finally:
        # Bring Object back to its original Value
        obj.prop -=1

```

Note: Context Manager is used with the _with_ Python Block.

### CoRoutine: 

- Receives Value 
- Different from Generator
- Persists the properties of an object, unlike functions. 
- We have send method to send to coroutine. 
- We can use the co-routine decorators to skip the use of the next() primer. 
- We can also use and create Coroutines pipelines.

```
def coroutine(string):
    count = 0
    try : 
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    print item
                else:
                    print "No match found"
            else:
                print "Please enter String"
    
    except GeneratorExit:
        print ("Closed Coroutine")
        
c_obj = coroutine("Yogesh")
c_obj.next()
c_obj.send("Yog")
c_obj.send("Nose")
c_obj.close()
```

