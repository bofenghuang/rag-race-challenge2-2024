platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities

## Retweet and Quote Tweet details

From the Twitter API perspective, Retweet and Quote Tweets are special kinds of Tweets that contain the original Tweet as an embedded object. So Retweets and Quote Tweet objects are parents of a child 'original' Tweet (and thus double the size). Retweets have a top-level "retweeted\_status" object, and Quoted Tweets have a "quoted\_status" object. For consistency, these top-level Retweet and Quote Tweet objects also have a text property and associated entities. However, the entities at the top level can differ from the entities provided by the embedded 'original' entities. In case of Retweets, new text is prepended to the original Tweet body. For Quoted Tweets, new text is appended to the Tweet body.

In general, the best practice is to retrieve the text, entities, original author and date from the original Tweet in retweeted\_status whenever this exists. An exception is getting Twitter entities that are part of the additive Quote. See below for more details and tips.