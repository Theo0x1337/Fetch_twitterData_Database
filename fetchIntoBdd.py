#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:18:52 2020

@author: bernardintheo
"""

import mysql.connector as mysql


db = mysql.connect(
        host = "127.0.0.1",
        user = "theo",
        passwd = "jAuevImVJWTrPMBz",
        database = "data_twitter",
        charset="utf8mb4",
        port = "8889"
        
)

cursor = db.cursor()



try:
    import json
except ImportError:
    import simplejson as json

# We use the file saved from last step as example
tweets_filename = 'test_data_twitter.txt'
tweets_file = open(tweets_filename, "r")

print(tweets_file)

with open(tweets_filename) as tfn:
        tweet = json.load(tfn)

for i in range(0,len(tweet)):
    # Read in one line of the file, convert it into a json object 
    #tweet = json.loads(line.strip())
    
    cursor.execute('SET NAMES utf8mb4')
    idTweet = tweet[i]["id"] # This is the tweet's id
    content = tweet[i]['text'] # content of the tweet
    langue = tweet[i]['lang']
    userID = tweet[i]['user']['id'] # id of the user who posted the tweet
    name = tweet[i]['user']['name'] # name of the user, e.g. "Wei Xu"
    print(content)
    query = "INSERT INTO tweet (idTweet, langue, name, idUser, content) VALUES ("+str(idTweet)+","+"\""+str(langue)+"\""+","+"\""+str(name)+"\""+","+str(userID)+","+"\""+str(content).replace("\"","").replace("\\","")+"\""+")"
    cursor.execute(query)
    cursor.execute('COMMIT')
cursor.close()
db.close()