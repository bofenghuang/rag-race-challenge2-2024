platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/integrate/compliance-best-practices


## Recommendations & Best Practices

* **Build Data Storage Schemas That Store Numeric Tweet ID and User ID**: User messages require action to be taken on all Tweets from that User. Therefore, since all compliance messages are delivered only by numeric ID, it is important to design storage schemas that maintain the relationship between Tweet and User based on numeric IDs. Data consumers will need to monitor compliance events by both Tweet ID and User ID and be able to update the local data store appropriately.
    
* **Build Schemas That Address All Compliance Statuses**: Depending on how compliance activities will be addressed in various applications, it may be required to add other metadata to the data store. For instance, data consumers may decide to add metadata to an existing database to facilitate restricting the display of content in countries affected by a tweet\_withheld message.
    
* **Handling Retweet Deletes**: Retweets are a special kind of Tweet where the original message is nested in an object within the Retweet. In this case, there are two Tweet IDs referenced in a Retweet – the ID for the Retweet, and the ID for the original message (included in the nested object). When an original message is deleted, a Tweet delete message is issued for the original ID. Tweet deletion events typically trigger delete events for all Retweets. It is a best practice to reference the original Tweet ID when storing Retweets, and deleting all referenced Retweets when receiving Tweet delete events.