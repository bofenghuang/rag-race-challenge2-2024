platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/message-attachments/guides/attaching-media

Attaching media

## Attaching media

[POST direct\_messages/events/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event.html) supports media attachments of type image, GIF and video. The process is similar to attaching media to Tweets:

1. Chunk upload the image, GIF or video.
2. Send Direct Message with media attachment.

It is possible to attach the same media asset to multiple Direct Messages. However, you must get users’ express consent to set media as “shared,” and must provide them with clear notice that “shared” media will be viewable by anyone with the media’s URL. See the documented process below for how to set media to "shared."

**Note:** Media for use with Direct Messages should be uploaded using the asynchronous chunked upload process described on this page.