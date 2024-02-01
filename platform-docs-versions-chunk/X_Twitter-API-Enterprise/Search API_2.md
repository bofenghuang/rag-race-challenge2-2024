platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview


## Overview

Enterprise

_The enterprise APIs are available within our managed access levels only. To use these APIs, you must first set up an account with our enterprise sales team. To learn more see [HERE](https://developer.twitter.com/content/developer-twitter/en/enterprise)._  

_You can view all of the Twitter API search Tweet offerings [HERE](https://developer.twitter.com/en/docs/twitter-api/search-overview)._

There are two enterprise search APIs:  

1. 30-Day Search API provides data from the previous 30 days.
2. Full-Archive Search API provides complete and instant access to the full corpus of Twitter data dating all the way back to the first Tweet in March 2006.

These RESTful APIs supports a single query of up to 2,048 characters per request. Queries are written with the PowerTrack rule syntax - see [Rules and filtering](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/building-a-rule) for more details. Users can specify any time period, to the granularity of a minute. However, responses will be limited to the lesser of your specified maxResults OR 31 days and include a next token to paginate for the next set of results. If time parameters are not specified, the API will return matching data from the 30 most recent days.

The enterprise search APIs provide low-latency, full-fidelity, query-based access to the Tweet archive with minute granularity. Tweet data is served in reverse chronological order, starting with the most recent Tweet that matches your query. Tweets are available from the search API approximately 30 seconds after being published.

These search endpoints provide edited Tweet metadata. All objects for Tweets created since September 29, 2022, include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history is documented by an array of Tweet IDs, starting with the original ID.

These endpoints will always return the most recent edit, along with any edit history. Any Tweet collected after its 30-minute edit window will represent its final version. To learn more about Edit Tweet metadata, check out the [Edit Tweets fundamentals](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/edit-tweets) page.

Requests include a maxResults parameter that specifies the maximum number of Tweets to return per API response. If more Tweets are associated with the query than this maximum amount of results per response, a next token is included in the response. These next tokens are used in subsequent requests to page through the entire set of Tweets associated with the query.

These enterprise search APIs provide a _counts_ endpoint that enables users to request the data volume associated with their query.