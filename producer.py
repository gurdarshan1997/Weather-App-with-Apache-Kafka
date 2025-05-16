import json
import random
import time
from kafka import KafkaProducer
import logging

# Configure logging
logging.basicConfig(
    filename='producer.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

WEATHER_RANGES = {
    "Winnipeg": {
        "temperature": (-30, 30),
        "wind_speed": (0, 50),
        "humidity": (20, 80)
    },
    "Vancouver": {
        "temperature": (-10, 25),
        "wind_speed": (0, 30),
        "humidity": (30, 99)
    }
}

def generate_weather_data(city):
    """Generate synthetic weather data for a given city."""
    ranges = WEATHER_RANGES[city]
    data = {
        "city": city,
        "temperature": round(random.uniform(*ranges["temperature"]), 2),
        "wind_speed": round(random.uniform(*ranges["wind_speed"]), 2),
        "humidity": round(random.uniform(*ranges["humidity"]), 2)
    }
    return data

def main():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    logging.info("Kafka Producer started...")

    try:
        while True:
            for city in WEATHER_RANGES:
                weather_data = generate_weather_data(city)
                producer.send('weather-data', weather_data)
                logging.info(f"Sent data: {weather_data}")

            # Wait 5 seconds before next iteration
            time.sleep(5)

    except KeyboardInterrupt:
        logging.info("Producer stopped by user.")
    finally:
        producer.close()

if __name__ == "__main__":
    main()
