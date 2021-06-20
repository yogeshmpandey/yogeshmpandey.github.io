---
layout: post
title:  "Docker Essential Training - 2 | Orchestration"
date:   2021-06-10 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.linkedin.com/learning/docker-essential-training-2-orchestration)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

This course is a tutorial series for the DCA exam using Docker EE. This Lesson deals with orchestration using Docker SWARM.

- Docker SWARM
    - HA
    - Load Balancing
    - Resiliency
    - Placement
    - Declarative Service model
    - Is secure by default.
    - `docker swarm init` initialtes a docker swarm.
    - `docker swarm join-token` to join as a cluster.

- Paradigms
    - Node: an independent service, can have multiple clusters.
    - A service can run many nodes. 
    - Quorum: to make sure that the swarm's state is healthy.

- Stacks and stacks files
  - Define a set of configurations for a set of services. A docker stack consists of all the SW systems needs by the applications like DB, webserver. 
  - Defined in yml file (Mostly like docker-compose file)
  - Set and update the configurations. Check the docker documentation for this.
  - Define the service to be global or replicated.

- Troubleshooting Docker SWARM
  - docker service logs _Service Name_
  - docker node inspect _labels_

- Deploy docker services using templates. 