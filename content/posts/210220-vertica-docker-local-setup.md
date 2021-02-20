---
title: "Vertica: docker(ized) development setup"
description: "Notes on setting up a local development environment for Vertica"
date: 2021-02-20T23:09:13+04:00
draft: false
tags: [vertica, homeserver]
---

## Enter the problem

At (current) work, Vertica serves the analytical workloads and as with all 
software, there are few things that we love about Vertica (speed) and few 
are idiotic/confusing. One such hassle for everyday work with Vertica is User 
and Access management.

Vertica provides a very minimal and essential user, role and access management 
through the 
[Adminstrative functions](https://www.vertica.com/docs/10.1.x/HTML/Content/Authoring/AdministratorsGuide/DBUsersAndPrivileges/ManagingUsersAndPrivileges.htm) 
which would work well for most installations. There is 
[Management Console](https://www.vertica.com/docs/10.1.x/HTML/Content/Authoring/ManagementConsole/GettingStartedWithMC/GettingStartedWithMC.htm) 
which could be installed but as of today can only 
[manage MC users](https://www.vertica.com/docs/10.1.x/HTML/Content/Authoring/ManagementConsole/ManagingUsersandPrivileges/ManagingUsersAndPrivileges.htm) 
and not DB users and roles. There is a promise of this improving in the future 
versions of Vertica but I was impatient and I started to think about 
[`vam!`](https://github.com/hrmnjt/vam)

In order to develop and work with Vertica, I needed a local development setup 
which is reproducible and easy to startup.

## Thought process

I chose to local Vertica on my home server and since I would want to persist 
data for Vertica while I didn't want to install on server directly, I chose to 
run it on a docker(ized) setup. As of now, there are no official docker(ized) 
setup for Vertica. I started to seek open source repos from awesome people 
of the Internet to solve my development Vertica setup.

If you search `docker + vertica` on Google or Dockerhub, you would get 
hundreds of docker images. Most of them work well, but I had two essential 
criteria to choose among all the images:
- GDB installed to register and run Vertica UDFs
- Multinode setup for latest Vertica version (10.1 at the time of this post)
- Sample database - VMart database provided (default) by Vertica

With this in mind, I narrowed to 
[docker-vertica](https://github.com/francoisjehl/docker-vertica) by 
[Github](https://github.com/francoisjehl) (also listed on 
[awesome-vertica](https://github.com/vertica/awesome-vertica))

## Setup

The steps on repo is pretty straight forward. Re-iterating for my reference.

### Step 1 - Setup repository

I chose to fork the repo so I can enable VMart and enable MC.
```bash
git clone git@github.com:francoisjehl/docker-vertica.git
# git clone git@github.com:hrmnjt/docker-vertica.git
cd docker-vertica
```

I've changed two configurations as of now, to enable VMart DB.
1. In `docker-compose.yml`
```docker
...
      WITH_VMART: 'true' 
...
```
1. In `Dockerfile`
```docker
# Environment Variables
ENV VERTICA_HOME=/opt/vertica \
    WITH_VMART=true \
    NODE_TYPE=master \
    CLUSTER_NODES=localhost \
    GDBSERVER_PORT=2159 \
    ENABLE_WATCHDOG=false
```

### Step 2 - Download Vertica RPM

- Create an account on Vertica and RPM for RHEL can be 
downloaded from 
[Community Edition page](https://www.vertica.com/download/vertica/community-edition/) 
- Enable the `VERTICA_RPM_PATH` variable
```bash
echo 'export VERTICA_RPM_PATH=/opt/vertica/vertica-10.1.0-0.x86_64.RHEL6.rpm' >> ~/.bashrc 
```

### Step 3 - Build, run and operate

To build and run
```bash
docker-compose build
docker-compose run -d
```

To stop gracefully
```bash
docker-compose kill -s SIGINT
```

## What's next?

This was a cheap effort to run the development Vertica and to get unblocked for 
`vam!`. Post this I would like to do few things:
- Move the setup to Nomad + base installation to have cleaner setup, start and 
run
- Enable Vertica monitoring console
- Enable metrics with Prometheus and Grafana

Until then, cheers!
