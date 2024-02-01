platform: X
topic: Twitter-API-V2
subtopic: Trends
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Trends.md
url: https://developer.twitter.com/en/docs/twitter-api/trends/introduction


### Getting started

To use this endpoint, you need a [bearer token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) from the [developer portal](https://developer.twitter.com/en/portal/dashboard). Once you have the bearer token,  you can call the usage API as shown below:

      `curl 'https://api.twitter.com/2/trends/by/woeid/26062' --header 'Authorization: Bearer XXXXX'` 
    

If the request is successful, you should see the JSON response as shown below:

      `{     "data": [         {             "trend_name": "Europe",             "tweet_count": 232408         },         {             "trend_name": "Isak",             "tweet_count": 2956         },         {             "trend_name": "RNLI",             "tweet_count": 2484         },         {             "trend_name": "Toon",             "tweet_count": 11447         },         {             "trend_name": "St James",             "tweet_count": 5565         },         {             "trend_name": "Manning",             "tweet_count": 10077         },         {             "trend_name": "Copenhagen",             "tweet_count": 35272         },         {             "trend_name": "Coventry",             "tweet_count": 3662     ] }`
    

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)