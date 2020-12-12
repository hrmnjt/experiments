---
title: "Hugo: working with themes"
description: "Notes on better ways of working with Hugo themes"
date: 2020-12-11T20:33:13+04:00
draft: false
tags: [hugo]
---

## What?

Personal websites are details which indicate the character and personality of 
author. This goes a long way to explain why there exists around thousand of 
themes associated with any of the static generator site be it Hugo, Jekyll or 
something new.

At the time of this blog, I'm using Hugo and wanted to safely try out a theme
for my existing project and I prefer the theme to be a submodule to involve 
minimal changes on the theme and explain the content in best way. While doing 
that I'm trying to check if the theme associates with me and I might be 
continuing on the same going ahead. So, here you go ...

## Checkout themes on existing project

Go to project
```bash
cd PROJECT_FOLDER
# cd code/sttp
```

Add theme as a submodule
```bash
git submodule add THEME_REPO themes/THEME_NAME
# git submodule add git@github.com:spookey/slick.git themes/slick
```

Change configurations
```bash
mv config.toml config.toml.bak
cp EXAMPLE_CONFIG config.toml
# cp themes/slick/_sites/config.toml config.toml
```

Serve, check and repeat!

## Removing a submodule theme completely

De-initializing submodule
```bash
git submodule deinit -f -- themes/THEME_NAME
# git submodule deinit -f -- themes/ezhil
```

Removing module files from `.git` folder
```bash
rm -rf .git/modules/themes/THEME_NAME
# rm -rf .git/modules/themes/ezhil
```

Removing theme submodule folder itself
```bash
git rm -rf themes/THEME_NAME
# git rm -rf themes/ezhil
```

