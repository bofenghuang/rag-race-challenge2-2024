platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/mentions

### Listening for and Replying to Comment @Mentions

You can listen for comment @mentions and reply to any that meet your criteria:

1. Set up an [Instagram webhook](https://developers.facebook.com/docs/instagram-api/guides/webhooks) that's subscribed to the `mentions` field.
2. Set up a script that can parse the Webhooks notifications and identify comment IDs.
3. Use the IDs to query the `GET /{ig-user-id}/mentioned_comment` endpoint to get more information about each comment.
4. Analyze the returned results to identify any comments that meet your criteria.
5. Use the `POST /{ig-user-id}/mentions` endpoint to [reply to those comments](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentions#creating).

The reply will appear as a sub-thread comment on the comment in which the Business or Creator Account was mentioned.