import json
from datetime import datetime
from kafka import KafkaConsumer
import psycopg2
import logging

# Configure logging
logging.basicConfig(
    filename='consumer.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# Adjust parameters for your PostgreSQL setup
DB_PARAMS = {
    'dbname': 'weather_data',
    'user': 'postgres',
    'password': '1305',
    'host': 'localhost',
    'port': 5432
}

def connect_db():
    """Connect to PostgreSQL and return the connection."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        conn.autocommit = True
        return conn
    except Exception as e:
        logging.error("Error connecting to the database", exc_info=True)
        raise

def create_table(conn):
    """Create weather_events table if it doesn't exist."""
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS weather_events (
                id SERIAL PRIMARY KEY,
                city VARCHAR(50),
                temperature REAL,
                wind_speed REAL,
                humidity REAL,
                received_at TIMESTAMP
            );
        """)

def insert_record(conn, record):
    """Insert a record into weather_events."""
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO weather_events (city, temperature, wind_speed, humidity, received_at)
            VALUES (%s, %s, %s, %s, %s);
        """, (
            record['city'],
            record['temperature'],
            record['wind_speed'],
            record['humidity'],
            record['received_at']
        ))

def main():
    # Connect to Postgres and set up table
    conn = connect_db()
    create_table(conn)

    consumer = KafkaConsumer(
        'weather-data',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    logging.info("Kafka Consumer started...")

    try:
        for message in consumer:
            data = message.value
            data['received_at'] = datetime.now()
            logging.info(f"Received data: {data}")
            insert_record(conn, data)
    except KeyboardInterrupt:
        logging.info("Consumer stopped by user.")
    finally:
        consumer.close()
        conn.close()

if __name__ == "__main__":
    main()
