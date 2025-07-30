from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    expr,
    pandas_udf,
    PandasUDFType,
    explode,
    count,
    to_json,
    struct,
)
import pandas as pd
import spacy

# Load the spaCy model
print("Loading spaCy model...")
nlp = spacy.load("en_core_web_sm")

# Create Spark session
print("Creating Spark session...")
spark = (
    SparkSession.builder.appName("RedditNamedEntities")
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1")
    .config("spark.sql.adaptive.enabled", "false")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "false")
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    .config("spark.hadoop.fs.defaultFS", "file:///")
    .getOrCreate()
)

# Read from Kafka topic1
print("Reading from Kafka topic1...")
df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "topic1")
    .load()
)

# Parse the JSON messages
comments = df.selectExpr("CAST(value AS STRING)")


# Define a UDF to extract named entities
@pandas_udf("array<string>", PandasUDFType.SCALAR)
def extract_entities(texts: pd.Series) -> pd.Series:
    entities = []
    for text in texts:
        if text:
            doc = nlp(text)
            entities.append([ent.text for ent in doc.ents])
        else:
            entities.append([])
    return pd.Series(entities)


# Apply the UDF to extract entities
print("Extracting named entities...")
entities_df = comments.withColumn("named_entity", extract_entities(col("value")))

# Explode the entities and count them
exploded_entities = entities_df.select(explode(col("named_entity")).alias("entity"))
entity_counts = exploded_entities.groupBy("entity").count()

# Convert to JSON format for Kafka
kafka_output_df = entity_counts.selectExpr(
    "CAST(entity AS STRING) AS key", "to_json(struct(*)) AS value"
)

# Write to Kafka topic2
print("Starting streaming query to topic2...")
kafka_output_query = (
    kafka_output_df.writeStream.outputMode("update")
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("topic", "topic2")
    .option("checkpointLocation", "/tmp/spark_checkpoints")
    .start()
)

print("Streaming query started! Press Ctrl+C to stop...")
kafka_output_query.awaitTermination()
