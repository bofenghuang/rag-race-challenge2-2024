platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/mentions

### Listening for and Replying to Caption @Mentions

You can listen for caption @mentions and reply to any that meet your criteria:

1. Set up an [Instagram webhook](https://developers.facebook.com/docs/instagram-api/guides/webhooks) that's subscribed to the `mentions` field.
2. Set up a script that can parse the Webhooks notifications and identify media IDs.
3. Use the IDs to query the `GET /{ig-user-id}/mentioned_media` endpoint to get more information about each media object.
4. Analyze the returned results to identify media objects with captions that meet your criteria.
5. Use the `POST /{ig-user-id}/mentions` endpoint to [comment on those media objects](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentions#creating).

[](#)

[](#)