platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/quick-start/full-archive-tweet-counts


### Steps to build a full-archive Tweet counts request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

  
Once you have the Twitter API v2 collection loaded in Postman, navigate to the Tweet counts > Full-archive Tweet counts request.

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request with the [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) authentication methods.

You must add your keys and tokens, specifically the [App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

This variable will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Create a query

Each full-archive Tweet counts request requires a single [query](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/integrate/build-a-query). For this example, we are going to use a query that matches on Tweets posted by the @XDevelopers account. For this query we use the from operator and set it to XDevelopers (case insensitive):

`from:XDevelopers`

In Postman, navigate to the "Params" tab and enter this ID, or a string of Tweet IDs separated by a comma, into the "Value" column of the `ids` parameter.  
 

| Key | Value | Description |
| --- | --- | --- |
| `query` | `from:XDevelopers` | Query to submit to the full-archive Tweet counts endpoint |

  
Step four (optional): Specify the granularity and time period  

If you click the ‘Send’ button after step three, you will get the default full-archive Tweet counts: by hour for the last 30 days. If you want to get full-archive Tweet counts by day, you will have to add the granularity parameter with a value of day. If you want Tweet counts for more than 30 days ago, you will have to specify the start\_time and end\_time parameters with the desired values. 

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Description** |
| granularity | day | The granularity for the Tweet counts results. Possible values are day, hour or minute |
| start\_time | 2021-05-01T00:00:00Z | The oldest UTC timestamp from which the Tweets will be provided |
| end\_time | 2021-06-01T00:00:00Z | The oldest UTC timestamp from which the Tweets will be provided. |

  
You should now see the following URL next to the "Send" button:  

      `https://api.twitter.com/2/tweets/counts/all?query=from%3AXDevelopers&start_time=2021-05-01T00:00:00Z&end_time=2021-06-01T00:00:00Z&granularity=day`
    

####   
Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive a response similar to the following:

      `{    "data": [        {            "end": "2021-05-02T00:00:00.000Z",            "start": "2021-05-01T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-03T00:00:00.000Z",            "start": "2021-05-02T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-04T00:00:00.000Z",            "start": "2021-05-03T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-05T00:00:00.000Z",            "start": "2021-05-04T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-06T00:00:00.000Z",            "start": "2021-05-05T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-07T00:00:00.000Z",            "start": "2021-05-06T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-08T00:00:00.000Z",            "start": "2021-05-07T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-09T00:00:00.000Z",            "start": "2021-05-08T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-10T00:00:00.000Z",            "start": "2021-05-09T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-11T00:00:00.000Z",            "start": "2021-05-10T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-12T00:00:00.000Z",            "start": "2021-05-11T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-13T00:00:00.000Z",            "start": "2021-05-12T00:00:00.000Z",            "tweet_count": 6        },        {            "end": "2021-05-14T00:00:00.000Z",            "start": "2021-05-13T00:00:00.000Z",            "tweet_count": 1        },        {            "end": "2021-05-15T00:00:00.000Z",            "start": "2021-05-14T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-16T00:00:00.000Z",            "start": "2021-05-15T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-17T00:00:00.000Z",            "start": "2021-05-16T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-18T00:00:00.000Z",            "start": "2021-05-17T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-19T00:00:00.000Z",            "start": "2021-05-18T00:00:00.000Z",            "tweet_count": 1        },        {            "end": "2021-05-20T00:00:00.000Z",            "start": "2021-05-19T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-21T00:00:00.000Z",            "start": "2021-05-20T00:00:00.000Z",            "tweet_count": 8        },        {            "end": "2021-05-22T00:00:00.000Z",            "start": "2021-05-21T00:00:00.000Z",            "tweet_count": 1        },        {            "end": "2021-05-23T00:00:00.000Z",            "start": "2021-05-22T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-24T00:00:00.000Z",            "start": "2021-05-23T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-25T00:00:00.000Z",            "start": "2021-05-24T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-26T00:00:00.000Z",            "start": "2021-05-25T00:00:00.000Z",            "tweet_count": 1        },        {            "end": "2021-05-27T00:00:00.000Z",            "start": "2021-05-26T00:00:00.000Z",            "tweet_count": 1        },        {            "end": "2021-05-28T00:00:00.000Z",            "start": "2021-05-27T00:00:00.000Z",            "tweet_count": 1        },        {            "end": "2021-05-29T00:00:00.000Z",            "start": "2021-05-28T00:00:00.000Z",            "tweet_count": 2        },        {            "end": "2021-05-30T00:00:00.000Z",            "start": "2021-05-29T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-05-31T00:00:00.000Z",            "start": "2021-05-30T00:00:00.000Z",            "tweet_count": 0        },        {            "end": "2021-06-01T00:00:00.000Z",            "start": "2021-05-31T00:00:00.000Z",            "tweet_count": 0        }    ],    "meta": {        "total_tweet_count": 22    } }`
    

####   
Step six: Paginate through your results

If the ‘meta’ object in your response also contains next\_token, you can pass its value to the next\_token query parameter.

| Key | Value | Description |
| --- | --- | --- |
| next\_token | You will add the next\_token that you pull from your previous request's meta object and add it here. | If your latest request does not deliver the remainder of the results, you will receive a next\_token in the meta object. You will pull the value of that field and add it as the value of the next\_token parameter in your next request, holding all other request parameters constant. |

Once you have the right value for next\_token set, hit the "Send" button and you will receive the next page of results.