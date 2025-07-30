import praw
from kafka import KafkaProducer
import json

# Reddit API credentials
reddit = praw.Reddit(
    client_id="oo4ywKnj4XBIFwM2O8hl8Q",
    client_secret="FuNXiBs9mn0XQxfnLEN96kIggicbOg",
    user_agent="Financial-Markets-Analytics/1.0",
)

# Kafka configuration
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)

# Subreddit to stream comments from - WallStreetBets for financial sentiment
subreddit = reddit.subreddit("wallstreetbets")

for comment in subreddit.stream.comments():
    try:
        # Prepare the message
        message = {"author": str(comment.author), "body": comment.body}

        # Send the message to Kafka topic
        producer.send("topic1", value=message)
        print(f"Sent: {message}")
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"An error occurred: {e}")
