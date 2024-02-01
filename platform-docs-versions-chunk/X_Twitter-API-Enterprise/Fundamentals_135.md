platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets

## Example attributes for an edited Tweet

The JSON below highlights edit metadata that is included for a Tweet posted after the edit Tweet feature was added. This example is for a Tweet that has had a single edit. 

Note that the "edit\_tweet\_ids" array has two IDs, one for the original Tweet and one for the edited update. 

      `{   "created_at": "Wed Aug 16 18:35:42 +0000 2022",   "id": 1557445923210514432,   "id_str": "1557445923210514432",   "text": "I wonder if I will ever use the edit button",   "edit_history": {     "initial_tweet_id": "1557433858676740098",     "edit_tweet_ids": ["1557433858676740098", "1557445923210514432"]   },   "edit_controls": {     "editable_until_ms": 1660155761384,     "edits_remaining": 4   },   "editable": true }`