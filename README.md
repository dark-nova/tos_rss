# TOS RSS
#### _or, [Tree of Savior][TOS] RSS Feed Project_

## Overview

Tree of Savior for the "international" region does not have its own RSS feed, so I sought to make one manually. This code scrapes one page of the "News" section of the website per run and creates an appropriate RSS [XML](feed.xml.original). (The `feed.xml.original` file serves as the template, but doesn't contain entries.)

For the live version, see [here](https://dark-nova.me/tos/feed.xml). The file is generated every hour using `cron`. You are free to use the live version however you see fit. For example, I have hooked it to [IFTTT](https://ifttt.com) to post automatic messages in Discord using webhooks as `That`.

[TOS]: https://treeofsavior.com/