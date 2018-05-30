from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.contrib.auth import views as auth_views
import tweepy
from django.conf import settings
from utils.utils import get_user_tweets

User = get_user_model()



@login_required
def bot_detector(request):
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
    auth.set_access_token(settings.access_token, settings.access_secret)
    api = tweepy.API(auth)


    bot_status_list = list()
    retweet_status_list = list()
    time_status_list = list()
    user_nane_list = list()
    tweet_text_list = list()

    for tweet in api.search(q="adidas", count=20, lang="tr"):
        print (tweet.text)
        tweet_text_list.append(tweet.text)
        user_nane_list.append(tweet.author.screen_name)
        is_bot = False
        screen_name = tweet.author.screen_name
        retweet_status_list.append(tweet.text[0:4] == "RT @")
        time_status_list.append(tweet.created_at)
        total_number_tweets, retweet_percentage, time_of_creation, average_no_per_day = get_user_tweets(api, screen_name)

        if retweet_percentage >= (settings.RT_cutoff * 1.0):
            high_RT_check = 1
        else:
            high_RT_check = 0

        if average_no_per_day >= settings.avg_tweet_cutoff:
            average_tweet_check = 1
        else:
            average_tweet_check = 0

        if high_RT_check or average_tweet_check:
            is_bot = True
            print ("BOT")
        else:
            print ("NOT BOT")

        bot_status_list.append(is_bot)
        return render(request, 'index.html', {'bot_status_list': bot_status_list,
                                              'time_status_list': time_status_list,
                                              'retweet_status_list': retweet_status_list
                                              })