---
layout: post
title:  "Docker Essential Training - 5 | Storage and Volumes"
date:   2021-06-13 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.linkedin.com/learning/docker-essential-training-4-storage-and-volumes)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

This course is a tutorial series for the DCA exam using Docker EE. This Lesson deals with Volumes using Docker.


- Storage Overview
    - Container data should not be stored in the container as they are emphermal. 
    - Container filesystem was not designed for high perfromance IO
    - Volume -> /vat/lib/docker/volumes
    - bind mounts -> host's file path
    - tempfs -> in RAM

- Block vs object storage
    - Block has fixed chuncks of data, best for I/O calls.
    - Object storage for container images similar to s3. 
    - Docker has layered storage, for an image, below are the layers. (Docker union file system)
        - Manifest
        - OS layer
        - Config Changes
        - Applications
    - We can check this by using _docker history <image ID>_

- Storage Drivers.
    - overlay2 -  For container's write, default choice.
    - Device-mapper uses block-based storage and can serve as an alternative to overlaying. 
    - When you change the storage driver, all the images will be lost. So better save them with the docker image save command. 
    - Volumes are used to store persistent data. Even can save on remote system
    - Use bind mounts as type = bind, source=/tmp
    - Make sure you prune the unused images the dangling images. 