platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/tweet-timeline


## Key concepts

#### From user-conventions to Twitter _first-class objects_

Twitter users organically introduced new, and now fundamental, communication patterns to the Twitter network. A seminal example is the hashtag, now nearly universally used across all social networks. Hashtags were introduced as a way to organize conversations and topics. On a network with hundreds of millions messages a day, tools to find Tweets of interest are key, and hashtags have become a fundamental method. Soon after the use of hashtags grew, they received official status and support from Twitter. As hashtags became a _‘first-class’ object_, this meant many things. It meant hashtags became clickable/searchable in the Twitter.com user interface. It also meant hashtags became a member of the Twitter _entities_ family, along with @mentions, attached media, stock symbols, and shared links. These entities are conveniently encoded in a pre-parsed JSON array, making it easier for developers to process, scan, and store them.

Retweets are another example of user-driven conventions becoming official objects. Retweeting emerged as a way of ‘forwarding’ content to others. It started as a manual process of copying/pasting a Tweet and prepending it with a “RT @” pattern. This process was eventually automated via a new Retweet button, complete with new JSON metadata. The ‘official’ Retweet was born. Other examples include ‘mentions’, sharing of media and web links, and sharing a location with your Tweet. Each of these use-patterns resulted in new [twitter.com](https://twitter.com/) user-interface features, new supporting JSON, and thus new ways to match on Tweets. All of these fundamental Tweet attributes have resulted in PowerTrack Operators used to match on them.  

#### Tweet metadata, mutability, updates, and currency

While Tweet messages can be up to a fixed number of characters long, the JSON description of a Tweet consists of over 100 attributes. Attributes such as who posted, at what time, whether it’s an original Tweet or a Retweet, and an array of first-class objects such as hashtags, mentions, and shared links. For the account that posted, there is a User (or Actor) object with a variety of attributes that provide the user’s Profile and other account metadata. Profiles include a short biographical description, a home location (freeform text), preferred language, and an optional web site link.

Some account metadata never change (e.g. numeric user ID and created date), some change slowly over time, while other attributes change more frequently. People change jobs and move. Companies updates their information. When you are collecting historical Tweets, it is important to understand how some metadata is _as it was when Tweeted_, and other metadata is _as it is when the query is submitted_. 

With all historical APIs, the user's profile description, display name, and profile 'home' attributes are updated to the values at the time of query.

#### “Native” media

Twitter.com and Twitter mobile apps support adding photos and videos to Tweets by clicking a button and browsing your photo galleries. Now that they are integrated as first-class actions, videos and photos shared this way are referred to as ‘native’ media.

Many querying Operators work with these ‘native’ resources, including `has:videos`, `has:images`, and `has:media`. These will match only on media content that was shared via Twitter features. To match on other media hosted off of the Twitter platform, you’ll want to use Operators that match on URL metadata.  

So, before we dig into the Historical PowerTrack and Full-Archive Search product details, let’s take a tour of how Twitter, as a product and platform, evolved over time.