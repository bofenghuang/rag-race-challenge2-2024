platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/edit-tweets

### Getting additional data with edit\_controls

If you want additional edited Tweet metadata such as whether a Tweet was eligible to be edited when it was created and how much time is remaining for a Tweet to be editable, you can request this information using the tweet.fields parameter and setting it to edit\_control.

**Request:**

      `curl --request GET 'https://api.twitter.com/2/users/:id/tweets?tweet.fields=edit_control' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**Sample Response:**

      `{   "data": [     {       "id": "1514991667853602823",       "text": "we have an edit button",       "edit_history_tweet_ids": ["1514991667853602822", "1514991667853602823"],       "edit_controls": {         "is_edit_eligible": true,         "editable_until": "2022-04-21 09:35:20.311",         "edits_remaining": 4       }     }   ] }`