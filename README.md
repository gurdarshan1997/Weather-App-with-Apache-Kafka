# Weather-App with Apache Kafka

**Assignment 5: Data Streaming with Apache Kafka**  
**Course:** Data Acquisition and Management  
**Instructor:** Muhammad Shahin  
**Program:** PGDM in Predictive Analytics  
**Author:** Gurdarshan Singh  
**Due Date:** February 23, 2025

---

## ✨ Objective

To develop a streaming data pipeline using Apache Kafka that simulates weather data for two Canadian cities (Winnipeg and Vancouver), transmits it in real time to a Kafka topic, and stores it into a PostgreSQL database for analysis.

---

## 📆 Project Overview

### 🛠 Components

- **Kafka Producer (`producer.py`)**  
  Generates and sends synthetic weather data every 5 seconds to a Kafka topic called `weather-data`. Logs all events to `producer.log`.

- **Kafka Consumer (`consumer.py`)**  
  Reads data from `weather-data` topic, appends a `received_at` timestamp, and inserts each record into a PostgreSQL table named `weather_events`. Logs all insertions to `consumer.log`.

- **PostgreSQL Database**  
  - Database: `weather_data`  
  - Table: `weather_events` with columns: city, temperature, wind_speed, humidity, received_at

- **Kafka Topic**  
  - Name: `weather-data`  
  - Partition: 1  
  - Replication: 1

---

## 📂 Files in This Repository

### 💻 Code
- `producer.py` — Python script to generate and send weather data
- `consumer.py` — Python script to consume and store weather data

### 📄 Logs
- `producer.log` — Event logs from the Kafka producer
- `consumer.log` — Event logs from the Kafka consumer

### 📝 Report
- `assignment_5.pdf` — Final assignment report with implementation steps, screenshots, and observations

### 📊 (Optional)
- `weather_data_backup.sql` — Optional PostgreSQL dump of the database (use `pg_dump` to generate)

---

## ⚡ How to Run

> Prerequisites: Kafka, Zookeeper, PostgreSQL must be installed and configured.

1. **Start Zookeeper**  
2. **Start Kafka Broker**  
3. **Create Kafka Topic** `weather-data`  
4. **Run Producer:**  
   ```bash
   python3 producer.py
   ```
5. **Run Consumer:**  
   ```bash
   python3 consumer.py
   ```
6. Let it run for ~10 minutes  
7. **Stop the Producer** (Ctrl+C)
8. **Query Data in PostgreSQL:**  
   ```sql
   SELECT * FROM weather_events;
   ```
9. **Stop Consumer, Kafka, and Zookeeper**

---

## 📊 Output & Results

- 272+ weather records ingested and stored in real time
- Verified database entries for both cities with timestamp
- Producer and consumer logs confirm smooth operation

---

## ✅ Conclusion

This project successfully demonstrates a working real-time data pipeline using Apache Kafka and PostgreSQL. All steps of the assignment were executed as instructed. For future production use, this setup could be enhanced with features like schema registry, Kafka Connect, horizontal scaling, and data visualization dashboards.

---

## 📷 Screenshots
> *(To be embedded manually in GitHub or included in `assignment_5.pdf`)*
- Zookeeper and Kafka terminals
- Topic creation
- Producer and consumer terminals
- Logs
- PostgreSQL table output
