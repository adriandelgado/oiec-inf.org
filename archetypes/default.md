---
title: "{{ replace .Name "-" " " | title }}"
description: ""
date: {{ .Date }}
{{ dateFormat "2006" .Date }}: "{{ dateFormat "01" .Date }}"
author:
tags: []
categories: []
images: ["thumbnail.png"]
draft: false
---
