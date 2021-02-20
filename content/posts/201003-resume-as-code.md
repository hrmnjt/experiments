---
title: "Resume as Code (RaS)"
description: "Journey on codifying and version controlling resume"
date: 2020-10-03T23:33:13+04:00
draft: false
tags: [as-code]
---

# Resume as Code (RaS)

TL; DR - [hrmnjt/resume](https://github.com/hrmnjt/resume)

This weekend I tasked myself to update my resume; I've dreaded the concept of 
resume in the past as it seems borderline (strong word:)narcissistic. In order 
to make it fun for me, and to check one of the items in my list, I decided to 
make my resume using LaTeX.

## Why LaTeX?

In past, I'd wonder why all journals and papers published always followed 
similar pattern and I thought to myself that it would be a criteria to write 
the journal/paper in that particular format. Researching deeper, I realized 
the reason it all looks similar was because in academics, people use a 
different word processing engine - one which came with its own set of awesome 
features.

- Macros and microtype
- Programmatic approach on visual formatting
- Pixel perfect typography for mathematics (haven't used it yet, but excited)
- Huge community (mostly nerds and geeks)

But the most understated reason that I felt was **codifying the document and 
version controlling**. Publishing documents as Git repositories seem like the 
most natural approach for editing and improving them over time.

## How?

I started with [Overleaf quickstart](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) 
which is great resource to kick-start your LAH-tek experience. Although, 
instead of using their online editor, I wanted to edit the documents at my 
own terms. I hate putting personal data on servers which I don't trust very 
well (no offense Overleaf. Love you lots!)

Instead of installing the binaries and I chose to go the Docker way

```dockerfile
# Dockerfile
FROM ubuntu:xenial
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q && apt-get install -qy \
    curl jq \
    texlive-full \
    python-pygments gnuplot \
    make git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /data
VOLUME ["/data"]
```

Steps to build and run
```bash
docker build -t latex .
docker run --rm -i -v "$PWD":/data latex pdflatex YOURFILE.tex
```

*This assumes the file `YOURFILE.tex` is present in the `pwd`*

Alternatively, you can choose to [install the binaries](https://www.latex-project.org/get/). 

For the template, I choose the basic single-column format with default 
formatting, except the font to be Sans Serif instead. Inspiration for the same 
came from [Sourabh Bajaj's Resume](https://github.com/sb2nov/resume).

Check out the repo: [hrmnjt/resume](https://github.com/hrmnjt/resume)
