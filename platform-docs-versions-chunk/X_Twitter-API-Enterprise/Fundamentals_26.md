platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet


## Nested Tweet objects

In several cases, a Tweet object will included other nested objects.  If you are working with nested objects, then that JSON payload will contain multiple Tweet objects, and each Tweet object may contain its own objects. The root-level object will contain information on the type of action taken, i.e. whether it is a Retweet or a Quote Tweet, and may also contain an object that describes the 'original' Tweet being shared. Extended Tweets will include a nested extended object that extends beyond 140 characters, which was used to prevent breaking changes when the update was made in 2017. Each nested object dictionary is described below.

#### Retweets

Retweets always contain two Tweet objects. The 'original' Tweet being Retweeted is provided in a "retweeted\_status" object. The root-level object encapsulates the Retweet itself, including a User object for the account taking the Retweet action and the time of the Retweet. Retweeting is an action to share a Tweet with your followers, and no other new content can be added. Also, a (new) location cannot be provided with a Retweet. While the 'original' Tweet may have geo-tagged, the Retweet "geo" and "place" objects will always be null.

Even before the introduction of Extended Tweets, the root-level "entities" object was in some cases truncated and incomplete due to the "RT @username " string being appended to Tweet message being Retweeted.  Note that if a Retweet gets Retweeted, the "retweet\_status" will still point to the original Tweet, meaning the intermediate Retweet is not included. Similar behavior is seen when using twitter.com to 'display' a Retweet. If you copy the unique Tweet ID assigned to the Retweet 'action', the original Tweet is displayed. 

Below is an example structure for a Retweet. Again, when parsing Retweets, it is key to parse the "retweeted\_status" object for complete (original) Tweet message and entity metadata.  
  

      `{ 	"tweet": { 		"text": "RT @author original message", 		"user": { 			"screen_name": "Retweeter" 		}, 		"retweeted_status": { 			"text": "original message", 			"user": { 				"screen_name": "OriginalTweeter" 			}, 			"place": {}, 			"entities": {}, 			"extended_entities": {} 		} 	}, 	"entities": {}, 	"extended_entities": {} }`
    

#### Quote Tweets

Quote Tweets are much like Retweets except that they include a new Tweet message. These new messages can contain their own set of hashtags, links, and other "entities" metadata. Quote Tweets can also include location information shared by the user posting the Quote Tweet, along with media such as GIFs, videos, and photos.

Quote Tweets will contain at least two Tweet objects, and in some cases, three. The Tweet being Quoted, which itself can be a Quoted Tweet, is provided in a "quoted\_status" object. The root-level object encapsulates the Quote Tweet itself, including a User object for the account taking the sharing action and the time of the Quote Tweet.

Note that Quote Tweets can now have photos, GIFs, or videos, added to them using the 'post Tweet' user-interface. When links to externally hosted media are included in the Quote Tweet message, the root-level "entities.urls" will describe those. Media attached to Quote Tweets will appear in the root-level "extended\_entities" metadata.

When Quote Tweets were first launched, a shortened link (t.co URL) was appended to the 'original' Tweet message and provided in the root-level "text" field. In addition, metadata for that t.co URL was included in the root-level 'entities.urls' array. In May 2018, we changed this so that the shortened t.co URL to the quoted Tweet _will not be included_ in the root-level "text" field. Second, the metadata for the quoted Tweet _will not be included_ in the "entities.urls" metadata. Instead, URL metadata for the quoted Tweet will be in a new "quoted\_status\_permalink" object on the root-level (or top-level), so at the same level of the "quoted\_status" object.

Below is an example structure for a Quote Tweet using this original formatting.   
  

      `{ 	"created_at": "Tue Feb 14 19:30:06 +0000 2017", 	"id_str": "831586333415976960", 	"text": "Definitely quotable! https:\/\/t.co\/J1LKrbHpWR", 	"user": { 		"screen_name": "happycamper" 	}, 	"quoted_status_id_str": "831569219296882688", 	"quoted_status": { 		"created_at": "Tue Feb 14 18:22:06 +0000 2017", 		"id_str": "831569219296882688", 		"text": "This is a test of the tweeting system \ud83d\ude0e to update #supportdocs @twitterboulder here: https:\/\/t.co\/NRq9UrSzm0", 		"user": { 			"screen_name": "furiouscamper", 		}, 		"place": { 			"id": "9a974dfc8efb32a0", 		}, 		"entities": { 			"hashtags": [{ 				"text": "supportdocs", 			}], 			"urls": [{ 			}], 			"user_mentions": [{	}], 			"symbols": [] 		}, 	}, 	"is_quote_status": true, 	"entities": {}, 	"matching_rules": [{}] }`
    

      `{ 	"created_at": "Fri Jan 04 18:47:16 +0000 2019", 	"id_str": "1081260794069671936", 	"text": "Quote test https://t.co/CE4m1qs3NJ", 	"user": { 		"screen_name": "furiouscamper" 	}, 	"place": null, 	"quoted_status_id_str": "1079578364904648705", 	"quoted_status": { 		"created_at": "Mon Dec 31 03:21:54 +0000 2018", 		"id_str": "1079578364904648705", 		"text": "AHHHHH", 		"user": { 			"screen_name": "infinite_scream" 		}, 		"place": null, 		"is_quote_status": false, 		"quote_count": 1, 		"reply_count": 0, 		"retweet_count": 3, 		"favorite_count": 6, 		"entities": { 			"hashtags": [], 			"urls": [], 			"user_mentions": [], 			"symbols": [] 		} 	}, 	"quoted_status_permalink": { 		"url": "https://t.co/CE4m1qs3NJ", 		"expanded": "https://twitter.com/infinite_scream/status/1079578364904648705", 		"display": "twitter.com/infinite_screa…" 	}, 	"is_quote_status": true, 	"quote_count": 0, 	"reply_count": 0, 	"retweet_count": 0, 	"favorite_count": 1, 	"entities": {} }`