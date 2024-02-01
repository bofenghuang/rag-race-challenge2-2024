platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/integrate/build-a-query


###   
Query examples

#### Tracking a natural disaster

The following query matched on original Tweets coming from weather agencies and gauges that discuss Hurricane Harvey, which hit Houston in 2017.

Here is what the query would look like without the HTTP encoding:

has:geo (from:NWSNHC OR from:NHC\_Atlantic OR from:NWSHouston OR from:NWSSanAntonio OR from:USGS\_TexasRain OR from:USGS\_TexasFlood OR from:JeffLindner1) -is:retweet

  
And here is what the query would look like with the HTTP encoding, the query parameter, and the recent Tweet counts URI:

https://api.twitter.com/2/tweets/counts/recent?query=-is%3Aretweet%20has%3Ageo%20(from%3ANWSNHC%20OR%20from%3ANHC\_Atlantic%20OR%20from%3ANWSHouston%20OR%20from%3ANWSSanAntonio%20OR%20from%3AUSGS\_TexasRain%20OR%20from%3AUSGS\_TexasFlood%20OR%20from%3AJeffLindner1)

####   
  
Reviewing the sentiment of a conversation

The next rule could be used to better understand the sentiment of the conversation developing around the hashtag, _#nowplaying_, but scoped to just Tweets published within North America.

Here is what the two different queries, one for positive and one for negative, would look like without the HTTP encoding:

#nowplaying (happy OR exciting OR excited OR favorite OR fav OR amazing OR lovely OR incredible) (place\_country:US OR place\_country:MX OR place\_country:CA) -horrible -worst -sucks -bad -disappointing

#nowplaying (horrible OR worst OR sucks OR bad OR disappointing) (place\_country:US OR place\_country:MX OR place\_country:CA) -happy -exciting -excited -favorite -fav -amazing -lovely -incredible

  
And here is what the query would look like with the HTTP encoding, the query parameter, and the recent Tweet counts URI:

https://api.twitter.com/2/tweets/counts/recent?query=%23nowplaying%20(happy%20OR%20exciting%20OR%20excited%20OR%20favorite%20OR%20fav%20OR%20amazing%20OR%20lovely%20OR%20incredible)%20(place\_country%3AUS%20OR%20place\_country%3AMX%20OR%20place\_country%3ACA)%20-horrible%20-worst%20-sucks%20-bad%20-disappointing

https://api.twitter.com/2/tweets/counts/recent?query=%23nowplaying%20(horrible%20OR%20worst%20OR%20sucks%20OR%20bad%20OR%20disappointing)%20(place\_country%3AUS%20OR%20place\_country%3AMX%20OR%20place\_country%3ACA)%20-happy%20-exciting%20-excited%20-favorite%20-fav%20-amazing%20-lovely%20-incredible

####   
Find Tweets that relate to a specific Tweet annotation  

This rule was built to filter for original Tweets that included an image of a pet that is not a cat, where the language identified in the Tweet is Japanese. To do this, we used the context: operator to take advantage of the [Tweet annotation](https://developer.twitter.com/en/docs/twitter-api/annotations) functionality. We first used the [Tweet lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup) endpoint and the tweet.fields=context\_annotations fields parameter to identify which domain.entity IDs we need to use in our query:

* Tweets that relate to cats return **domain** 66 (Interests and Hobbies category) with entity 852262932607926273 (Cats). 
* Tweets that relate to pets return **domain** 65 (Interests and Hobbies Vertical) with entity 852262932607926273 (Pets). 

  
Here is what the query would look like without the HTTP encoding:

context:65.852262932607926273 -context:66.852262932607926273 -is:retweet has:images lang:ja

  
And here is what the query would look like with the HTTP encoding, the query parameter, and the recent Tweet counts URI:

https://api.twitter.com/2/tweets/counts/recent?query=context%3A65.852262932607926273%20-context%3A66.852262932607926273%20-is%3Aretweet%20has%3Aimages%20lang%3Aja