platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/guides/tweet-availability

Tweet availability

**Tweets, Retweets, Quote Tweets**: A Twitter user can delete a status at any point in time. Deleted statuses cannot be reversed and are permanently deleted.  When the original Tweet is deleted, all Retweets are also deleted. When the original quoted Tweet is deleted, the Quote Tweet remains.

**Protected accounts**: A Twitter user can protect or unprotect their account at any time. Protected accounts require manual user approval of every person who is allowed to view their account's Tweets. For more information, see [About Public and Protected Tweets](https://help.twitter.com/en/safety-and-security/public-and-protected-tweets).

**Nullcasted Tweets**: A type of Tweet that is created through the Ads API Platform or at ads.twitter.com. Nullcasted Tweets do not appear in the public timeline and are not served to followers, but they do come through the firehose when they are created. In the case of a nullcasted Tweet, the below object will be seen in your enriched native payload. If a Tweet payload includes this object, it was created on the ads platform; however, not all promoted Tweets include this metadata.

      `"scopes": {   "followers": false }`