platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-lookup


# GET statuses/lookup

Returns fully-hydrated [Tweet objects](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object) for up to 100 Tweets per request, as specified by comma-separated values passed to the `id` parameter.

This method is especially useful to get the details (hydrate) a collection of Tweet IDs.

[GET statuses / show / :id](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-show-id) is used to retrieve a single Tweet object.

There are a few things to note when using this method.

* You must be following a protected user to be able to see their most recent Tweets. If you don't follow a protected user their status will be removed.
* The order of Tweet IDs may not match the order of Tweets in the returned array.
* If a requested Tweet is unknown or deleted, then that Tweet will not be returned in the results list, unless the `map` parameter is set to `true`, in which case it will be returned with a value of `null`.
* If none of your lookup criteria matches valid Tweet IDs an empty array will be returned for `map=false`.
* You are strongly encouraged to use a POST for larger requests.