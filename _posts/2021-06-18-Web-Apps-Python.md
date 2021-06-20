---
layout: post
title:  "Learn Python by Creating Webapps"
date:   2021-06-18 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.packtpub.com/product/complete-python-web-course-build-8-python-web-applications-video/9781839215094)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

- Using Beautiful Soup to Parse Website Data 

```
import requests
from bs4 import BeautifulSoup, element

request = requests.get("https://www.packtpub.com/product/complete-python-web-course-build-8-python-web-applications-video/9781839215094")
# <span class="price-list__price" itemprop="price" content="6823.99"> ₹6,823.99  </span>
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", attrs={"itemprop": "price", "class": "price-list__price"})
print (element.text.strip())
```


- Using MongoDB with python

```
from pymongo import MongoClient

client = MongoClient('localhost', 27018)
database = client["yogesh"]
print (database.list_collection_names())
collection = database["posts"]

# Inserts
post = {"name": "vertika", "age": 31}
post_id = collection.insert_one(post).inserted_id
 
# Retrieval
usrs = collection.find({})
for user in usrs:
    print(user)
```