#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:28:31 2020

@author: bernardintheo
"""
import sys

class StreamListener(tweepy.StreamListener):

    #method executed when the connection is established
    def on_status(self, status):
        #print the tweet found by the program 
        print(status._json)
        #open the file test_data_twitter.txt
        with open('test_data_twitter.txt','a') as tf:
            #write the tweet in JSON format in the file 
            tf.write(json.dumps(status._json))
            #separate the different JSON objects with a ,
            tf.write(",")
            return True
    
    #when there is an error with the connection
    def on_error(self, status_code):
        if status_code == 420:
            return False


#Create a streamListener
stream_listener = StreamListener()
#Establish the connection with tweepy 
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
#Filter the tweet with different condition : the tweet must contain "bonjour" and must be located in the area of Annecy
stream.filter(track=["bonjour"],languages=["fr"],locations=[45.904476,6.085753,45.920235,6.158495])

