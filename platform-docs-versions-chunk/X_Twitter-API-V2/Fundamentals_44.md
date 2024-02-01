platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/fields


### Example

If you are using the [GET /tweets/search/recent](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent) endpoint, you will primarily receive [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) in that response. Without specifying any fields parameters, you will just receive the default values, `id` and `text`. If you are interested in receiving the public metrics of the Tweets that are returned in the response, you will want to include the `tweet.fields` parameter in your request, with `public_metrics` set as the value. 

This request would look like the following. If you would like to use this request, make sure to replace $BEARER\_TOKEN with your [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) and send it using your command line tool.  

      `curl --request GET \   --url 'https://api.twitter.com/2/tweets/search/recent?query=from%3Atwitterdev&tweet.fields=public_metrics' \   --header 'Authorization: Bearer $BEARER_TOKEN'`
    

  
If you send this request in your terminal, then each of the Tweets that return will include the following fields:

      `{    "data": {        "id": "1263150595717730305",        "public_metrics": {            "retweet_count": 12,            "reply_count": 14,            "like_count": 49,            "quote_count": 7        },        "text": "Do you 👀our new Tweet settings?\n\nWe want to know how and why you’d use a feature like this in the API. Get the details and let us know what you think👇\nhttps://t.co/RtMhhfAcIB https://t.co/8wxeZ9fJER"    } }`
    

If you would like to retrieve a set of fields from a secondary object that is associated with the primary object returned by an endpoint, you will need to include an additional `[expansions](https://developer.twitter.com/en/docs/twitter-api/expansions.html)` parameter. 

For example, if you were using the same GET search/tweets/recent endpoint as earlier, and you wanted to retrieve the author's profile description, you will have to pass the expansions=author\_id and user.fields=description with your request. Here is an example of what this might look like. If you would like to try this request, make sure to replace the $BEARER\_TOKEN with your [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) before pasting it into your command line tool.

      `curl --request GET \   --url 'https://api.twitter.com/2/tweets/search/recent?query=from%3Atwitterdev&tweet.fields=public_metrics&expansions=author_id&user.fields=description' \   --header 'Authorization: Bearer $BEARER_TOKEN'`
    

  
If you specify this in the request, then each of the Tweets that deliver will have the following fields, and the related [user object's](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) default and specified fields will return within includes. The user object can be mapped back to the corresponding Tweet(s) by matching the tweet.author\_id and users.id fields.  
 

      `{   "data": [     {       "id": "1263150595717730305",       "author_id": "2244994945",       "text": "Do you 👀our new Tweet settings?\n\nWe want to know how and why you’d use a feature like this in the API. Get the details and let us know what you think👇\nhttps://t.co/RtMhhfAcIB https://t.co/8wxeZ9fJER",       "public_metrics": {         "retweet_count": 12,         "reply_count": 13,         "like_count": 51,         "quote_count": 7       }     }   ],   "includes": {     "users": [       {         "id": "2244994945",         "username": "TwitterDev",         "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",         "name": "Twitter Dev"       }     ]   } }`
    

Bear in mind that you cannot request specific subfields (for example, `public_metrics.retweet_count`). All subfields will be returned when the top-level field (`public_metrics`) is specified. We have listed all possible fields that you can request in each endpoints' API reference page's parameters table. 

A full list of fields are listed in the [object model](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model.html). To expand and request fields on an object that is not that endpoint’s primary resource, use the [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions.html) parameter with fields.