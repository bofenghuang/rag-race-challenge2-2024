platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/guides/changelog


### Filtering tips

Given all the above timeline information, it is clear that there are a lot of details to consider when writing Search APIs filters. There are two key things to consider:

* Some metadata have ‘born-on’ dates so filters can result in _false negatives_. Such searches include Operators reliant on metadata that did not exist for all of part of the search period. For example, if you are searching for Tweets with the `has:images` Operator, you will not have any matches for periods before July 2011. That is because that Operator matches on _native_ photos (attached to a Tweet using the Twitter user-interface). For a more complete data set of photo-sharing Tweets, filters for before July 2011 would need to contain rule clauses that match on common URLs for photo hosting.
* Some metadata has been backfilled with metadata from a time _after_ the Tweet was posted.

There are several attribute types that are commonly focused on when creating PowerTrack queries:

* Twitter Profiles
* Original or shared Tweets
* Tweet language classification
* Geo-referencing Tweets
* Shared links media

Some of these have product-specific behavior while others have identical behavior. See below for more details.

#### Twitter Profiles

The Search APIs serves historical Tweets with the user profile data set as it is at the _time of retrieval_. If you request a Tweet from 2014, the user’s profile metadata will reflect how it exists at query-time.

#### Original Tweets and Retweets

The PowerTrack `_is:retweet_` Operator enables users to either include or exclude Retweets. Users of this Operator need to have two strategies for Retweet matching (or not matching) for data before August 2009. Before August 2009, the Tweet message itself needs to be checked, using exact phrase matching, for matches on the “@RT ” pattern (Actually, if you are filtering on Retweets from between May-August 2009, the “Via @” pattern should be included). For periods after August 2009, the _is:retweet_ Operator is available.

#### Tweet language classifications

For filtering on a Tweet’s language classification, Twitter’s historical products are quite different. When the Search archive was built, all Tweets were backfilled with the Twitter language classification. Therefore the lang: Operator is available for the entire Tweet archive.

#### Geo-referencing Tweets

There are three primary ways to geo-reference Tweets:

* **Geographical references in Tweet message.** Matching on geographic references in the Tweet message, while often the most challenging method since it depends on local knowledge, is an option for the entire Tweet archive. [Here](https://twitter.com/biz/statuses/28311) is an example geo-referenced match from 2006 for the San Francisco area based on a ‘golden gate’ filter.
    
* **Tweets geo-tagged by the user.** With the search APIs the ability to start matching on Tweets with some Geo Operators started in March 2010, and with others in February 2015:
    
    * March 6, 2010: `has:geo`, `bounding_box:` and `point_radius:`
    * February 17, 2015: `place_country:` and `place:`
* **Account profile ‘home’ location set by the user.** Profile Geo Operators are available in both Historical PowerTrack and the Search APIs. With the Search APIs, these Profile Geo metadata is available starting in February 2015. For Tweets posted before Profile Geo metadata became available, the `bio_location:` Operator is available which can be used to match on non-normalized user input.
    

#### Shared links and media

In March 2012, the expanded URL enrichment was introduced. Before this time, the Tweet payloads included only the URL as provided by the user. So, if the user included a shortened URL it can be challenging to match on (expanded) URLs of interest. With the Search APIs, these metadata are available starting in March 2012.

In July 2016, the enhanced URL enrichment was introduced. This enhanced version provides a web site’s HTML title and description in the Tweet payload, along with Operators for matching on those. These metadata begin emerging in December 2014.

In September 2016 Twitter introduced ‘native attachments’ where a trailing shared link is not counted against the 140 Tweet character limit. Both URL enrichments still apply to these shared links.

Here are when related Search Operators begin matching:

* 2006 October 26 - `has:links`
* 2011 July 20 - `has:images` and `has:media`
* 2011 August - `url:` with the [Expanded URLs enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) As early as September 2006 `(url:"spotify.com" OR url:gnip OR url:microsoft OR url:google OR url:youtube)` matches http://twitter.com/Adam/statuses/16602, even though there is no urls\[\] metadata in twitter\_entities and gnip objects. “youtube.com” is an example of message content that, without any urls\[\] metadata, matches url:youtube.
* 2015 February 10 - `has:videos` for native videos. Between 2010/08/28 and 2015/02/10, this Operator matches on Tweets with links to select video hosting sites such as youtube.com, vimeo.com, and vivo.com.
* 2016 May 1 - `url_title:` and `url_description:`, based on the [Enhanced URLs enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls), generally available. First Enhanced URL metadata began appearing in December 2014.