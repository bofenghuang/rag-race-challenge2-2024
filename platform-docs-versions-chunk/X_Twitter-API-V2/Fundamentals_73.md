platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/conversation-id


###   
Using conversation\_id as a filter operator

The conversation\_id can be used as a search query parameter when using either recent search or as an operator within a rule for filtered stream.  Using the operator on its own will result in the entire conversation thread of Tweets being returned in either real time through [filtered stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction.html), or paginated in reverse chronological order from [search Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction.html). You can also receive a count of the Tweets in a conversation using this operator with [Tweet counts](https://developer.twitter.com/en/docs/twitter-api/tweets/counts).

Additional operators can be added to the query/rule, in conjunction with the conversation\_id operator, however these will apply only to the Tweets that are part of that conversation.  Only one conversation\_id can be specified at a time without an OR clause within the query/rule.

Reconstructing the conversation can be done by ordering the Tweets with a matching conversation\_id by timestamp, and taking note of which Tweets are directly in reply to other Tweets in the conversation thread. This can be accomplished by also requesting the in\_reply\_to\_user\_id field and referenced\_tweets.id and in\_reply\_to\_user\_id expansions.

  
Request to query by conversation\_id  

      `curl --request GET \   --url 'https://api.twitter.com/2/tweets/search/recent?query=conversation_id:1279940000004973111&tweet.fields=in_reply_to_user_id,author_id,created_at,conversation_id' \   --header 'Authorization: Bearer $ACCESS_TOKEN'` 
    

####   
Response

_**Note**: Results for search Tweets are in reverse chronological order._ 

      `{ 	"data": [{ 			"id": "1280169000000704333", 			"text": "@attributeisland @iterationjoe What beautiful creatures! Happy #seaturtleweek", 			"conversation_id": "1279940000004973111", 			"public_metrics": { 				"retweet_count": 0, 				"reply_count": 0, 				"like_count": 7, 				"quote_count": 0 			} 		}, 		{ 			"id": "1280166000000519222", 			"text": "@attributeisland \"One touch of nature makes the whole world kin.\" -John Muir", 			"conversation_id": "1279940000004973111", 			"public_metrics": { 				"retweet_count": 0, 				"reply_count": 1, 				"like_count": 1, 				"quote_count": 0 			} 		}, 		{ 			"id": "1280166000000519221", 			"text": "@attributeisland I love turtles!", 			"conversation_id": "1279940000004973111", 			"public_metrics": { 				"retweet_count": 1, 				"reply_count": 0, 				"like_count": 4, 				"quote_count": 0 			} 		}, 		{ 			"id": "1280166000000519220", 			"text": "@attributeisland Turtlemoji🐢", 			"conversation_id": "1279940000004973111", 			"public_metrics": { 				"retweet_count": 0, 				"reply_count": 0, 				"like_count": 1, 				"quote_count": 0 			} 		}, 		{ 			"id": "1279940000004973111", 			"text": "Sea turtles are roaming in our waters!", 			"conversation_id": "1279940000004973111", 			"public_metrics": { 				"retweet_count": 67, 				"reply_count": 11, 				"like_count": 396, 				"quote_count": 2 			} 		} 	], 	"meta": { 		"newest_id": "1280169000000704333", 		"oldest_id": "1279940000004973111", 		"result_count": 5 	} }`