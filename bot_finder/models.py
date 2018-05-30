# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class BotChecker(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    retweet_status = models.BooleanField()
    average_tweet_status = models.BooleanField()
    bot_status = models.BooleanField()
    username = models.CharField(max_length=80, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    follower_count = models.IntegerField(null=True, blank=True)

    def get_retweet_status(self):
        return self.retweet_status

    def get_average_tweet_status(self):
        return self.average_tweet_status

    def get_bot_status(self):
        return self.bot_status

    def get_username(self):
        return self.username

    def get_follower_count(self):
        return self.retweet_status

    def get_is_active(self):
        return self.retweet_status

    def delete(self, using=None, keep_parents=False):
        return super(BotChecker, self).delete(using, keep_parents)

    def __unicode__(self):
        return self.username

