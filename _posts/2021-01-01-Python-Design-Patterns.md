---
layout: post
title:  "Python Design Patterns"
date:   2018-04-22 03:52:38
categories: Tech
hidden: true
tags: [DIY, Coding]
image:
  background: witewall_3.png
---

Factory DP : This is an design pattern in which we can create a interface factory (method) to instantiate the objects of classes. This helps in instantialting the right kind of object.

In the example below, we have 2 classes for Cars and Truck, in which we have the methods that return the no of tyres in each type of Vehicle. Using factory pattern we can identify the correct class to instantiate based on the parameters invoked in the factory method.

```

class Car:

	def __init__(self, type):
		self._type = type

	def no_of_tyres(self):
		return 4

class Truck:

	def __init__(self, type):
    		self._type = type

	def no_of_tyres(self):
		return 6

def get_auto(auto_type="car"):

	"""The factory method"""

	autos = dict(car=Car("Audi"), truck=Truck("Volvo"))

	return autos[auto_type]

d = get_auto("car")

print(d.no_of_tyres())

c = get_auto("truck")

print(c.no_of_tyres())


```

Abstract Factory DP : In the last example we have seen that we can create a factory for known classes. In Abstract factory we don't have this information (classes) till runtime.

To implement this we will create Abstact factory and concrete factory as below: 


```
```