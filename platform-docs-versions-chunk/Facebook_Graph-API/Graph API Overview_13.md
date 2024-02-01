platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview

## Webhooks

You can be notified of changes to nodes or interactions with nodes by subscribing to webhooks. See [Webhooks](https://developers.facebook.com/docs/graph-api/webhooks).

## Versions

The Graph API has multiple versions with quarterly releases. You can specify the version in your calls by adding "v" and the version number to the start of the request path. For example, here's a call to version 4.0:

curl -i -X GET \\
  "https://graph.facebook.com/v4.0/USER-ID/photos
    ?access\_token=ACCESS-TOKEN"

If you do not include a version number we will default to the oldest available version, so it's recommended to include the version number in your requests.

You can read more about versions in our [Versioning guide](https://developers.facebook.com/docs/graph-api/guides/versioning) and learn about all available versions in the [Graph API Changelog](https://developers.facebook.com/docs/graph-api/changelog).