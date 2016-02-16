---
layout: post
title:  "Twitter Butler"
date:   2015-05-24 20:52:38
categories: coding
image:
  background: witewall_3.png
---

Howdy folks, Hobby post after a long time. This post briefly deals with a fun project that i created this weekend.

Basically while learning about IOT and other M2M stuff, I thought how to incorporate it in daily usage. And in a fun way learn something new and productive.

Basically the idea that struck was that we use twitter in our day to day lives to interact with people so, why can't we use it to interact with machines. In this application I have a twitter butler that reponds to my request and perform some actions accordingly on the board (pi). I had a Raspberry Pi which was used basically as a torrent seeder. So I reconfigued it with the application that runs the butler. Butler is bascially a python program that I created which uses twitter and shell Api's to interact with my requests.

Whenever any request is made to the butler via twitter (mentions or DMs) it understands (in a way Siri/Cortana does but in very naive manner) and responds it to me if the job is done. Basically it would be used to add torrents, download youtube videos, songs schedule maintenence and run shell commands for automation.It is in a very inital stage right now and would be extending the functionality if needed. So, more ideas are invited ;).

Here is a small Example :-

<img src="/images/butler.png" alt="">


The twitter library that i am using is available [here](https://github.com/sixohsix/) and the butler [here](https://twitter.com/tweet__butler).

You can use the code to interact with any machine or system that exposes a high level Api.(Like a personalised [IFTTT](https://ifttt.com/) software but much more effective.)

Maybe this is what we can get in the future.


<img src="/images/iot.jpg" alt="">

Reuse and Happy Hacking. 