platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/introduction


### User Tweet timeline

The user Tweet timeline endpoint provides access to Tweets published by a specific Twitter account.  Retrieving a user's Tweets allows you to build experiences such as showcasing a timeline in a user interface, analyzing a user's Tweets to better understand their content, or creating engagement workflows with their Tweets programmatically. This endpoint gives you access to a single Twitter account's most recent Tweets, Retweets, replies, and Quote Tweets, similar to what may be seen on a user's profile timeline.

Here is a user timeline for @XDevelopers:

[Tweets by XDevelopers](https://twitter.com/XDevelopers?ref_src=twsrc%5Etfw)

The user Tweet timeline endpoint is a REST endpoint that receives a single path parameter to indicate the desired user (by user ID). The endpoint can return the 3,200 most recent Tweets, Retweets, replies, and Quote Tweets posted by the user.

Tweets are delivered in reverse-chronological order, starting with the most recent. Results are [paginated](https://developer.twitter.com/en/docs/twitter-api/pagination.html) up to 100 Tweets per page. Pagination tokens are provided for paging through large sets of Tweets. The Tweet IDs of the newest and the oldest Tweets included in the given page are also provided as metadata, which can also be used for polling timelines for recent Tweets. The user Tweet timeline also supports the ability to specify start\_time and end\_time parameters to receive Tweets that were created within a certain window of time. 

The user Tweet timeline endpoint supports [fields](https://developer.twitter.com/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) parameters, and returns the [new JSON data format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

To successfully make a request to this endpoint, you will need to authorize your request with the [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), or [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) authentication methods. You must use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE when requesting nonpublic metrics, promoted metrics or a protected user's timeline. 

The user Tweet timeline endpoint is designed to support two common usage patterns: 

* "Get a user’s historical Tweets": Requests made to user Tweet timeline in order to receive Tweets authored by the user of interest in chronological order over a specific recent timeframe. The timeframe can be set using the start\_time and end\_time and paginating through the full results.  In some cases, a user’s entire history of Tweets can be retrieved if the user has only authored up to 3,200 Tweets in their account. Tweets included will depend on the public availability and the authentication that is used for the requests.
    
* "Polling for new Tweets": Requests made to user Tweet timeline on a continual basis, to retrieve new Tweets authored by a specific user. The last Tweet ID received can be set as a parameter for any new requests since the last Tweet.