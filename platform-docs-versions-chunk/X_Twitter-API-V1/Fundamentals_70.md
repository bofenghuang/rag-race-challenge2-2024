platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets

## 

* Tweet is promoted
* Tweet has a poll
* Tweet is a non-self-thread reply
* Tweet is a Retweet (note that Quote Tweets are eligible for edit)
* Tweet is nullcast
* Community Tweet
* Superfollow Tweet
* Collaborative Tweet

Example attributes for unedited Tweet  
## 

The JSON below highlights edit metadata that is included for a Tweet posted after the edit Tweet feature was added. This example is for a Tweet that has no edit history. 

Note that the "edit\_tweet\_ids" array has a single ID. 

      `{   "created_at": "Wed Aug 16 18:29:02 +0000 2022",   "id": 1557433858676740098,   "id_str": "1557433858676740098",   "text": "I wonder if I will every use teh edit button",   "ext_edit_control": { 	"initial": { 	  "edit_tweet_ids":["1557433858676740098"],  	  "editable_until_msecs": "1658438151000", 	  "edits_remaining": "5", 	  "is_edit_eligible": true 	} }`