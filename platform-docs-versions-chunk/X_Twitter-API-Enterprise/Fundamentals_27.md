platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet


### Extended Tweets

JSON that describes _Extended Tweets_ was introduced when 280-character Tweets were launched in November 2017. Tweet JSON was extended to encapsulate these longer messages, while not breaking the thousands of apps parsing these fundamental Twitter objects. To provide full backward compatibility, the original 140-character 'text' field, and the entity objects parsed from that, were retained. In the case of Tweets longer than 140 characters, this root-level 'text' field would become truncated and thus incomplete. Since the root-level 'entities' objects contain arrays of key metadata parsed from the 'text' message, such as included hashtags and links, these collections would be incomplete. For example, if a Tweet message was 200 characters long, with a hashtag included at the end, the legacy root-level 'entities.hashtags' array would not include it. 

A new 'extended\_tweet' field was introduced to hold the longer Tweet messages and complete entity metadata. The "extended\_tweet" object provides the "full\_text" field that contains the complete, untruncated Tweet message when longer than 140 characters. The "extended\_tweet" object also contains an "entities" object with complete arrays of hashtags, links, mentions, etc.

Extended Tweets are identified with a root-level "truncated" boolean. When true ("truncated": true), the "extended\_tweet" fields should be parsed instead of the root-level fields.

Note in the JSON example below that the root-level "text" field is truncated and the root-level "entities.hashtags" array is empty even though the Tweet message includes three hashtags. Since this is an Extended Tweet, the "truncated" field is set to true, and the "extended\_tweet" object provides complete "full\_text" and "entities" Tweet metadata.  
  

      `{ 	"created_at": "Thu May 10 17:41:57 +0000 2018", 	"id_str": "994633657141813248", 	"text": "Just another Extended Tweet with more than 140 characters, generated as a documentation example, showing that [\"tru… https://t.co/U7Se4NM7Eu", 	"display_text_range": [0, 140], 	"truncated": true, 	"user": { 		"id_str": "944480690", 		"screen_name": "FloodSocial" 	}, 	"extended_tweet": { 		"full_text": "Just another Extended Tweet with more than 140 characters, generated as a documentation example, showing that [\"truncated\": true] and the presence of an \"extended_tweet\" object with complete text and \"entities\" #documentation #parsingJSON #GeoTagged https://t.co/e9yhQTJSIA", 		"display_text_range": [0, 249], 		"entities": { 			"hashtags": [{ 				"text": "documentation", 				"indices": [211, 225] 			}, { 				"text": "parsingJSON", 				"indices": [226, 238] 			}, { 				"text": "GeoTagged", 				"indices": [239, 249] 			}] 		}  	}, 	"entities": { 		"hashtags": [] 	} }`