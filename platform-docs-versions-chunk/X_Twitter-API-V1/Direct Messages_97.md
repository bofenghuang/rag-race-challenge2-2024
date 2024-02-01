platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/custom-profiles/api-reference/delete-profile

## Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -X DELETE /1.1/custom_profiles/destroy.json?id=100001

## Example Response[¶](#example-response "Permalink to this headline")

Calling this multiple times on a valid id will return a 204 response code.

    HTTP 204 with empty body