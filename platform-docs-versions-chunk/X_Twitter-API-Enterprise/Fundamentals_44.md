platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities


## Introduction

Entities provide metadata and additional contextual information about content posted on Twitter. The `entities` section provides arrays of common things included in Tweets: hashtags, user mentions, links, stock tickers (symbols), Twitter polls, and attached media. These arrays are convenient for developers when ingesting Tweets, since Twitter has essentially pre-processed, or pre-parsed, the text body. Instead of needing to explicitly search and find these entities in the Tweet body, your parser can go straight to this JSON section and there they are.

Beyond providing parsing conveniences, the `entities` section also provides useful ‘value-add’ metadata. For example, if you are using the [Enhanced URLs enrichment](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls), URL metadata include fully-expanded URLs, as well as associated website titles and descriptions. Another example is when there are user mentions, the entities metadata include the numeric user ID, which are useful when making requests to many Twitter APIs.

Every Tweet JSON payload includes an `entities` section, with the minimum set of `hashtags`, `urls`, `user_mentions`, and `symbols` attributes, even if none of those entities are part of the Tweet message. For example, if you examine the JSON for a Tweet with a body of “Hello World!” and no attached media, the Tweet’s JSON will include the following content with entity arrays containing zero items:

    "entities": {
        "hashtags": [
        ],
        "urls": [
        ],
        "user_mentions": [
        ],
        "symbols": [
        ]
      }

Notes:

* media and polls entities will only appear when that type of content is part of the Tweet.
* if you are working with native media (photos, videos, or GIFs), the [Extended Entities object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities) is the way to go.