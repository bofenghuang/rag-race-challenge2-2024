platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks

### Optional signature header validation

When receiving a POST request from Twitter, sending a GET request to create a webhook, or sending a GET request to perform a manual CRC, a hash signature will be passed in the headers as x-twitter-webhooks-signature. This signature can be used to validate the source of the data is Twitter. The POST hash signature starts with sha256= indicating the use of HMAC SHA-256 to encrypt your Twitter App Consumer Secret and payload. The GET hash is calculated from the query parameter string crc\_token=$token&nonce=$nonce. 

**Steps to validate a request**

1. Create a hash using your consumer secret and incoming payload body.
2. Compare created hash with the base64 encoded x-twitter-webhooks-signature value. Use a method like [compare\_digest](https://docs.python.org/2/library/hmac.html) to reduce the vulnerability to timing attacks.