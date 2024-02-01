platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/overview/about_collections

## Authenticating Requests

It is important to note that the Twitter API is strict about character encoding in OAuth 1.0a and HTTP. Reserved characters in query strings and application/x-www-form-urlencoded POST bodies must first be encoded according to RFC 3986.

OAuth 1.0a handles requests of other content-types slightly differently. A POST body that is not application/x-www-form-urlencoded is not considered as part of the parameters that will be encoded in the OAuth signature base string. Instead your signature base string will contain only any parameters contained on the query string and the oauth\_\* parameters that are typically part of the OAuth signature generation process. [POST collections / entries / curate](https://dev.twitter.com/rest/reference/get/collections/entries/curate) uses application/json POST bodies.