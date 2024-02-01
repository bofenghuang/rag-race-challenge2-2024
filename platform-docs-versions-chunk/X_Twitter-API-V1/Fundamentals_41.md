platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/entities

## Entities for Direct Messages

Entities for Direct Messages are very similar to entities for Tweets. However, there are a few differences concerning the media entities.

Unlike media shared in Tweets, media shared in Direct Messages requires authorization to view. This authorization can be presented via an authenticated twitter.com session or by signing a request with the User’s access token using OAuth 1.0A.

Also, in Tweets, media URLs are only in the media entities, but in Direct Messages, media URLs are in both media and URLs entities.