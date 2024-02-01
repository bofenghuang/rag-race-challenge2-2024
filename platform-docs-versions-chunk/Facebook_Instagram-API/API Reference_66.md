platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights

## New Metrics

The metrics listed below are new and will gradually be made available to all developers. These metrics will eventually replace the legacy metrics listed above. If you see this message you are able to use the new metrics described below.

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-media-id}/insights
  ?metric={metric}
  &breakdown={breakdown}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-media-id}` | **Required.** [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) ID. |