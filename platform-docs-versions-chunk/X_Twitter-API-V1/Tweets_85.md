platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines

### Optimizing max\_id for environments with 64-bit integers

While one redundant Tweet is not inefficient, it is still possible to optimize max\_id requests to address this problem if your platform is capable of working with 64-bit integers. **Environments where a Tweet ID cannot be represented as an integer with 64 bits of precision (such as JavaScript) should skip this step.** Subtract 1 from the lowest Tweet ID returned from the previous request and use this for the value of max\_id. It does not matter if this adjusted max\_id is a valid Tweet ID, or if it corresponds with a Tweet posted by a different user - the value is just used to decide which Tweets to filter. When adjusted in this manner, it is possible to page through a timeline without receiving redundant Tweets.