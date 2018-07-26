import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key ='dTG24NJgFeIZ8VkWN3H7ZFTYR'
consumer_secret = 'I0NnZaH000KS6IMAEB7AvnTJw6YLeRj5eazo64HfkkTv23D23z'
access_token ='1909906172-zhXPdYxASxriH5b5XWAiUze8RQgObpJ1kfvdaOp'
access_secret ='i5QCVH5yTbjdYudmMmBrOYqckO3C04w00VltmucNUGoEQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('Data11#Tags.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#Ecuador ,#InfanciaSinViolencia",count=100,
                           lang="es",
                           since="2015-01-01").items():
	print (tweet.created_at, tweet.text)
	csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
