platform: X
topic: Twitter-API-Enterprise
subtopic: Decahose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Decahose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/overview/streaming-likes


## Getting started with Likes

As you prepare to consume likes data, you should know that:

* Likes are delivered via an independent, separate stream
* Likes are historically referred to as “Favorites”. The enriched native format payload maintains this nomenclature
* Streams include only public likes
    * Public means that the liking user, Tweet creator and Tweet are all public on the platform
* Likes are very similar to Retweets and represent a public signal of engagement
* Payload elements include:
    * Original Tweet object
    * Actor object that created the original Tweet
    * Actor object that performed the like action
* Only original content can be liked
    * Retweets cannot be liked. A like of a Retweet is applied to the original Tweet
    * Quoted Tweets _can_ be liked
* Like activities include applicable Gnip Enrichments (where purchased/applied)
* Supported Products / Features
    * Likes streams support Backfill (where purchased/applied)
    * There is no Replay support for likes streams
    * There is no Search or Historical support for likes
    * There are no immediate plans to add likes support to PowerTrack