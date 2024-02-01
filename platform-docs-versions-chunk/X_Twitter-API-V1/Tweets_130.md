platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/basic-stream-parameters

### filter\_level

This parameter may be used on all streaming endpoints, unless explicitly noted.

Setting this parameter to one of none, low, or medium will set the minimum value of the filter\_level Tweet attribute required to be included in the stream. The default value is none, which includes all available Tweets.

When displaying a stream of Tweets to end users (dashboards or live feeds at a presentation or conference, for example) it is suggested that you set this value to medium.

### language

This parameter may be used on all streaming endpoints, unless explicitly noted.

Setting this parameter to a comma-separated list of [BCP 47](http://tools.ietf.org/html/bcp47) language identifiers corresponding to any of the languages listed on Twitter’s [advanced search](https://twitter.com/search-advanced) page will only return Tweets that have been detected as being written in the specified languages. For example, connecting with language=en will only stream Tweets detected to be in the English language.