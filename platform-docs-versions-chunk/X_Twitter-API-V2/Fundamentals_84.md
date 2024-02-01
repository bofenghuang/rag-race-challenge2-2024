platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/consistency


## Consistency across the Twitter API v2 endpoints

One of the main aspects of the new v2 version of the Twitter API is consistency across endpoints. This means that objects returned, features, and behaviors of the API are uniform across similar endpoints.

You can expect the following elements to be the same across all endpoints:

* **Path naming** always includes the endpoint [version](https://developer.twitter.com/en/docs/twitter-api/versioning.html), followed by the **resource**. Beyond that, the path can contain an **ID** that relates to the earlier resource, a **selection verb** which helps to determine which data to return (for example, `search` or `sample`), a **delivery verb** which helps to determine how the data will deliver (for example, `stream`), or other resources that have a **relationship** with the primary resource (for example, /user/12/tweets). Finally, you can append a **query parameter** to the end if the endpoint includes any query parameters.  
      
    Here are some examples of how these path and query items could be organized:  
      
    `/version/resource/id?param1=value&param2=value`  
      
    `/version/resource/delivery/selection?param1=value&param2=value`  
      
    Here are some examples of what this might look like in your actual requests:  
      
    `/2/tweets/1067094924124872705?expansions=attachments.media_keys&tweet.fields=author_id`  
      
    `/2/users/2244994945?user.fields=created_at,description`  
      
    `/2/tweets/search/stream`  
      
    `/2/tweets/search/recent?query=snow`  
    

* **JSON Schema**  
    Responses to requests are defined using [JSON Schema](http://json-schema.org/). This means that requests consistently return sets of objects as arrays, with each element having an ID. Requests do not return maps with IDs as keys.  
    
* **Response object and parameters**  
    The default object returned is the same for each endpoint of that object type:
    
    * `id` objects are always strings.
    * Parameters and response fields consistently use American-English spelling.
    * Fields are empty or not returned if there is no value.
    * The `entities` object only contains entities sourced from the Tweet text: this includes `urls`, `hashtags`, `mentions` and `cashtags`.
    * All cards-related information, including the `media_keys` and `poll_ids` fields, are returned in the `attachments` object.

Here is an example response object from the [single Tweet lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets-id.html) endpoint (with the [tweet.fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet.html) parameter set to `author_id,``entities`):

      `{    "data": {        "id": "1278747501642657792",        "text": "It's been a year since Twitter's Developer Labs launched.\n\nAs we build towards the next generation of the #TwitterAPI (coming VERY soon), see what we've learned and changed along the way. https://t.co/WvjuEWCa6G",        "author_id": "2244994945",        "entities": {            "urls": [                {                    "start": 188,                    "end": 211,                    "url": "https://t.co/WvjuEWCa6G",                    "expanded_url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/a-year-with-twitter-developer-labs.html",                    "display_url": "blog.twitter.com/developer/en_u…",                    "images": [                        {                            "url": "https://pbs.twimg.com/news_img/1278747527043362816/7HQRkQeV?format=jpg&name=orig",                            "width": 1600,                            "height": 600                        },                        {                            "url": "https://pbs.twimg.com/news_img/1278747527043362816/7HQRkQeV?format=jpg&name=150x150",                            "width": 150,                            "height": 150                        }                    ],                    "status": 200,                    "title": "A year with Twitter Developer Labs: What we've learned and changed",                    "description": "Labs has been invaluable in helping us understand what works well and what doesn’t, what you liked and what you didn’t.",                    "unwound_url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/a-year-with-twitter-developer-labs.html"                }            ],            "hashtags": [                {                    "start": 106,                    "end": 117,                    "tag": "TwitterAPI"                }            ]        }    } }`
    

* **Authentication**  
    All Twitter API v2 endpoints require authentication. Many of them accept the [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0.html) method. This means that you will have to pass along a Bearer Token with your request to the endpoint to make a successful request.  
      
    For those endpoints that require you to be authorized to create, manipulate, or retrieve data on behalf of another user, you will have to use [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a). This means that you have to provide your [developer App’](https://developer.twitter.com/content/developer-twitter/en/docs/basics/apps/overview)s [API keys and tokens](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/api-key-and-secret), as well as a set of user [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) that you generate for the user that you are making a request on behalf of. You can use the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) to retrieve a set of Access Tokens from a user to make requests on behalf of them. If you are building a request from scratch for and endpoint that requires OAuth 1.0a User Context, you will need to [authorize your request](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/authorizing-a-request), however, we recommend that you use a [tool or library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) that automatically builds this authorization header for you.  
      
    More information on authentication can be found in our documentation on [authentication](https://developer.twitter.com/en/docs/authentication).  
    
* **Fields**

The object returned on each endpoint is condensed. To allow developers more customization in the response they get back from the API, the `[fields](https://developer.twitter.com/en/docs/twitter-api/fields.html)` parameter is used to request the fields desired. Fields will remain consistent across endpoints. The Tweet object will return the same fields across all endpoints the Tweet object is returned. The same set of fields can be queried across similar endpoints. For example, the same Tweet fields can be queried in the [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html) and for the expanded pinned Tweet in the [Users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction.html).

* **Expansions**  
    Where appropriate, [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions.html) are available for all nested id fields (for example, all fields named `*_id`, such as `author_id`). Expansions are also available for all fields that have an id that is not the top-level identifier of the current object. For example, in the [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html), the Tweet is the current object with field `id` as the top-level identifier. The `author_id` or `referenced_tweets.id` fields are available to expand into complete user or Tweet objects by adding these comma-separated values to the `expansions` parameter.  
      
    

Please [report any inconsistencies](https://twitterdevfeedback.uservoice.com/) that you notice, related to these fields.