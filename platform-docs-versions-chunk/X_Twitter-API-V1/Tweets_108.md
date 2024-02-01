platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/overview


### Compliance Messages

#### Status deletion notices (delete)

These messages indicate that a given Tweet has been deleted. Client code must honor these messages by clearing the referenced Tweet from memory and any storage or archive, even in the rare case where a deletion message arrives earlier in the stream that the Tweet it references.

{  
"delete":{  
"status":{  
"id":1234,  
"id\_str":"1234",  
"user\_id":3,  
"user\_id\_str":"3"  
}  
}  
}

#### Location deletion notices (scrub\_geo)

These messages indicate that geolocated data must be stripped from a range of Tweets. Clients must honor these messages by deleting geocoded data from Tweets which fall before the given status ID and belong to the specified user. These messages may also arrive before a Tweet which falls into the specified range, although this is rare.

{  
"scrub\_geo":{  
"user\_id":14090452,  
"user\_id\_str":"14090452",  
"up\_to\_status\_id":23260136625,  
"up\_to\_status\_id\_str":"23260136625"  
}  
}

#### Withheld content notices (status\_withheld, user\_withheld)

These messages indicate that either the indicated Tweet or indicated user has had their content withheld.

#### status\_withheld[¶](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#status-withheld "Permalink to this headline")

These events contain an id field indicating the status ID, a user\_id indicating the user, and a collection of withheld\_in\_countries uppercase two-letter country codes. This example illustrates a hypothetical Tweet that has been withheld in Germany and Argentina.

{  
"status\_withheld":{  
"id":1234567890,  
"user\_id":123456,  
"withheld\_in\_countries":\["DE", "AR"\]  
}  
}

#### user\_withheld[¶](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#user-withheld "Permalink to this headline")

These events contain an id field indicating the user ID and a collection of withheld\_in\_countries uppercase two-letter country codes. This example illustrates a hypothetical user who has been withheld in Germany and Argentina.

{  
"user\_withheld":{  
"id":123456,  
"withheld\_in\_countries":\["DE","AR"\]  
}  
}

#### User update

Everytime a user updates their profile we broadcast a user\_update event to indicate that an update has been made to the user profile. The source and target objects are identical in content.

{  
"created\_at": "Tue Aug 06 02:23:21 +0000 2013",  
"source": {  
...  
},  
"target": {  
...  
},  
"event": "user\_update"  
}