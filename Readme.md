# MySQL-Kafka-Cassandra

## Objective
The objective of this project is to demonstrate a real-time data pipeline using MySQL, Apache Kafka, and Apache Cassandra. This setup allows for efficient data streaming and storage, showcasing how to handle large volumes of data in a distributed environment.

## Introduction
This project integrates MySQL as a relational database, Kafka as a message broker for real-time data streaming, and Cassandra as a NoSQL database for storing data at scale. The combination of these technologies allows for high-throughput data processing, making it suitable for applications requiring real-time analytics and data processing.

## Features
- **Real-time Data Ingestion**: Stream data from MySQL to Kafka for real-time processing.
- **Scalable Storage**: Store streamed data in Cassandra, providing high availability and scalability.
- **Fault Tolerance**: Ensure data integrity and fault tolerance in the event of system failures.
- **Decoupled Architecture**: Utilize Kafka to decouple data producers and consumers for better scalability.

## Architecture Diagram
![Architecture Diagram](https://github.com/Satyam20091998/MySql-Kafka-Cassandra/assets/92753984/9053e6a0-6c6a-4836-921c-65f659c608a8) <!-- Replace this with the actual link to your architecture diagram -->

## Installation
To set up the project, follow these steps:

### Prerequisites
- Docker
- Apache Kafka
- Apache Cassandra
- MySQL

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/Satyam20091998/MySql-Kafka-Cassandra.git
    cd MySql-Kafka-Cassandra
    ```
2. Set up Docker containers for Kafka and Cassandra.
3. Configure MySQL database with the required schema.
4. Run the Kafka producer to start streaming data.

## Usage
After setting up the project, you can use the following command to start the Kafka producer and stream data from MySQL to Kafka.

```bash
# Example command to start the producer
python producer.py
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [MySQL](https://www.mysql.com/) for database management.
- [Apache Kafka](https://kafka.apache.org/) for stream processing.
- [Apache Cassandra](https://cassandra.apache.org/) for NoSQL database solutions.
- Any other resources or libraries that were helpful in the development of this project.


### Notes
- Make sure to replace `link-to-your-diagram` with the actual link to your architecture diagram if you have one.
- You can adjust any sections to better reflect your project's specifics or add any additional information that may be relevant.



## Steps to setup projects

1. Use the docker file to run container for MYSQL

2. Then load the data in MYSQL and produce data using the kafka producer.

3.then load the data in cassandra

![Screenshot (6)](https://github.com/Satyam20091998/Spark-Kafka-MongoDB/assets/92753984/4e2fa654-e3d8-4d50-aeba-a10fd03c5812)
