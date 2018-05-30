import time
import datetime

LENGTH_OF_THE_TWEET = 3


def get_user_tweets(api, screen_name):
    # To overcome with the rate limit
    time.sleep(1)
    user_recent_tweets = api.user_timeline(screen_name=screen_name, count=100, include_rts=True)

    count = 0
    retweets = 0
    total_number_tweets = 0

    for tweet in user_recent_tweets:
        print tweet.author.screen_name
        print tweet.text
        total_number_tweets = tweet.user.statuses_count
        text_of_tweet = tweet.text
        count += 1
        if len(text_of_tweet) > LENGTH_OF_THE_TWEET:
            if text_of_tweet[0:4] == "RT @":
                retweets += 1

    date_of_account_creation = tweet.user.created_at
    account_active_days = datetime.datetime.now() - date_of_account_creation
    active_days_with_date = float(str(account_active_days).split()[0])
    average_number_of_tweet_per_day = (total_number_tweets*1.0) / active_days_with_date
    retweet_percentage = 100.0 * ((retweets * 1.0) / (count*1.00))

    return total_number_tweets, retweet_percentage, date_of_account_creation, average_number_of_tweet_per_day

