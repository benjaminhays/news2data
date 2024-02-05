# News Sieve
A collection of tools for collecting, organizing, and ingesting information security news from many sources for future analysis. 

Currently the utility supports Twitter profiles and generic RSS feeds as data sources. It primarily serves to process and ingest events into an Elasticsearch instance, but I hope to support other formats in the future. 

## Quick Start
First, you'll either need to:
* change the default variables in `.env` to target your Elasticsearch server

```bash
ES_PORT=9200 # Change this
ES_HOST=127.0.0.1 # Change this
```

<ins>**OR:**</ins>

* deploy a new Elasticsearch instance (see the included docker-compose.yml file)

```bash
# in the main folder for news-sieve
sudo docker-compose up -d
```

After you've configured the Elasticsearch related settings, now bring your attention to the rest of the `.env` file, specifically the sources section. I've included some defaults, but you should modify them to capture the data you're most interested in.

```bash
# Data feeds
TWITTER_SOURCES=CISACyber,NISTcyber,SonicWallAlerts,Unit42_Intel
RSS_SOURCES=https://www.bleepingcomputer.com/feed/,https://www.theregister.com/security/headlines.atom,https://thehackernews.com/feeds/posts/default,https://www.cisa.gov/cybersecurity-advisories/all.xml
```

Once you have a suitable configuration, running the tool is as simple as:
```bash
./main.py
```