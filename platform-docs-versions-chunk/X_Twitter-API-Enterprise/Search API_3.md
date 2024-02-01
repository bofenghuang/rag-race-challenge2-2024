platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview


### Request types

The enterprise search APIs support two types of requests:  

#### Search requests (data)

Search requests to the enterprise search APIs allow you to retrieve up to 500 results per response for a given timeframe, with the ability to paginate for additional data. Using the maxResults parameter, you can specify smaller page sizes for display use cases (allowing your user to request more results as needed) or larger page sizes (up to 500) for larger data pulls. The data is delivered in reverse chronological order and compliant at the time of delivery.

#### Counts requests (Tweet count)

Counts requests provide the ability to retrieve historical activity counts, which reflect the number of activities that occurred which match a given query during the requested timeframe. The response will essentially provide you with a histogram of counts, bucketed by day, hour, or minute (the default bucket is _hour_). It's important to note that counts results do not always reflect compliance events (e.g., Tweets deletes) that happen well after (7+ days) a Tweet is published; therefore, it is expected that the counts metric may not always match that of a data request for the same query.  

**Billing note:** each request – _including pagination requests_ – made against the data and counts endpoints are counted as a billed request. Therefore, if there are multiple pages of results for a single query, paging through the X pages of results would equate to X requests for billing.