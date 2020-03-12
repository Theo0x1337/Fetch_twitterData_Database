#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:28:31 2020

@author: bernardintheo
"""
import sys

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status._json)
        with open('test_data_twitter.txt','a') as tf:
            tf.write(json.dumps(status._json))
            tf.write(",")
            return True
        
    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["bonjour"],languages=["fr"],locations=[45.904476,6.085753,45.920235,6.158495])

