platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/streaming-message-types

### Status deletion notices (delete)

These messages indicate that a given Tweet has been deleted. Client code _**must honor these messages**_ by clearing the referenced Tweet from memory and any storage or archive, even in the rare case where a deletion message arrives earlier in the stream than the Tweet it references.

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

### Location deletion notices (scrub\_geo)

These messages indicate that geolocated data must be stripped from a range of Tweets. Clients _**must honor these messages**_ by deleting geocoded data from Tweets which fall before the given status ID and belong to the specified user. These messages may also arrive before a Tweet which falls into the specified range, although this is rare.

{  
"scrub\_geo":{  
"user\_id":14090452,  
"user\_id\_str":"14090452",  
"up\_to\_status\_id":23260136625,  
"up\_to\_status\_id\_str":"23260136625"  
}  
}