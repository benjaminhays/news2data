#!/usr/bin/python
import os
from dotenv import load_dotenv
from feeds import twitter, news
from ingestion import elasticsearch
import json

load_dotenv()

## ElasticStack settings
ELASTICSEARCH_HOST = os.getenv("ES_HOST")
ELASTICSEARCH_PORT = int(os.getenv("ES_PORT"))

## Twitter related settings
TWITTER_SOURCES = os.getenv("TWITTER_SOURCES") # Comma seperated list of accounts (IE: "cyb3rops,CISACyber")
NEWS_SOURCES = os.getenv("RSS_SOURCES") # Comma seperated list of links

def main():
    # Fetch events from different sources
    twitter_events = twitter.fetch_events(TWITTER_SOURCES.split(","))
    news_events = news.fetch_events(NEWS_SOURCES.split(","))
    print(json.dumps(twitter_events + news_events))

    elasticsearch.ingest_events(twitter_events + news_events)

if __name__ == "__main__":
    main()
