platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/activity


### Nested Tweet activity obejcts

In several cases, a Tweet object will included other nested Tweets.  If you are working with nested objects, then that JSON payload will contain multiple objects, and each Tweet object may contain its own objects. The root-level object will contain information on the type of action taken, i.e. whether it is a Retweet or a Quote Tweet, and may also contain an object that describes the 'original' Tweet being shared. Extended Tweets will include a nested extended object that extends beyond 140 characters, which was used to prevent breaking changes when the update was made in 2017. Each nested object dictionary is described below.

#### Retweets

Activity streams format of Retweets includes a nested object with the type "activity" and the verb "note" to represent the original Tweet being Retweeted.

      `{ 	"id": "tag:search.twitter.com,2005:222222222222", 	"objectType": "activity", 	"verb": "share", 	"body": "RT @TheOriginalTweeter: Coffee and art ☕️", 	"actor": { 		"displayName": "TheRetweeter" 	}, 	"object": { 		"id": "tag:search.twitter.com,2005:11111111111", 		"objectType": "activity", 		"verb": "post", 		"body": "Coffee and art ☕️", 		"actor": { 			"displayName": "TheOriginalTweeter" 		}, 		"object": { 			"objectType": "note", 			"id": "object:search.twitter.com,2005:11111111111", 			"summary": "Coffee and art ☕️", 			"link": "http://twitter.com/originaltweeter/statuses/11111111111", 			"postedTime": "2020-12-04T11:00:01.000Z" 		}, 		"twitter_entities": {}, 		"twitter_extended_entities": {} 	}, 	"twitter_entities": {}, 	"twitter_extended_entities": {}, 	"gnip": {} }`
    

#### Twitter quoted status

Activity streams format embeded quote Tweets

      `{ 	"id": "tag:search.twitter.com,2005:222222222222", 	"objectType": "activity", 	"verb": "post", 	"body": "Quoting a Tweet: https://t.co/mxiFJ59FlB", 	"actor": { 		"displayName": "TheQuoter2" 	}, 	"object": { 		"objectType": "note", 		"id": "object:search.twitter.com,2005:111111111", 		"summary": "https://t.co/mxiFJ59FlB" 	}, 	"twitter_entities": {}, 	"twitter_extended_entities": {}, 	"gnip": {}, 	"twitter_quoted_status": { 		"id": "tag:search.twitter.com,2005:111111111", 		"objectType": "activity", 		"verb": "post", 		"body": "console.log('Happy birthday, JavaScript!');", 		"actor": { 			"displayName": "TheOriginalTweeter" 		}, 		"object": { 			"objectType": "note", 			"id": "object:search.twitter.com,2005:111111111" 		}, 		"twitter_entities": {} 	} }`
    

Retweeted Quote Tweet:

      `    {     	"id": "tag:search.twitter.com,2005:1293612267087384577",     	"objectType": "activity",     	"verb": "share",     	"postedTime": "2020-08-12T18:16:13.000Z",     	"generator": {},     	"provider": {},     	"link": "http://twitter.com/TwitterDev/statuses/1293612267087384577",     	"body": "RT @compston: So excited to make this first set of endpoints available - many more to come before we're done. The @TwitterDev #DevRel team…",     	"actor": {},     	"object": {},     	"favoritesCount": 0,     	"twitter_entities": {},     	"twitter_lang": "en",     	"retweetCount": 13,     	"gnip": {},     	"twitter_filter_level": "low",     	"twitter_quoted_status": {}     }`