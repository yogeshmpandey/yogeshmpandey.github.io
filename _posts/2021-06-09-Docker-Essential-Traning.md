---
layout: post
title:  "Docker Essential Training - 1 | Basics " 
date:   2021-06-09 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.linkedin.com/learning/docker-essential-training-1-installation-and-configuration)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

This course is a tutorial series for the DCA exam using Docker EE. 


- Docker EE vs Docker CE
- Take into account the size of hardware before running docker. 
  - If the containers use UCP and DTR (Docker Trusted Registry) you need to understand and adhere to the requirements.

- Docker engine is a client-server platform. It has:-
  - dockerd server daemon
  - docker cli client 
  - Docker does not run in 32bit systems.
  - Docker containers are ephemeral

- Docker Universal Control Plane.
  - To manage multiple Docker engines
  - Has a trusted registry for centralized storage for images. 
  - Manage networks and docker infra.
  - UCP runs a Container from Docker HUB. Only on Docker EE.

- Docker namespaces
  - Helps in virtualize Linux process, mount, IPC, User, Network to isolate docker containers.
  - Uses Linux internal Functionalities.

- CGROUPS
  - Set CPU, memory Limits etc for the container. 
  - All docker files are in /var/lib/docker 

- Docker Storage Driver.
  - Find which storage driver you are using. 
  - Storage driver control how you are storing your data.

- Docker Registry.
  - Docker HUB is the default docker registry.
  - Similar to Github.

- Docker Swarm
  - Enables HA
  - Multiple Worker Nodes. 
  - Can be used via UCP. 

- Managing Users
  - Via UCP its very easy to add users via Add Organization -> Add Team -> Add user -> Add roles

- Backup Docker
  - Backup Docker Cluster 
    - Copy /var/lib/docker/swarm  after stopping docker daemon. 
  - Backup UCP 
    - Copy/Paste command to place UCP to a tar.gz file. 
  - Backup DTR
    - Multiple commands to backup multiple DTR data. 

- Installing DTR
  - It runs as a docker command. Asks for UCP's Details 

- Use daemon.json for docker specific configurations.