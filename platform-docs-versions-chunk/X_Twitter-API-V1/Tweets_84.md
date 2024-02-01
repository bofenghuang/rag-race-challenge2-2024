platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines

### The max\_id parameter

The solution to the issue described above is to use a technique for working with streams of data called cursoring. Instead of reading a timeline relative to the top of the list (which changes frequently), an application should read the timeline relative to the IDs of Tweets it has already processed. This is achieved through the use of the max\_id request parameter.

To use max\_id correctly, an application’s first request to a timeline endpoint should only specify a count. When processing this and subsequent responses, keep track of the lowest ID received. This ID should be passed as the value of the max\_id parameter for the next request, which will only return Tweets with IDs lower than or equal to the value of the max\_id parameter. Note that since the max\_id parameter is inclusive, the Tweet with the matching ID will actually be returned again.