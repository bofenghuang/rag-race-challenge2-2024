platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/tweet-timeline


## Introduction

At its core, Twitter is a public, real-time, and global communication network. Since 2006, Twitter’s evolution has been driven by both user use-patterns and conventions and new product features and enhancements. If you are using Twitter data for historical research, understanding the timeline of this evolution is important for surfacing Tweets of interest from the data archive.

Twitter was launched as a simple SMS mobile app, and has grown into a comprehensive communication platform. A platform with a complete set of APIs. APIs have always been a pillar of the Twitter network. The [first API hit the streets soon after Twitter was launched](https://blog.twitter.com/2006/introducing-the-twitter-api). When geo-tagging Tweets was first introduced in 2009, it was made available through a [Geo API](https://blog.twitter.com/2009/think-globally-tweet-locally) (and later the ability to ‘geo-tag’ a Tweet was integrated into the Twitter.com user-interface). Today, Twitter’s APIs drive the two-way communication network that has become the source of breaking news and sharing information. The opportunities to build on top of this global, real-time communication channel are endless.  

Twitter makes available two historical APIs that provide access to every publicly available Tweet: [Historical PowerTrack](https://developer.twitter.com/en/docs/tweets/batch-historical) and the [Full-Archive Search API](https://developer.twitter.com/en/docs/tweets/search). Both APIs provide a set of _operators_ used to query and collect Tweets of interest. These operators match on a variety of attributes associated with every Tweet, hundreds of attributes such as the Tweet’s text content, the author’s account name, and links shared in the Tweet. Tweets and their attributes are encoded in JSON, a common text-based data-interchange format. So as new features were introduced, new JSON attributes appeared, and typically new API operators were introduced to match on those attributes. If your use-case includes a need to _listen_ to what the world has said on Twitter, the better you understand when operators started having JSON metadata to match on, the more effective your historical PowerTrack filters can be.  

Next, we will introduce some key concepts that set the stage for understanding how updates in Tweet metadata affect finding your data signal of interest.