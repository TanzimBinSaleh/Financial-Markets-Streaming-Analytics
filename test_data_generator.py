import random
import json
from kafka import KafkaProducer

# Mock Financial data for testing
financial_entities = [
    "SPY",
    "QQQ",
    "Tesla",
    "Apple",
    "Microsoft",
    "Google",
    "Amazon",
    "Meta",
    "Netflix",
    "Nvidia",
    "AMD",
    "Intel",
    "JPMorgan",
    "Goldman Sachs",
    "Bank of America",
    "Wells Fargo",
    "Morgan Stanley",
    "Berkshire Hathaway",
    "Johnson & Johnson",
    "Pfizer",
    "Coca-Cola",
    "PepsiCo",
    "McDonald's",
    "Walmart",
    "Target",
    "Home Depot",
    "Visa",
    "Mastercard",
    "PayPal",
]

market_terms = [
    "calls",
    "puts",
    "bulls",
    "bears",
    "diamond hands",
    "paper hands",
    "YOLO",
    "to the moon",
    "stonks",
    "tendies",
    "apes",
    "retards",
    "squeeze",
    "hedge funds",
    "shorts",
    "longs",
    "gamma",
    "theta",
    "volatility",
    "earnings",
    "Fed",
    "Powell",
    "rates",
    "inflation",
]

trading_comments = [
    "Just bought {} calls, let's go!",
    "{} is going to the moon! 🚀",
    "Why is {} dumping so hard?",
    "Time to buy the {} dip",
    "{} earnings gonna be huge",
    "Diamond hands on {} until $1000",
    "Paper hands selling {} at a loss",
    "YOLO'd my life savings into {}",
    "{} squeeze incoming!",
    "Fed gonna tank {} today",
    "Rate cut will pump {}",
    "Inflation data will affect {}",
    "{} option flow looking bullish",
    "Gamma squeeze on {} possible",
    "Short interest on {} is massive",
]

authors = [
    "DiamondHands_Dave",
    "YOLO_Trader",
    "BullMarket_Bob",
    "BearKiller_99",
    "TendieHunter",
    "WSB_Veteran",
    "OptionOracle",
    "StockSavant",
    "MarketMaker_Mike",
    "CryptoKing",
    "GammaGuru",
    "ThetaGang_Leader",
    "VolatilityViper",
    "EarningsExpert",
    "FedWatcher",
    "InflationInsider",
]

print("Starting Financial Markets test data generator...")

# Kafka configuration
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)

try:
    for i in range(50):  # Generate 50 test messages

        # Random financial discussion scenarios
        scenario = random.choice(
            [
                "stock_discussion",
                "options_play",
                "market_analysis",
                "earnings_discussion",
                "fed_discussion",
            ]
        )

        if scenario == "stock_discussion":
            entity1 = random.choice(financial_entities)
            entity2 = random.choice([t for t in financial_entities if t != entity1])
            comment = f"{entity1} vs {entity2} - which one you buying?"

        elif scenario == "options_play":
            entity = random.choice(financial_entities)
            comment = random.choice(trading_comments).format(entity)

        elif scenario == "market_analysis":
            entity = random.choice(financial_entities)
            term = random.choice(market_terms)
            comment = f"Technical analysis shows {entity} breaking resistance. {term.capitalize()} incoming!"

        elif scenario == "earnings_discussion":
            entity = random.choice(financial_entities)
            comment = f"{entity} earnings next week. Expecting big moves!"

        else:  # fed_discussion
            entity = random.choice(financial_entities)
            comment = (
                f"Fed meeting today will impact {entity} heavily. Rate cut priced in?"
            )

        message = {"author": random.choice(authors), "body": comment}

        # Send to Kafka topic1
        producer.send("topic1", value=message)
        print(f"Sent: {message}")

        # Small delay to simulate real-time streaming
        import time

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Test data generation stopped.")

except Exception as e:
    print(f"Error: {e}")

finally:
    producer.close()
    print("Financial markets test data generator stopped.")
