platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/streaming-message-types


### Withheld content notices (status\_withheld, user\_withheld)[](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#withheld-content-notices-status-withheld-user-withheld "Permalink to this headline")

These messages indicate that either the indicated Tweet or indicated user has had their content withheld.

#### status\_withheld[](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#status-withheld "Permalink to this headline")

These events contain an id field indicating the status ID, a user\_id indicating the user, and a collection of withheld\_in\_countries uppercase two-letter country codes. This example illustrates a hypothetical Tweet that has been withheld in Germany and Argentina.

{  
"status\_withheld":{  
"id":1234567890,  
"user\_id":123456,  
"withheld\_in\_countries":\["DE", "AR"\]  
}  
}

#### user\_withheld[](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#user-withheld "Permalink to this headline")

These events contain an id field indicating the user ID and a collection of withheld\_in\_countries uppercase two-letter country codes. This example illustrates a hypothetical user who has been withheld in Germany and Argentina.

{  
"user\_withheld":{  
"id":123456,  
"withheld\_in\_countries":\["DE","AR"\]  
}  
}