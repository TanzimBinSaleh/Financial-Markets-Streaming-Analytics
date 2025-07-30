# 📊 Real-Time Financial Market Sentiment Analysis

**A production-ready streaming analytics system that processes live financial discussions from Reddit's WallStreetBets community using Apache Kafka, PySpark, and Elasticsearch to identify trending stocks and market sentiment patterns.**

![Financial Sentiment Analysis](https://img.shields.io/badge/Domain-Financial%20Technology-brightgreen)
![Real-time](https://img.shields.io/badge/Processing-Real--time-blue)
![Tech Stack](https://img.shields.io/badge/Stack-Kafka%20%7C%20Spark%20%7C%20Elasticsearch-orange)

## 🎯 **Project Overview**

This system captures and analyzes real-time trading discussions, extracting financial entities (stock tickers, company names, trading terms) and visualizing market sentiment trends for investment intelligence and market analysis.

### **Key Features**

- 🔴 **Live Data Streaming**: Real-time comment ingestion from WallStreetBets
- 🧠 **Named Entity Recognition**: Automatic extraction of financial entities using spaCy
- ⚡ **High-Performance Processing**: Stream processing with Apache Kafka & PySpark
- 📈 **Interactive Dashboards**: Kibana visualizations for market sentiment analysis
- 🎯 **Investment Intelligence**: Track trending stocks, viral discussions, and market sentiment

## 🏗️ **System Architecture**

```
Reddit API (PRAW) → Kafka → PySpark (NER) → Kafka → Logstash → Elasticsearch → Kibana
```

1. **Data Source**: WallStreetBets subreddit via Reddit API
2. **Stream Processing**: Kafka topics for reliable data transmission
3. **NLP Processing**: PySpark + spaCy for financial entity extraction
4. **Data Storage**: Elasticsearch for fast search and analytics
5. **Visualization**: Kibana dashboards for real-time insights

## 📊 **Analytics & Visualizations**

### **Dashboard 1: Top Trending Stocks** 📈

- **Type**: Vertical Bar Chart
- **Purpose**: Shows most discussed financial entities in real-time
- **Metrics**: Mention count, trending analysis
- **Update Frequency**: Real-time (30-minute windows)

### **Dashboard 2: Financial Sentiment Word Cloud** ☁️

- **Type**: Tag Cloud Visualization
- **Purpose**: Visual representation of market discussion intensity
- **Features**: 50+ financial terms, size-based popularity
- **Insights**: Immediate visual sentiment indicators

### **Dashboard 3: Stock Ticker Focus** 🎯

- **Type**: Horizontal Bar Chart
- **Purpose**: Tracks specific high-value stocks (SPY, UNH, Tesla, META, etc.)
- **Filtering**: Focused on major market movers
- **Business Value**: Investment decision support

## 🛠️ **Technology Stack**

| **Component**         | **Technology**    | **Purpose**                |
| --------------------- | ----------------- | -------------------------- |
| **Data Source**       | Reddit API (PRAW) | Live comment streaming     |
| **Message Queue**     | Apache Kafka      | Reliable data transmission |
| **Stream Processing** | PySpark + spaCy   | NLP & entity extraction    |
| **Data Storage**      | Elasticsearch     | Fast search & analytics    |
| **Visualization**     | Kibana            | Interactive dashboards     |
| **Language**          | Python 3.9+       | Core application logic     |

## 🚀 **Setup & Installation**

### **Prerequisites**

- Python 3.9+
- Java 17+ (for Kafka/Spark)
- Docker (for Elasticsearch)
- Homebrew (macOS) or equivalent package manager

### **1. Environment Setup**

```bash
# Clone the repository
git clone <repository-url>
cd Financial-Markets-Streaming-Analytics

# Create virtual environment
python -m venv financial_streaming_env
source financial_streaming_env/bin/activate  # On Windows: financial_streaming_env\Scripts\activate

# Install dependencies
pip install praw kafka-python pyspark requests spacy
python -m spacy download en_core_web_sm
```

### **2. Infrastructure Setup**

```bash
# Install and start Kafka
brew install kafka
brew services start zookeeper
brew services start kafka

# Install and start Elasticsearch
docker run -d --name elasticsearch -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.15.0

# Install Logstash
brew install logstash
```

### **3. Reddit API Configuration**

Update `reddit_to_kafka.py` with your Reddit API credentials:

```python
reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    user_agent="Financial-Markets-Analytics/1.0"
)
```

## 🎮 **Running the System**

### **Step 1: Start Infrastructure**

```bash
# Ensure Kafka and Elasticsearch are running
brew services start kafka
docker start elasticsearch
```

### **Step 2: Start Data Pipeline**

```bash
# Terminal 1: Start Reddit data streaming
python reddit_to_kafka.py

# Terminal 2: Start PySpark processing
python spark_processor.py

# Terminal 3: Start Logstash data forwarding
logstash -f logstash.conf
```

### **Step 3: Access Analytics**

1. **Kibana Dashboard**: http://localhost:5601
2. **Elasticsearch**: http://localhost:9200
3. **Create Index Pattern**: `redditvisualize*`
4. **Import Visualizations**: Use the three dashboard configurations above

**Tech Stack**: Python | Apache Kafka | PySpark | Elasticsearch | Kibana | spaCy NLP | Reddit API | Docker  
**Domain**: Financial Technology | Real-time Analytics | Big Data | Market Intelligence
