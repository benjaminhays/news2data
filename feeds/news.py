import requests
import feedparser
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

def fetch_events(links):
    feeds = []
    events = []

    for link in links:
        response = requests.get(link, headers=headers)

        if response.status_code == 200 or response.status_code == 304:
            feeds.append(response)
        else:
            print(f"Failed to fetch feed for {link}")
            
    for feed in feeds:
        parsed = feedparser.parse(feed.content)
        for entry in parsed.entries:
            event = {}
            event["title"] = entry.title
            event["link"] = entry.link
            event["date"] = entry.published
            event["source"] = "RSS"
            event["author"] = parsed.feed.title
            events.append(event)

    return events