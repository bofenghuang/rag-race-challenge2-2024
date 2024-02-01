platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets

## Example attributes for an edited Tweet

The JSON below highlights edit metadata that is included for a Tweet posted after the edit Tweet feature was added. This example is for a Tweet that has had a single edit. 

Note that the "edit\_tweet\_ids" array has two IDs, one for the original Tweet and one for the edited update. 

      `{   "created_at": "Wed Aug 16 18:35:42 +0000 2022",   "id": 1557445923210514432,   "id_str": "1557445923210514432",   "text": "I wonder if I will ever use the edit button",  "ext_edit_control": {         "edit": {           "edit_control_initial": {             "edit_tweet_ids": [               "1557433858676740098",               "1557445923210514432"             ],             "editable_until_msecs": "1658438151000",             "edits_remaining": "4",             "is_edit_eligible": true           },           "initial_tweet_id": "1557433858676740098"         }    }  }`