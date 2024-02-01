platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/guides/direct-message-migration


### Sending Direct Messages

[POST direct\_messages/events/new](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) is a direct replacement for sending Direct Messages. The most significant difference with this endpoint is that all information is now sent as JSON in the POST request body as opposed to individual POST params.

**Example Twurl request**  

twurl -A 'Content-type: application/json' -X POST /1.1/direct\_messages/events/new.json -d '{"event": {"type": "message\_create", "message\_create": {"target": {"recipient\_id": "4534871"}, "message\_data": {"text": "Hello World!"}}}}'

Note in the above request that the content-type is set to application/json as opposed to application/x-www-form-urlencoded. Additionally, if you are constructing the OAuth 1.0a signature, note that the JSON body is not included in the generation of the signature. Most OAuth libraries already account for this. If you are using [twurl](https://github.com/twitter/twurl), ensure you are using at least version 0.9.3.  

#### Summary

* Message is defined in JSON POST body
* Content-type header must be set to application/json
* JSON body is not included in the generation of the OAuth signature.