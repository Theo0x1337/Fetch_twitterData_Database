# Fetch_twitterData_Database
Get some tweet from a keyword and location, and store them into a database

In this project, the objectiv is to retrieve some tweets from a keyword and/or a location, to convert the result to JSON format and add them into a database. 

Tweepy is used, here is the doc of it : http://docs.tweepy.org/en/latest/

You will also need to create a twitter app : https://docs.inboundnow.com/guide/create-twitter-application/

## First step : Retrieve tweet with keyword/location

First we need to retrieve tweet and fetch it in a file in JSON format, this is the role of StreamListener.py file.

Here's an example on how to instanciate a tweepy StreamListener 

```Python
#Create a streamListener
stream_listener = StreamListener()
#Establish the connection with tweepy 
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
#Filter the tweet with different condition : the tweet must contain "bonjour" and must be located in the area of Annecy
stream.filter(track=["bonjour"],languages=["fr"],locations=[45.904476,6.085753,45.920235,6.158495])
```

## Second step : Fetch the data in database

In this step, I used a local database to fetch the data in. You need to instanciate the connection with your database and iterate on your JSON objects that are stocked in the file test_data_twitter.txt. 

Then make a query to insert the data you choosed in your database. See https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object to know which attributes you can access and store into your database.

