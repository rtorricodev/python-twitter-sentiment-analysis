from twiter_apy import *
from textblob import TextBlob
import string

#files

def save_in(my_file,text):
    file = open(my_file,'w') 
    file.write(text) 
    file.close()

def save_list_in_file(my_file,my_list):
    with open(my_file, mode="w") as outfile:  
        for element in my_list:
            outfile.write(str("\n") + str(element))

# twits

def show_twits(public_twits):
    for tweet in public_twits:
        print tweet.text

def save_twits_in_list(my_list,public_twits):
    for tweet in public_twits:
        my_list.append(tweet.text.encode('utf-8'))
    return my_list

#sentiments

def show_twits_sentiments(public_twits):
    for tweet in public_twits:
        analysis = TextBlob(tweet.text)
        print analysis.sentiment

def save_twits_sentiments_in_list(my_list,public_twits):
    for tweet in public_twits:
        analysis = TextBlob(tweet.text)
        analysis_sentiment = str(analysis.sentiment)
        analysis_sentiment = analysis_sentiment.translate(string.maketrans('', ''), 'Sentiment=polarysubjcv()')
     
        # analysis_sentiment = analysis_sentiment + ','
        my_list.append(analysis_sentiment)
    return my_list

query = 'bitcoin'
max_tweets = 2000
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

show_twits_sentiments(searched_tweets)

my_list = []
my_list = save_twits_sentiments_in_list(my_list,searched_tweets)
save_list_in_file('r.txt',my_list)