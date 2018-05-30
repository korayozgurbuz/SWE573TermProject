import tweepy
from tweepy import OAuthHandler
import csv
import operator
import datetime
import time


#Variables that contains the user credentials to access Twitter API
access_token = "75166266-lKHuaTrC4WBGdzp9oFvSJN2jFNe6BzEW1a7NHA59n"
access_secret = "3gorUNeoPdJHDzV1X02zoiuygRxOO9iwG82dUmHkKWfA1"
consumer_key = "zRuKIDvTumdERI0gi2MvoUAyG"
consumer_secret = "UkC1vHhQpxenaxXlyS2XFOMCsmLv1vsYGeVUbc1VkHQXT3iyg0"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
# csvFile = open('tweets.csv', 'a')
#Use csv Writer
# csvWriter = csv.writer(csvFile)

# ,"runthegame", "adidasMY", "adidasRunning"


avg_tweet_cutoff = 50 #bot sayilmasi icin gunde ortalama kac tweet'ten fazla atmasi gerekiyor bir profilin?
RT_cutoff = 95 #bot sayilmasi icin RT oraninin kaca esit veya uzerinde olmasi gerekiyor


def get_user_tweets(screen_name):
    # To overcome with the rate limit
    time.sleep(1)
    try:
        user_recent_tweets = api.user_timeline(screen_name=screen_name, count=100, include_rts=True)
    except Exception:
        return 0, 0, 0, 0

    count = 0
    retweets = 0
    total_number_tweets = 0

    for tweet in user_recent_tweets:
        total_number_tweets = tweet.user.statuses_count
        text_of_tweet = tweet.text
        count += 1
        if len(text_of_tweet) > 3:
            if text_of_tweet[0:4] == "RT @":
                retweets += 1
    try:
        date_of_account_creation = tweet.user.created_at
        account_active_days = datetime.datetime.now() - date_of_account_creation
        active_days_with_date = float(str(account_active_days).split()[0])
        average_number_of_tweet_per_day = (total_number_tweets*1.0) / active_days_with_date
        retweet_percentage = 100.0 * ((retweets * 1.0) / (count*1.00))
        return total_number_tweets, retweet_percentage, date_of_account_creation, average_number_of_tweet_per_day
    except Exception:
        return 0,0,0,0

bot_status_list = list()
retweet_status_list = list()
time_status_list = list()
user_nane_list = list()
tweet_text_list = list()

bot_file = open("Bot.txt", "r")

for screen_name in bot_file.readlines():
    is_bot = False
    print (screen_name)
    total_number_tweets, retweet_percentage, time_of_creation, average_no_per_day = get_user_tweets(screen_name)
    try:
        if retweet_percentage >= (RT_cutoff * 1.0):
            high_RT_check = 1
        else:
            high_RT_check = 0

        if average_no_per_day >= avg_tweet_cutoff:
            average_tweet_check = 1
        else:
            average_tweet_check = 0

        if high_RT_check or average_tweet_check:
            is_bot = True
            print ("BOT")
        else:
            print ("NOT BOT")
    except Exception:
        is_bot = True

    bot_status_list.append(is_bot)
print ("DONE")
