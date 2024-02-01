platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/twitter-entities

Entities object

## Twitter entities object

For Activity streams format, the twitter\_entities is the same format and data dictionary shown on the native enriched format [entities object here](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities.html#entitiesobject).

### Example:

      `"twitter_entities": { 	"hashtags": [{ 		"text": "TwitterAPI", 		"indices": [ 			228, 			239 		] 	}], 	"urls": [{ 		"url": "https://t.co/r6z6CI7kEy", 		"expanded_url": "https://twittercommunity.com/t/retiring-labs-v2-recent-search-and-hide-replies/145795", 		"display_url": "twittercommunity.com/t/retiring-lab…", 		"indices": [ 			250, 			273 		] 	}], 	"user_mentions": [], 	"symbols": [] }`