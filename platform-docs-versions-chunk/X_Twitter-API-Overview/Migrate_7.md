platform: X
topic: Twitter-API-Overview
subtopic: Migrate
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Overview/Migrate.md
url: https://developer.twitter.com/en/docs/twitter-api/migrate/whats-new


### Flexibility to choose which objects and fields you receive  

When making a request to a GET endpoint, you will receive the primary data object that relates to that endpoint, which will include a set of default fields. For example, the Tweet object delivers the id and text fields as its default. 

If you would like to retrieve additional fields with your request, you will have to use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) parameters. The expansions parameter enables you to retrieve related data objects such as a user's pinned Tweet or a media object, while the field operators enable you to request specific fields within returned objects beyond the defaults. 

Here is a full list of expansions that you can request with the different X API v2 endpoints:  
 

|     |     |
| --- | --- |
| **Object / Resource** | **Available expansions** |
| **Tweets** | author\_id  <br>edit\_history\_tweet\_ids  <br>entities.mentions.username  <br>in\_reply\_to\_user\_id  <br>referenced\_tweets.id  <br>referenced\_tweets.id.author\_id  <br>attachments.poll\_ids  <br>attachments.media\_keys  <br>geo.place\_id |
| **Users** | pinned\_tweet\_id |
| **Spaces** | invited\_user\_ids  <br>speaker\_ids  <br>creator\_id  <br>host\_ids  <br>topic\_ids |

  
Learn more about [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions), and check out our [full list of data objects and fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary) in the X API v2 data dictionary.