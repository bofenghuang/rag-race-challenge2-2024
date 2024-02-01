platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/overview


## Introduction

Enterprise

Tweets are the basic atomic building block of all things Twitter. All Twitter APIs that return Tweets provide that data encoded using JavaScript Object Notation (JSON). JSON is based on key-value pairs, with named attributes and associated values. Tweet objects retrieved from the API include a Twitter User's "status update" but Retweets, replies, and quote Tweets are all also Tweet objects.  If a Tweet is related to another Tweet, as a Retweet, reply or quote Tweet, each will be identified or embedded into the Tweet object.  Even the simplest Tweet in the native Twitter data format, will have nested JSON objects to represent the other attributes of a Tweet, such as the author, mentioned users, tagged place location, hashtags, cashtag symbols, media or URL links.  When working with Twitter data, this is an important concept to understand. The format of the Tweet data you will receive from the Twitter API depends on the type of Tweet received, the Twitter API you are using, and the format settings.

Enterprise endpoints that return Tweet objects have been updated to provide the metadata needed to understand the Tweet's edit history. Learn more about these metadata on the ["Edit Tweets" fundamentals](https://developer.twitter.com/en/docs/twitter-api/edit-tweets) page.

> What did the developer write in their Valentine’s card?  
>   
> while(true) {  
> I = Love(You);  
> }
> 
> — Twitter Dev (@TwitterDev) [February 14, 2020](https://twitter.com/TwitterDev/status/1228393702244134912?ref_src=twsrc%5Etfw)

In native Twitter format, the JSON payload will include of ‘root-level’ attributes, and nested JSON objects (which are represented here with the `{}` notation):

      `{ 	"created_at": "Fri Feb 14 19:00:55 +0000 2020", 	"id_str": "1228393702244134912", 	"text": "What did the developer write in their Valentine’s card?\n  \nwhile(true) {\n    I = Love(You);  \n}", 	"entities": { 		"hashtags": [], 		"symbols": [], 		"user_mentions": [], 		"urls": [] 	}, 	"user": { 		"entities": { 			"url": {} 		} 	}, 	"place": {} }`