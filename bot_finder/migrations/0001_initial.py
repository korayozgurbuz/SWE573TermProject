# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotChecker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('retweet_status', models.BooleanField()),
                ('average_tweet_status', models.BooleanField()),
                ('bot_status', models.BooleanField()),
                ('username', models.CharField(unique=True, max_length=80, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('follower_count', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
