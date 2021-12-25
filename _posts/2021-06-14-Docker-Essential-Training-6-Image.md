---
layout: post
title: "Docker Essential Training - 6 | Image Creation, Management, and Registry "
date: 2021-06-14 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.linkedin.com/learning/docker-essential-training-3-image-creation-management-and-registry/)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

This course is a tutorial series for the DCA exam using Docker EE. This Lesson deals with Image Creation, Management, and Registry using Docker.

- Docker Images Overview

  - Image is an executable package that contains everything to run your application.
  - Images are stopped container and are read-only.
  - A Dockerfile contains all commands to build an image. Used in _docker build_

- DockerFile

  - ADD - copy files, also suports tar
  - Copy - copy files
  - VOLUME - Add mount point
  - ENTRYPOINT - which app to run
  - EXPOSE - Which Port to Publish
  - CMD - Arguments to entrypoint
  - ENV - Environment
  - FROM - Defines base image, must be first command.
  - RUN - runs a new command in new layer.
  - WORKDIR - Defines working directory.
  - _docker image history_ to see the layer history.

- Managing Images

  - _docker image inspect_ - provides low-level information on docker.
  - _docker tag_ - to tag an image.

- Docker Registry
  - Stateless, HA application for storing, sharing images.
  - _docker push <registry location>_ to push to local registry
  - DTR is available in Docker EE.
  - _docker login_ to login to docker hub, free cloud registry
  - Docker notary helps in own image signing.
  - _docker search_ to search the docker hub for images.
