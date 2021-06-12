---
layout: post
title:  "Docker Essential Training - 3 | Networking"
date:   2021-06-11 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.linkedin.com/learning/docker-essential-training-5-networking)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

This course is a tutorial series for the DCA exam using Docker EE. This Lesson deals with Networking using Docker.

- Types of networking 

  - Bridge: Default NW.
  - Host: Removes network isolation, connects directly to host. 
  - Overlay: Only in Docker EE, to connect multiple docker hosts. 
  - Macvlan: Support to connects VLAN. Clones host interfaces. 
  - None: No networking accessibility.
  - Other nw plugins.

- Creating networks
  - docker network ls
  - docker network create --driver bridge app-nw
  - -p _port name_ to expose the port in a container.
  - --DNS _dns name_ to set the DNS name.
  - docker container logs _container name_ to debug the networking logs. -f to use like tail -f.