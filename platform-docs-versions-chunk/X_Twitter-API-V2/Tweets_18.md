platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/migrate/standard-to-twitter-api-v2


### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * https://api.twitter.com/1.1/statuses/show
    * https://api.twitter.com/1.1/statuses/lookup
* Twitter API v2 endpoint:
    * https://api.twitter.com/2/tweets
    * https://api.twitter.com/2/tweets/:id

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated to a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a Project.   
  

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default, and then have the option to use parameters to identify which fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the Tweet id and text fields by default. To request any additional fields or objects, you will need to use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions) parameters. Any Tweet fields that you request from these endpoints will return in the primary Tweet object. Any expanded user, media, poll, or place objects and fields will return in an includes object within your response. You can then match any expanded objects back to the Tweet object by matching the IDs located in both the Tweet and the expanded object. 

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions). 

We have also put together a [data format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2) which can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.   
 

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including [Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) and [user](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array. 
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed. 
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like. 
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have a non-null values.   
     

We also introduced a new set of fields to the [Tweet object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) including the following:

* A [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field
* Two new [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) fields, including context and entities
* Several new [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) fields 
* A new reply\_setting field, which shows you who can reply to a given Tweet

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

|     |     |
| --- | --- |
| **Standard** | **Twitter API v2** |
| id  | ids |

There are also a set of standard v1.1 Tweet lookup request parameters **not** supported in Twitter API v2:

| Standard | Comment |
| --- | --- |
| tweet\_mode | This parameter enables developers to request a series of different extended fields that had been introduced in the years since statuses/show and statuses/lookup were introduced. It has been replaced with the fields and expansions functionality. |
| trim\_user | This parameter is used to reduce the number of fields that deliver in the user object that comes alongside each Tweet. It has been replaced with the additive fields and expansions functionality.  <br>To request user information alongside your requested Tweet, you will need to use a combination of the author\_id expansion and the user.fields parameter with a set of specified [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user). |
| include\_my\_retweet | This parameter includes the ID of the source Tweet for those specified Tweets that were Retweeted by the authenticating user. |
| include\_entities | This parameter is used to remove the entities node from the Tweet payload. It has been replaced with the additive fields and expansions functionality. |
| include\_ext\_alt\_text | This parameter adds an additional ext\_alt\_text field in the media entity if that media has alt text attached to it. |
| include\_card\_uri | This parameters adds a card\_uri attribute when there is an ads card attached. |
| map | This parameter would return the Tweet ID and nullified fields for unavailable Tweets. <br><br>In v2, we return the Tweet ID and a detailed error message for unavailable Tweets. |