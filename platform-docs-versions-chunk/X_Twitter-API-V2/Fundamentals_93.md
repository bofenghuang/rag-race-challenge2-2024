platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/rate-limits


### Recovering from a rate limit

When these rate limits are exceeded, a 429 'Too many requests' error is returned from the endpoint.  As discussed below, when rate limit errors occur, a best practice is to examine HTTP headers that indicate when the limit resets and pause requests until then.    

When a "too many requests" or rate-limiting error occurs, the frequency of making requests needs to be slowed down. When a rate limit error is hit, the x-rate-limit-reset: HTTP header can be checked to learn when the rate-limiting will reset.   

Another common pattern is based on exponential backoff, where the time between requests starts off small (for example, a few seconds), then doubled before each retry. This is continued until a request is successful, or some reasonable maximum time between requests is reached (for example, a few minutes).    

Ideally, the client-side is self-aware of existing rate limits and can pause requests until the currently exceeded window expires. If you exceed a 15-minute limit, then waiting a minute or two before retrying makes sense.

Note that beyond these limits on the number of requests, the Standard Basic level of access provides up to 500,000 Tweets per month from the recent search and filtered stream endpoints. If you have exceeded the monthly limit on the number of Tweets, then it makes more sense for your app to raise a notification and know its enrollment day of the month and hold off requests until that day.