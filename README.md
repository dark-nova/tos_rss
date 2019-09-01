# Tree of Savior RSS Feed Project

## Overview

[Tree of Savior][TOS] for the "international" region does not have its own RSS feed, so I sought to make one manually. This code scrapes one page of the "News" section of the website per run and creates an appropriate RSS [feed](feed.xml.original). (The `feed.xml.original` file serves as the template, but doesn't contain entries.)

## Usage

Run [`feed.py`](feed.py). You may also run [`db.py`](db.py) first to create the necessary database.

## Requirements

This code is designed around the following:

- Python 3.5+
- `bs4` and its dependencies, used for scraping
- `feedgen` and its dependencies, used for creating the RSS feed
- `pendulum` and its dependencies, used for date and time
- other [requirements](requirements.txt)

## Setup

Set up your environment for self-hosting. Read [Requirements](#Requirements) for dependencies.
Python `venv` is highly recommended for managing your files, including dependencies.
Like so:

```
$ git clone <url> && cd tos_rss
$ # venv may be installable in package management.
$ # For Debian-like distros, `apt install python3-venv`
$ python -m venv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
```

No other configuration is necessary.

## Live Version

See [here](https://dark-nova.me/tos/feed.xml). The file is generated every hour using `cron`. You are free to use the live version however you see fit.

For example, I have used [IFTTT](https://ifttt.com) to post automatic messages in [Discord](https://discordapp.com). (If **RSS Feed**, then **Webhooks**.)

## Disclaimer

This project is not affiliated with or endorsed by Tree of Savior. See [`LICENSE`](LICENSE) for more detail.

[TOS]: https://treeofsavior.com/
