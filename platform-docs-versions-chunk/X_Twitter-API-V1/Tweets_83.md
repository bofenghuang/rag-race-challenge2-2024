platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines

### The problem with “pages”

In an ideal world, paging would be very easy to implement. Consider the case where a timeline has 10 reverse-chronologically sorted Tweets. An application might attempt to read the entire timeline in two requests by setting a page size of 5 elements and requesting the first page, then the second page. 

The problem with this method is that Twitter timelines are constantly having new Tweets added to their front. Consider the previous example. If two new Tweets are added to the timeline between the first and second calls, the second fetch retrieves two Tweets which were returned in the previous call.

In fact, if 5 or more Tweets were added between calls, subsequent calls would eventually retrieve all the Tweets returned from the first request - making an entire API request completely redundant.