platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights

## Updating

This operation is not supported.

## Deleting

This operation is not supported.

## New Metrics

The metrics listed below are new and will gradually be made available to all developers. These metrics will eventually replace the legacy metrics listed above. If you see this message you are able to use the new metrics described below.

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-user-id}/insights
  ?metric={metric}
  &period={period}
  &timeframe={timeframe}
  &metric\_type={metric-type}
  &breakdown={breakdown}
  &since={since}
  &until={until}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-user-id}` | **Required.** [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) ID. |