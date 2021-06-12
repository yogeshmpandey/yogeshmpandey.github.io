---
layout: post
title:  "Docker Essential Training - 4 | Security"
date:   2021-06-12 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.linkedin.com/learning/docker-essential-training-6-security)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

This course is a tutorial series for the DCA exam using Docker EE. This Lesson deals with Security using Docker.

- Docker Security
    - By default namespaces and control group define the control and security measures.
    - Security by MTLS in a docker swarm.
    - Secure Docker Trusted Registry by certificates.
    - Docker content trust: Docker notary signs DTR and enforces policy. Enabled as env variable as DOCKER_CONTENT_TRUST = 1.
    - Enabled in UCP and set to run the only image that is signed by docker content trust.

- Configuring Docker Security.
    - Docker access control model (RBAC):
        - Subject: who are we talking about. ex: users
        - Roles: what can be done by the subject. ex: view
        - Resources: swarm collections
        - Grant: Combination of above as an ACL.
    - The docker access control can be done by UCP.
    - You can also use other certificates in DTR, UCP.
    - You can create a Security client bundle that includes security certificates and provide them to new users. 
    - You can also configure LDAP using UCP.
    - You can scan your images using DTR via system-> security-> Image scanning
