platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/quick-start/full-archive-search


### Steps to build a full-archive search request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

  
Once you have the Twitter API v2 collection loaded in Postman, navigate to the Search Tweets > Full-archive search request.

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request with the [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) authentication methods.

You must add your keys and tokens, specifically the [App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

This variable will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Create a search query

Each full-archive search query requires a single search query. For this example, we are going to use a query that matches on Tweets posted by the @XDevelopers account. For this query we use the from operator and set it to XDevelopers (case insensitive):

`from:XDevelopers`

In Postman, navigate to the "Params" tab and enter this ID, or a string of Tweet IDs separated by a comma, into the "Value" column of the `ids` parameter.  
 

| Key | Value | Description |
| --- | --- | --- |
| `query` | `from:XDevelopers` | Search query to submit to the full-archive search endpoint |

  
Step four: Identify and specify which fields you would like to retrieve  

If you click the "Send" button after step three, you will receive the default [Tweet object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) fields in your response: `id` ,`text`, and edit\_history\_tweet\_ids. Note that if you receive Tweets from before editing was supported, the edit\_history\_tweet\_ids field will not be provided. No history backfill was performed for this field. 

If you would like to receive additional fields beyond these default fields, you will have to specify those fields in your request with the [field](https://developer.twitter.com/en/docs/twitter-api/fields) and/or [expansion](https://developer.twitter.com/en/docs/twitter-api/expansions) parameters.

For this exercise, we will request a four different sets of fields from different objects:

1. The default Tweet object fields
2. The additional tweet.created\_at field in the primary user objects
3. The associated authors’ [user object’s](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) default fields for the returned Tweets
4. The additional user.description field in the associated user objects  
     

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

| Key | Value | Returned fields |
| --- | --- | --- |
| `tweet.fields` | `created_at` | `tweets.created_at` |
| `expansions` | `author_id` | includes.users.id, includes.users.name, includes.users.username |
| user.fields | description | includes.users.description |

  
You should now see the following URL next to the "Send" button:  

      `https://api.twitter.com/2/tweets/search/all?query=from:XDevelopers&tweet.fields=created_at&expansions=author_id&user.fields=created_at`
    

**Please note**

By default, only 10 most recent Tweets will be returned. If you want more than 10 Tweets per request, you can use the max\_results parameter and set it to a maximum of 500 Tweets per request. Similarly,  by default Tweets from the last 30 days will be returned. If you want to get Tweets that are older than 30 days, you can use the start\_time and end\_time parameters in your API call.

####   
Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive a response similar to the following:

      `{    "data": [        {            "author_id": "2244994945",            "created_at": "2020-06-11T16:05:06.000Z",            "id": "1271111223220809728",            "text": "Tune in tonight and watch as @jessicagarson takes us through running your favorite Python package in R. 🍿\n\nLearn how to use two powerful programming languages for data science together, and see a live example that uses the recent search endpoint from Twitter’s Developer Labs. https://t.co/v178oUZNuj"        },        {            "author_id": "2244994945",            "created_at": "2020-06-10T19:25:24.000Z",            "id": "1270799243071062016",            "text": "As we work towards building the new Twitter API, we’ve extended the deprecation timeline for several Labs v1 endpoints. Learn more 📖 https://t.co/rRWaJYJgKk"        },        {            "author_id": "2244994945",            "created_at": "2020-06-09T18:08:47.000Z",            "id": "1270417572001976322",            "text": "Annotations help you learn more about a Tweet — they can even help you find topics of interest. 🔬\n\nIn this tutorial, @suhemparack shows us how find Tweets related to COVID-19 using annotations + the filtered stream endpoint.\n\nLearn how you can, too. ⤵️\nhttps://t.co/qwVOgw0zSV"        }    ],    "includes": {        "users": [            {                "description": "The voice of Twitter's #DevRel team, and your official source for updates, news, & events about Twitter's API. \n\n#BlackLivesMatter",                "id": "2244994945",                "name": "Twitter Dev",                "username": "TwitterDev"            }        ]    },    "meta": {        "newest_id": "1271111223220809728",        "oldest_id": "1270417572001976322",        "result_count": 3    } }`
    

  
In this example, we used a very simple query. If you would like to see more detailed guides, please visit the resources listed below.