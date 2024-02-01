platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/entities


### Quote Tweets

Quote Tweets were introduced in 2016, and differ from Retweets in that when you "quote" a Tweet you are adding new content "on top" of a shared Tweet. This new content can include nearly anything an original Tweet can have, including new text, hashtags, mentions, and URLs.

Quote Tweets can contain native media (photos, videos, and GIFs), and will appear under the entities object.

Since Twitter entities can be added, the Quote entities are likely different from the original entities.

In this example, a new URL and hashtag were positioned at the end of the Quote Tweet.

This Tweet, https://twitter.com/FloodSocial/status/907983973225160704, has the following Tweet text:

                  strange and equally tragic when islands flood... trans-atlantic testing of quote tweets | [@thisuser](https://twitter.com/andypiper) [@thatuser](https://twitter.com/johnd) [http://bit.ly/2vMMDuu](https://t.co/fzFgMhWlPO "http://bit.ly/2vMMDuu")  [#testing](https://twitter.com/hashtag/testing?src=hash)  

In this case, the top-level entities do not reflect the Quote details. 

However, the Tweet text and entities in extended\_tweet perfectly reflect the Quote Tweet with no truncation or incorrect entities, hence our recommendation to rely on the nested _extended\_tweet_ object for Quote Tweets.