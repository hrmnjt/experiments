---
title: "Hugo: working with themes"
description: "Notes on better ways of working with Hugo themes"
date: 2020-10-30T20:33:13+04:00
draft: false
tags: [hugo]
---

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

