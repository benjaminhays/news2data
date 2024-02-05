from elasticsearch import Elasticsearch
from datetime import datetime
from dateutil import parser
from dotenv import load_dotenv
import os

load_dotenv()

## ElasticStack settings
ELASTICSEARCH_HOST = os.getenv("ES_HOST")
ELASTICSEARCH_PORT = int(os.getenv("ES_PORT"))

ELASTICSEARCH_INDEX = "news_events"

def ingest_events(events):
    # Initialize Elasticsearch client
    es = Elasticsearch([{"host": ELASTICSEARCH_HOST, "port": ELASTICSEARCH_PORT, "scheme": "http"}])

    # Create the index if it doesn't exist
    if not es.indices.exists(index=ELASTICSEARCH_INDEX):
        es.indices.create(index=ELASTICSEARCH_INDEX)

    # Ingest unique events into Elasticsearch
    for event in events:
        # Check for duplicates based on the title
        if not is_duplicate(es, ELASTICSEARCH_INDEX, "title", event["title"]):
            # Format the date to Elasticsearch format
            event["date"] = parse_date(event["date"])
            
            # Ingest the event into Elasticsearch
            es.index(index=ELASTICSEARCH_INDEX, body=event)

def parse_date(date_str):
    try:
        # Try parsing the date using dateutil.parser
        parsed_date = parser.parse(date_str)
        return parsed_date.isoformat()
    except ValueError:
        # Handle parsing errors and return None
        print(f"Error parsing date: {date_str}")
        return None

def is_duplicate(es, index, field, value):
    # Check if an event with the same title already exists
    query = {"query": {"match": {field: value}}}
    result = es.search(index=index, body=query)

    return result["hits"]["total"]["value"] > 0