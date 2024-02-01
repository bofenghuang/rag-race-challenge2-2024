platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-entries-remove

## Example Response[¶](#example-response "Permalink to this headline")

Success:

    {
      "response": {
        "errors": [
    
        ]
      },
      "objects": {
      }
    }

Failure:

    {
      "response": {
        "errors": [
          {
            "change": {
              "tweet_id": "390890231215292416",
              "op": "remove"
            },
            "reason": "not_found"
          }
        ]
      },
      "objects": {
      }
    }