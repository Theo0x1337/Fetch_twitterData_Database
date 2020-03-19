#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:28:31 2020

@author: bernardintheo
"""
import sys
import tweepy
import json

access_token = 'YOUR TOKEN HERE'
access_token_secret = 'YOUR TOKEN HERE'
consumer_key = 'YOUR TOKEN HERE'
consumer_secret = 'YOUR TOKEN HERE'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
search_results = api.search(q="coronavirus",geocode="48.6833,6.2,10km", count=500)
    
with open('data_twitter_search.txt','a') as tfs:
    for i in search_results:
        tfs.write(json.dumps(i._json))
        #separate the different JSON objects with a ,
        tfs.write(",")
    
    
with open('data_twitter_search.txt', 'r+') as f:
    content = f.read()
    content = content[:-1]
    f.seek(0, 0)
    f.write('['.rstrip('\r\n') + '\n' + content)
    f.close()

f=open('data_twitter_search.txt','a')
f.seek(0) #get to the first position
f.write("]")
f.close()
