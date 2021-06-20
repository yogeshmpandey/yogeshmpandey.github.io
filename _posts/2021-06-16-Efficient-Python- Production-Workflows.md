---
layout: post
title:  "Efficient Python Production Workflows"
date:   2021-06-16 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.linkedin.com/learning/efficient-python-production-workflows/)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

- A good process avoid mistakes.
    - Automation
    - Checklists
    - Knowledge Transfer

- OODA
    - Observe
    - Orient
    - Decide
    - Change

- Dependency Management
    - Use package manager, venv. use requiremnts.txt
    - Have separate requirements file for prod and dev
    - _--find-links_ to find internal packages.
    - Use docker file

- Testing
    - Best value Tests 
        - Deployment
        - Integration
        - Regression
        - Fuzzing
        - Unit
        - Linters
    - Know which type of tests must have caught the bug.
    - CI detects much class of errors. ex: Jenkins
    - Mark tests. Ideally, dev tests should not take more than 1 minute to run. 

- Logging
    - what? format? How many? where to store?
    - Log Levels and log.ini file.
    - Logging is a balance between too much and too little.
    - Use structured logging, like JSON. It's easier for parsing.
    - Log aggregators

- Metrics
    - Measurements about the system. Helps in detecting outliers.
    - Prometheus metrics: Gauge, counter, histograms.
    - They should be based on Business. Use KPIs. Strive to get actual numbers. Have SLA in numbers.
    - Use Decorators. Prometheus gives ready-made decorators.
    - Push vs pull-based metric systems.
    - Alerting system based on metrics. ex: PagerDuty. 

- Deployment Methods
    - Blue-Green deployment
        - Direct traffic from blue to green.
    - Rolling and Canary
    - Deployment should be automated. ex: Fabric: FabFile.py.
    - Try to mimic production in testing.