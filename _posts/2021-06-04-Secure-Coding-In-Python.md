---
layout: post
title:  "Secure Coding in Python"
date:   2021-06-04 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---


[Main Course Link](https://www.linkedin.com/learning/secure-coding-in-python)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

The author discusses the top 10 OWSAP vulnerabilities with examples and how to take care of them in python:-


- Ask yourself, will you pay 1000k USD to use this software. Keep your development environment clean.

- Make sure you download from secure websites.

- Make sure your libraries are updated with the latest security patches.

- CVE is a list of known cybersecurity vulnerabilities, pipenv has a tool called 'safety' that can detect these vulnerabilities. 

- pipenv check, bandit are tools that help in catching these vulnerabilities.

- Nowadays certificates are free, so make sure to add them to your code. 

- Recheck your code to check for vulnerabilities ex: SQL injection 

- Python dynamic types can increase productivity but also can add vulnerabilities ex: Truthy Values, Falsy Values. Explicit is better (and safer) than implicit . 

- Python optimized mode might lead to unpredictable behaviours.

- Pickle can lead to vulnerabilities. Use JSON instead which can be deserialized.

- Use a separate python environment for isolation. 

- Find a better way to manage secrets (in env variables or a 3rd party software).

- Know what goes into source control, use a gitignore file. (Add secrets to your git ignore file.)

- Make sure you don't overexpose the data in REST APIs. 

- Make sure that the permissions are set correctly in the code for multiple users (Broken Authentication). 

- Code without test is broken and insecure by design. 

- Never store the password in plain text. There are different methods of hashing. 

- Keep yourself updated with the latest updates using OWSAP guidelines. 

