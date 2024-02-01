platform: Facebook
topic: Graph-API
subtopic: Url Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Url Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/url

### Examples

To get information about a URL published in a Post or Comment, send a `GET` request to `https://graph.facebook.com` with the `id` parameter set to the URL, any fields about the URL, and an access token requested from the User or Page who published the Post or Comment.

The follow example shows the engagement for the URL, https://www.facebook.com, that was shared by the User represented by the User access token.

_Formatted for readability._

curl -i -X GET \\
 "https://graph.facebook.com/{latest-graph-api-version}/
    ?id=https://www.facebook.com
    &fields=engagement
    &access\_token={user-access-token}"

On success your app receives the following engagement counts for the URL that was shared:

{
  "engagement": {
    "reaction\_count": 514919172,
    "comment\_count": 68687082,
    "share\_count": 975739682,
    "comment\_plugin\_count": 1641
  },
  "id": "https://www.facebook.com"
}

## Creating

You can't perform this operation on this endpoint.

## Updating

Update a URL.