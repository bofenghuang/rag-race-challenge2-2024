platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview


### Single vs. Multi-threaded Requests

Each customer has a defined rate limit for their search endpoint. The default per-minute rate limit for Full-Archive search is 120 requests per minute, for an average of 2 queries per second (QPS). This average QPS means that, in theory, 2 requests can be made of the API every second. Given the pagination feature of the product, if a one-year query has one million Tweets associated with it, spread evenly over the year, over 2,000 requests would be required (assuming a ‘maxResults’ of 500) to receive all the data. Assuming it takes two seconds per response, that is 4,000 seconds (or just over an hour) to pull all of that data serially/sequentially through a single thread (1 request per second using the prior response’s “next” token). Not bad!

Now consider the situation where twelve parallel threads are used to receive data. Assuming an even distribution of the one million Tweets over the one-year period, you could split the requests into twelve parallel threads (multi-threaded) and utilize more of the per-second rate limit for the single “job”. In other words, you could run one thread per-month you are interested in and by doing so, data could be retrieved 12x as fast (or ~6 minutes).

This multi-threaded example applies equally well to the counts endpoint. For example, if you wanted to receive Tweet counts for a two-year period, you could make a single-threaded request and page back through the counts 31 days at a time. Assuming it takes 2 seconds per response, it would take approximately 48 seconds to make the 24 API requests and retrieve the entire set of counts. However, you also have the option to make multiple one-month requests at a time. When making 12 requests per second, the entire set of counts could be retrieved in approximately 2 seconds.