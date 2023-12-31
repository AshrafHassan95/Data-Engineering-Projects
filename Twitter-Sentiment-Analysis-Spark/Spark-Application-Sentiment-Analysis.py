from textblob import TextBlob
from pyspark import SparkConf, SparkContext
import re

def abb_en(line):
    abbreviation_en = {
        'u': 'you',
        'thr': 'there',
        'asap': 'as soon as possible',
        'lv': 'love',
        'c': 'see'
    }
    abbrev = ' '.join(abbreviation_en.get(word, word) for word in line.split())
    return abbrev

def remove_features(data_str):
    url_re = re.compile(r'https?://(www.)?\w+\.\w+(/\w+)*/?')
    mention_re = re.compile(r'@|#(\w+)')
    RT_re = re.compile(r'RT(\s+)')
    num_re = re.compile(r'(\d+)')
    
    data_str = str(data_str)
    data_str = RT_re.sub(' ', data_str)
    data_str = data_str.lower()
    data_str = url_re.sub(' ', data_str)
    data_str = mention_re.sub(' ', data_str)
    data_str = num_re.sub(' ', data_str)
    return data_str

def calculate(value):
    if value > 0.0:
        return "Positive"
    elif value < 0.0:
        return "Negative"
    else:
        return "Neutral"

def main(sc, input_filename, output_folder):
    sentiment = sc.textFile(input_filename) \
        .map(lambda x: x.split(",")) \
        .filter(lambda x: len(x) == 8 and len(x[0]) > 1) \
        .map(lambda x: x[7].lower()) \
        .map(lambda x: remove_features(x)) \
        .map(lambda x: abb_en(x)) \
        .map(lambda x: x.replace("'", "")) \
        .map(lambda x: x.replace('"', '')) \
        .map(lambda x: TextBlob(x).sentiment.polarity) \
        .map(lambda x: calculate(x))

    full = sc.textFile(input_filename) \
        .map(lambda x: x.split(",")) \
        .filter(lambda x: len(x) == 8 and len(x[0]) > 1)

    new = full.zip(sentiment) \
        .map(lambda x: str(x).replace("'", "")) \
        .map(lambda x: str(x).replace('"', ''))

    new.saveAsTextFile(output_folder)

if __name__ == "__main__":
    conf = SparkConf().setMaster("local[1]").setAppName("Twitter_Sentiment_Analysis")
    sc = SparkContext(conf=conf)
    
    input_filename = "blockchain.csv"
    output_folder = "project_twitter_output"
    
    main(sc, input_filename, output_folder)
    
    sc.stop()
