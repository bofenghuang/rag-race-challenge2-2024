platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-entries-curate

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/collections/entries/curate.json`

## Example Response[¶](#example-response "Permalink to this headline")

    POST /1.1/collections/entries/curate.json
    Content-Type: application/json
    Content-Length: 226

    {"id":"custom-388061495298244609","changes":[{"op":"add","tweet_id":"390897780949925889"},{"op":"add","tweet_id":"390853164611555329"},{"op":"add","tweet_id":"390892747810295808"},{"op":"add","tweet_id":"390898463090561024"}]} 

## Success:[¶](#success- "Permalink to this headline")

    {"objects":{},"response":{"errors":[]}}