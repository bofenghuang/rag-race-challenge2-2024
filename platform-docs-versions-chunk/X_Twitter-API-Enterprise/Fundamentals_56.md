platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities


### Retweets  

An important detail with Retweets is that no additional Twitter _entities_ can be added to the Tweet. Users can not add hashtags, URLs or other details when they Retweet. However, the Retweet (top-level) text attribute is composed of the original Tweet text with “RT @username: ” prepended.  

In some cases, especially with accounts with long user names, the combination of these new characters and the original Tweet body can easily exceed the original Tweet text length limit of 140 characters. In order to preserve support for 140 character based display and storage, the top-level body truncates the end of the Tweet body and adds an ellipsis (“…”). Consequently, some top-level entities positioned at the end of the original Tweet might be incorrect or missing, for instance in the case of a truncated hashtag or URL entry.

This Tweet,  https://twitter.com/FloodSocial/status/907974220298125312, has the following Tweet text:

               Just another test Tweet that needs to be exactly 140 characters with trailing URL and hashtag [http://wapo.st/2w8iwPQ](https://t.co/R5iMzxWelp "http://wapo.st/2w8iwPQ")  [#Testing](https://twitter.com/hashtag/Testing?src=hash)  

In the above example, both the URL and hashtag were affected. Since the hashtag was completely truncated and the URL partially truncated, these are missing from the the top-level entities. You will also notice the additional user\_mentions top-level entity coming from the “RT @floodsocial: ” prefix on the text field.

However, the Tweet text and entities in retweeted\_status perfectly reflect the original Tweet with no truncation or incorrect entities, hence our recommendation to rely on the nested _retweeted\_status_ object for Retweets.