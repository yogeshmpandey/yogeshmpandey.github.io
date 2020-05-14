---
layout: post
title:  "Useful Docker Commands"
date:   2020-05-11 03:52:38
categories: Tech
hidden: true
tags: [DIY, Coding]
image:
  background: witewall_3.png
---

I use docker everyday at work. Here are a few commands that are useful : 

1. Few useful docker-compose and docker commands:
     - **docker-compose build** - builds all the service containers. To build a single service container, use **docker-compose build [serv_cont_name]**
     -  **docker-compose down** - stops and removes the service containers
     - **docker-compose up -d** - brings up the service containers by picking the changes done in **docker-compose.yml**
     - **docker ps** - check running containers
     - **docker ps -a** - check running and stopped containers
     - **docker stop $(docker ps -a -q)** - stops all the containers
     - **docker rm $(docker ps -a -q)** - removes all the containers. Useful when you run into issue of already container is in use.
     - [docker compose cli](https://docs.docker.com/compose/reference/overview/)
     - [docker compose reference](https://docs.docker.com/compose/compose-file/)
     - [docker cli](https://docs.docker.com/engine/reference/commandline/cli/#configuration-files)
     
2. If you want to run the docker images separately i.e, one by one, run the command **docker-compose run --no-deps [service_cont_name]**. If the container is running and one wants to get inside, use cmd: **docker-compose exec [service_cont_name] /bin/bash** or **docker exec -it [cont_name] /bin/bash**

3. Best way to check logs of containers is to use command: **docker logs -f [cont_name]**. If one wants to see all the docker-compose service container logs at once, then just run
   **docker-compose logs -f**
