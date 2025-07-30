import praw
from kafka import KafkaProducer
import json
from datetime import datetime

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

print("🚀 Starting Enhanced Financial Markets Data Collection...")
print("📊 Capturing: Upvotes, Awards, Comment Length, Sentiment Indicators")

for comment in subreddit.stream.comments():
    try:
        # Enhanced message with upvotes and metadata
        enhanced_message = {
            "author": str(comment.author),
            "body": comment.body,
            "score": comment.score,  # 🔥 UPVOTES!
            "upvote_ratio": getattr(comment, "upvote_ratio", None),
            "total_awards_received": comment.total_awards_received,
            "controversiality": comment.controversiality,
            "comment_length": len(comment.body),
            "created_utc": comment.created_utc,
            "timestamp": datetime.utcnow().isoformat(),
            "permalink": f"https://reddit.com{comment.permalink}",
            "parent_id": comment.parent_id,
            "submission_title": (
                comment.submission.title if hasattr(comment, "submission") else None
            ),
            "submission_score": (
                comment.submission.score if hasattr(comment, "submission") else None
            ),
        }

        # Send enhanced data to Kafka topic1 (for entity processing)
        basic_message = {
            "author": enhanced_message["author"],
            "body": enhanced_message["body"],
        }
        producer.send("topic1", value=basic_message)

        # Send enhanced data to new topic for comment analysis
        producer.send("reddit_comments", value=enhanced_message)

        # Print with upvote info
        print(
            f"📈 {enhanced_message['score']} upvotes | {enhanced_message['author']}: {enhanced_message['body'][:100]}..."
        )

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"An error occurred: {e}")

print("Enhanced data collection stopped.")
