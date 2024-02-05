import requests
import feedparser
import json
import time

def fetch_events(accounts):
    base_url = "https://nitter.io.lol/"
    rss_url = "/rss"
    feeds = []
    events = []

    for account in accounts:
        url = base_url + account + rss_url
        response = requests.get(url)

        if response.status_code == 200:
            feeds.append(response)
        else:
            print(f"Failed to fetch feed for {account}")
            
    for feed in feeds:
        parsed = feedparser.parse(feed.content)
        for entry in parsed.entries:
            event = {}
            event["title"] = entry.title
            event["link"] = entry.link
            event["source"] = "Twitter"
            event["date"] = entry.published
            event["author"] = parsed.feed.title
            events.append(event)

    return events