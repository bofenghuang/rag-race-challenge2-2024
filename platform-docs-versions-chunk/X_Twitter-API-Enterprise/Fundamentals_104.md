platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/tweet-timeline


## Twitter timeline

Below you will find a select _timeline_ of Twitter. Most of these Twitter updates in some way fundamentally affected either user behavior, Tweet JSON contents, query Operators, or all three. Looking at Twitter as a API platform, the following events in some way affected the JSON payloads that are used to encode Tweets. In turn, those JSON details affect how Twitter historical API match on them.

Note that this timeline list is generally precise and not exhaustive.  

#### 2006

* October
    * @replies becomes a convention.
    * $cashtags first emerge, but using for stock ticker mentions does not become common until early 2009. $Cashtags became a clickable/searchable link in June 2012.
* November - Favorites introduced.

#### 2007

* January - @replies become a first-class object with a UI reply button with `in_reply_to` metadata.
* April - Retweets become a convention.
* August - #hashtags emerge as a primary tool for searching and organizing Tweets.

#### 2009

* February - $cashtags become a common convention for discussing stock ticker symbols.
* May - Retweet ‘beta’ is introduced with “Via @” prepended to Tweet body.
* June - Verified accounts introduced.
* August - Retweets a first-class object with “RT @” pattern and new `retweet_status` metadata.
* October - List feature launched.
* November - [Tweet Geotagging API is launched](https://blog.twitter.com/2009/think-globally-tweet-locally), providing the first method for users to share location via third-party apps.

#### 2010

* June - Twitter Places introduced for geo-tagging Tweets.
* August - Tweet button for websites is launched. Made sharing links easier.

#### 2011

* May - Follow button introduced, making it easier to follow accounts associated with websites.
* August - Native photos introduced.

#### 2012

* June - $Cashtags become a clickable/searchable link.

#### 2014

* March - [Photo tagging and up to four photos supported](https://blog.twitter.com/2014/photos-just-got-more-social). _Extended_ Twitter Entities metadata was introduced.
* April - Emojis are natively supported in Twitter UI. Emojis were commonly used in Tweets since at least 2008.

#### 2015

* April - A change in Twitter’s ‘post Tweet’ user-interface design results in fewer Tweets being geo-tagged.
* October - [Twitter Polls introduced](https://blog.twitter.com/2015/introducing-twitter-polls). Polls originally supported two choices with a 24-hour voting period. In November, Polls started supporting four choices with voting periods from 5 minutes to seven days. Poll metadata made available (enriched native format only) in February 2017.

#### 2016

* February - [Searchable GIFs natively hosted in Tweet compose](https://blog.twitter.com/2016/introducing-gif-search-on-twitter).
* May - [“Doing More with 140”](https://blog.twitter.com/express-even-more-in-140-characters) (dmw140) announced, stating plans for new ways of handling Replies and attached media with respect to a Tweet’s 140-character message.
* June - [Native video support](https://blog.twitter.com/official/en_us/a/2016/new-ways-to-tap-into-video-on-twitter.html)
* June - Quoted Retweets generally available.
* June - [Stickers introduced for adding to photos](https://blog.twitter.com/2016/introducing-stickers-on-twitter).
* September - [‘Native attachments’ introduced](https://twitter.com/Twitter/status/777915304261193728) with trailing URL not counted towards 140 characters (“dmw140, part 1”).

#### 2017

* February - Twitter Poll metadata included in Tweet metadata (enriched native format only).
* April - [‘Simplified Replies’](https://blog.twitter.com/2017/now-on-twitter-140-characters-for-your-replies) introduced with replied-to-accounts not counted towards 140 characters (“dmw140, part 2”).

2018

* May - [GDPR updates](https://twittercommunity.com/t/upcoming-changes-to-the-developer-platform/104603) user.time\_zone set to null, user.utc\_offset set to null, user.profile\_background\_image\_url set to default value
* June - Updating [quoteTweet formatting changes](https://twittercommunity.com/t/updating-how-urls-are-rendered-in-the-quote-tweet-payload/105473)

2022

* September 29 - The ability to edit Tweets is rolled out to a small test group. Edited Tweet metadata are added to the Tweet object where relevant. This includes edit\_history and edit\_controls objects. These metadata will not be returned for Tweets that were created before editable functionality was added. No associated Operators for these metadata. To learn more about how Tweet edits work, see the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/edit-tweets)