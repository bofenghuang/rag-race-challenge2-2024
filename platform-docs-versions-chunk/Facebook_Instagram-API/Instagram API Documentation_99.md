platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/webhooks

### Reply to Comment @Mentions

If you subscribe to the `mentions` field, we send your endpoint a webhook notification whenever an Instagram user @mentions an Instagram Business or Creator Account in a comment or caption.

For example, here's a sample comment webhook notification payload sent for an Instagram Business Account (`17841405726653026`):

#### Sample Comment @Mention Payload

\[
  {
    "entry": \[
      {
        "changes": \[
          {
            "field": "mentions",
            "value": {
              "comment\_id": "17894227972186120",
              "media\_id": "17918195224117851"
            }
          }
        \],
        "id": "17841405726653026",
        "time": 1520622968
      }
    \],
    "object": "instagram"
  }
\]