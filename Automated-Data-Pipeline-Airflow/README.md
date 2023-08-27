# Weather Data Pipeline using Airflow and AWS S3

![Weather Data Pipeline Image](pipeline.png)

## Overview

This project is designed to collect weather data from a weather API and store it in an AWS S3 bucket in CSV format. The pipeline is orchestrated using Apache Airflow, ensuring automated and timely data collection and storage.

## Features

**1. Data Collection**
- The pipeline fetches weather data from a weather API.
- It supports dynamic configuration to collect data for different locations and parameters.

**2. Data Transformation**
- Collected data is transformed into a structured format suitable for analysis.
- Temperature values are converted from Kelvin to Celsius for easier interpretation.

**3. Data Storage**
- Transformed data is stored in an AWS S3 bucket in CSV format.
- The pipeline handles naming and organizing files based on timestamps.

**4. Scheduling**
- The data collection process is scheduled at regular intervals using Apache Airflow's scheduling capabilities.
- You can easily customize the schedule to meet your specific needs.

**5. Error Handling**
- Robust error-handling mechanisms are in place to ensure data integrity and reliability.
- Airflow's logging and alerting features help in identifying and resolving issues.

## Technologies Used

- **Apache Airflow**: Orchestrating the data pipeline and scheduling tasks.
- **Python 3**: Writing custom data collection and transformation scripts.
- **Pandas**: Data manipulation and transformation.
- **Boto3**: Interacting with AWS S3 for data storage.
- **Weather API**: Fetching weather data (replace with the name of the specific weather API you use).

## Usage

1. **Clone this repository to your local machine.**

   ```bash
   git clone https://github.com/your-username/Weather-Data-Pipeline.git
