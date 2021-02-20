---
title: "Hugo: publishing with Github Actions"
description: "Notes on approach to deploy Hugo content to Github Pages using Github Actions"
date: 2020-12-13T02:09:13+04:00
draft: false
tags: [hugo]
---

# Hugo: publishing with Github Actions

Notes on publishing static website (personal) created with Hugo on
Github Pages using Github Actions

## Why?

Why not?

**Hugo** - is a fast static site generator and it is also the gopher way of 
publishing a personal website

**Github Pages** - allows you to publish static content for free hosting. BONUS: it 
applies SSL certificates required automatically and makes your site hosting 
secure. BLUF: who doesn't like free secure hosting?

**Github Action** - is a service to run CI actions on a Github repository.
BONUS: it is free for open source repository. BLUF: who doesn't like free CI 
server to build and deploy.

## How?

If you want to setup a static site, start with [Hugo Quickstart](https://gohugo.io/getting-started/quick-start/)

If you want to setup Github pages for custom domain, start with 
[this awesome stack overflow answer](https://stackoverflow.com/a/9123911/10046768)

I use free Github marketplace Action created by [@peaceiris](https://github.com/peaceiris) and has helped a lot of people deploy their sites for free.

[Github Actions workflow](https://github.com/hrmnjt/sttp/blob/master/.github/workflows/main.yml)

I'll comment the worflow file itself to provide maximum details on steps 
included and you can always refer to the awesome source repo itself:
- [To build Hugo](https://github.com/peaceiris/actions-hugo)
- [To deploy on Github Pages](https://github.com/peaceiris/actions-gh-pages)
