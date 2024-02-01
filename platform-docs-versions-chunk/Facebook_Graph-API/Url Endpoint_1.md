platform: Facebook
topic: Graph-API
subtopic: Url Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Url Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/url

This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/url)

# URL `/?id={url}`

Represents a URL shared in a Post or in a Comment on a Post.

Refer to our [News Tab Indexing API](https://developers.facebook.com/docs/news-tab-indexing) documentation for additional information.

## Reading

Get information about a URL that was shared in a Post or a Comment on a Post.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](#) | Any access token can be used to make this request. |
| [Features](#) | Not applicable. |
| [Page Tasks](#) | Not applicable. |
| [Permissions](#) | Not applicable. |

### Limitations

* Engagement values returned are not precise but do reflect user engagement with a URL.
* You are limited to 10 GET requests per URL, per app, per hour.