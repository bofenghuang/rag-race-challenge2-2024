platform: Facebook
topic: Graph-API
subtopic: Url Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Url Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/url

### Examples

To update information about a URL published in a Post or Comment, send a `POST` request to `https://graph.facebook.com` with the `id` parameter set to the URL, the `scrape` parameter set to `true`, any `fields` about the URL, and an access token requested from the User or Page who published the Post or Comment.

The follow example updates the URL, https://www.facebook.com/my-update, that was shared by the User represented by the User access token.

_Formatted for readability._

curl -i -X POST \\
 "https://graph.facebook.com/{latest-graph-api-version}/
    ?id=https://www.facebook.com/my-update
    &scrape=true
    &access\_token={user-access-token}"

On success your app receives the following engagement counts for the URL that was shared:

{
  "success": true
}