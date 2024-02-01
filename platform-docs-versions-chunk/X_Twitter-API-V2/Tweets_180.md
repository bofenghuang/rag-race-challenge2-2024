platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/quick-start/recent-tweet-counts


### Steps to build a recent Tweet counts request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

  
Once you have the Twitter API v2 collection loaded in Postman, navigate to the Tweet counts > Recent Tweet counts request.

####   
Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request with the [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) authentication methods.

You must add your keys and tokens, specifically the [App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

This variable will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Create a query

Each recent Tweet counts request requires a single [query](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/integrate/build-a-query). For this example, we are going to use a query that matches on Tweets posted by the @XDevelopers account. For this query we use the from: operator and set it to XDevelopers (case insensitive):

`from:XDevelopers`

In Postman, navigate to the "Params" tab and enter this ID, or a string of Tweet IDs separated by a comma, into the "Value" column of the `ids` parameter.

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Description** |
| `query` | from:XDevelopers | Query to submit to the recent Tweet counts endpoint |

#### Step four (optional): Specify the granularity of the request

If you click the ‘Send’ button after step three, you will get the default recent Tweet counts: by hour for the last seven days. If you want to get recent Tweet counts by day, you will have to add the granularity parameter with a value of day.

In Postman, navigate to the "Params" tab and day into the "Value" column of the granularity parameter.

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Description** |
| granularity | day | The granularity for the Tweet counts results. Possible values are day, hour or minute |

  
You should now see the following URL next to the "Send" button:  

      `https://api.twitter.com/2/tweets/counts/recent?query=from%3AXDevelopers&granularity=day`
    

####   
Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

      `{    "data": [        {            "end": "2021-06-16T00:00:00.000Z",            "start": "2021-06-15T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-06-17T00:00:00.000Z",            "start": "2021-06-16T00:00:00.000Z",            "tweet_count": 1        },        {            "end": "2021-06-18T00:00:00.000Z",            "start": "2021-06-17T00:00:00.000Z",            "tweet_count": 2        },        {            "end": "2021-06-19T00:00:00.000Z",            "start": "2021-06-18T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-06-20T00:00:00.000Z",            "start": "2021-06-19T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-06-21T00:00:00.000Z",            "start": "2021-06-20T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-06-22T00:00:00.000Z",            "start": "2021-06-21T00:00:00.000Z",            "tweet_count": 1        },        {            "end": "2021-06-23T00:00:00.000Z",            "start": "2021-06-22T00:00:00.000Z",            "tweet_count": 2        }    ],    "meta": {        "total_tweet_count": 6    } }`