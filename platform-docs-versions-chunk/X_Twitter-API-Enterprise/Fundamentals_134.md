platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets

## 

The JSON below highlights edit metadata that is included for a Tweet posted after the edit Tweet feature was added. This example is for a Tweet that has no edit history. 

Note that the "edit\_tweet\_ids" array has a single ID. 

      `{   "created_at": "Wed Aug 16 18:29:02 +0000 2022",   "id": 1557433858676740098,   "id_str": "1557433858676740098",   "text": "I wonder if I will every use teh edit button",   "edit_history": {     "initial_tweet_id": "1557433858676740098",     "edit_tweet_ids": ["1557433858676740098"]   },   "edit_controls": {     "editable_until_ms": 1660155761384,     "edits_remaining": 5   },   "editable": true }`