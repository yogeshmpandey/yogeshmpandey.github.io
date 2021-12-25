---
layout: post
title:  "Python Web Scraping"
date:   2021-06-19 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.linkedin.com/learning/web-scraping-with-python?u=2163426)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

- We use scrapy as it is more mature and well defined library for Web Scraping.

- Different ways of using xpath selector. The [Documentation](https://docs.scrapy.org/en/latest/) has it all.

- Why Scrape when you have APIs.

- scapy genspider "Website to Scrape"

- Running commands : Running commands : scrapy runspider indiahikes.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10

- Use the settings file to set the parsing rules and other settings.

- In piplelines.py you can create the web scraping pipelines.

- Piplines are the bestway to write in data.

- I created a webcrawler to crawl indiahikes website and save the cost of all treks in a json file 

- Github Link for the Project. [ihScraper](https://github.com/yogeshmpandey/ihScraper)

- Advanced Techniques
  - Sumitting a form.
  - Finding Hidden API that are often embedded in a website. Using Inspect network. (Very intersting detective work)
  - Use Sitemap for better scraping. Use robots.txt for finding this.
  - Automatic Logins

- Using Selenuim with Scrapy for automation
