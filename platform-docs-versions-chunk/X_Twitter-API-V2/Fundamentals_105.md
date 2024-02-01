platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/edit-tweets


### Getting Tweet objects for all Tweets in a Tweet’s edit history

The examples above provide an array of Tweet IDs in a Tweet’s edit history. If you want the actual Tweet object for each of these Tweet IDs, you can use the expansion parameter and set it to edit\_history\_tweet\_ids. The Tweet objects that make up the edit history will be provided in the "includes" object. 

**Request:**

      `curl --location --request GET 'https://api.twitter.com/2/users/:id/tweets?tweet.fields=edit_control&expansions=edit_history_tweet_ids' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**Sample Response:**

      `{   "data": [     {       "id": "1514991667853602823",       "text": "we have an edit button",       "edit_history_tweet_ids": ["1514991667853602822", "1514991667853602823"],       "edit_controls": {         "is_edit_eligible": true,         "editable_until": "2022-04-21 09:35:20.311",         "edits_remaining": 4       }     }   ],   "includes": {     "tweets": [       {         "id": "1514991667853602822",         "text": "we need an eidt button",         "edit_history_tweet_ids": [           "1514991667853602822",           "1514991667853602823"         ],         "edit_controls": {           "is_edit_eligible": true,           "editable_until": "2022-04-21 09:35:20.311",           "edits_remaining": 4         }       }     ]   } }`