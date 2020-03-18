#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:28:31 2020

@author: bernardintheo
"""
import sys
import tweepy
import json

access_token = '1159875631670280201-XFBPMULm4RxzvybEwSmGC60FDl3R3e'
access_token_secret = 'J48Oixymj0DmQ9xy5UsEugkZr3amJ1WvoN27XakOPtCf5'
consumer_key = '2BAaR711Mz6rTzkBQKgACVXUl'
consumer_secret = 'eCFxVBntV9ebhC9yuqdDy2LNvaRHzEMHbFNcVyiNRRS2DOaVQe'
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
