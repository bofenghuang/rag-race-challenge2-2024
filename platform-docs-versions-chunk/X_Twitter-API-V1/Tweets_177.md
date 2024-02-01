platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-entries-move

## Success:[¶](#success- "Permalink to this headline")

    {
      "objects": {},
      "response": {
        "errors": []
      }
    }

## Failure:[¶](#failure- "Permalink to this headline")

    {
      "objects": {},
      "response": {
        "errors": [
          {
            "change": {
              "op": "move",
              "tweet_id": "610990849493762050"
            },
            "reason": "not_found"
          }
        ]
      }
    }