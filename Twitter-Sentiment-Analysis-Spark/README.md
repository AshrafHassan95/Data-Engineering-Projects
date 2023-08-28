# Twitter Sentiment Analysis using Spark

**Performing sentiment analysis on Twitter data using Apache Spark and TextBlob.**

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Dataset](#dataset)
- [Results](#results)

---

## Prerequisites

Before running this Spark application, ensure you have the following prerequisites installed:

- **Python**: Make sure you have Python installed on your system.

- **Apache Spark**: Install Apache Spark.

- **TextBlob library**: Install TextBlob using pip:

  ```bash
  pip install textblob

# Usage

## Clone or Download
Clone or download this repository to your local machine.

## Twitter Data
Prepare your Twitter data in CSV format. In this project, the filename is set to `blockchain.csv`. You can replace it with your own file.

## Run the Application
Execute the Spark application with the following command:

  ```bash
  spark-submit twitter_sentiment_analysis.py
```


Replace `twitter_sentiment_analysis.py` with your actual filename.

## Analysis Process

The application reads Twitter data, cleans it by removing URLs, mentions, numbers, and special characters, and performs sentiment analysis using TextBlob. The results are categorized as "Positive," "Negative," or "Neutral."

## Save Results

The analyzed data will be saved in a directory named "project_twitter" as text files.

# Code Explanation

Here's a brief overview of the main components of the code:

- The `abb_en` function replaces common abbreviations with their full forms.

- The `remove_features` function removes URLs, mentions, numbers, and other unwanted features from the tweet text.

- The `calculate` function categorizes sentiment values into "Positive," "Negative," or "Neutral."

- The `main` function is the entry point of the Spark application. It reads Twitter data, processes it, and performs sentiment analysis. The results are saved in the "project_twitter" directory.

- The Spark application is configured to run locally on one core using SparkConf.

# Dataset

You need to provide your own Twitter dataset in CSV format. Ensure that the CSV file contains at least 8 columns, and the tweets are in one of the columns. The code shows that the tweet text is in the eighth column of the CSV file.

# Results

The sentiment analysis results will be saved in the "project_twitter" directory as text files, with each line containing a tweet and its corresponding sentiment category.

Feel free to customize the code and the input dataset according to your requirements. Happy sentiment analysis!
