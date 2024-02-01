platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/guides/changelog


### Metadata timelines

Below is a timeline of when Full-archive search endpoint Operators begin matching. In some cases Operator matching began well _after_ a ‘communication convention’ became commonplace on Twitter. For example, @Replies emerged as a user convention in 2006, but did not become a _first-class object_ or _event_ with ‘supporting’ JSON until early 2007. Accordingly, matching on @Replies in 2006 requires an examination of the Tweet body, rather than relying on the `to:` and `in_reply_to_status_id:` PowerTrack Operators.

The details provided here were generated using Full-Archive Search (a product of hundreds of searches). This timeline is not 100% complete or precise. If you identify another filtering/metadata “born on date” fundamental to your use-case, please let us know.

Note that the underlying Search index is subject to being rebuilt. Accordingly, these timeline details are subject to change.

#### 2006

* March 26 - `lang:`. An example of Tweet metadata being backfilled while generating the Search index.
* July 13 - `has:mentions` begins matching.
* October 6 - `has:symbols`. $cashtags (or symbols) for discussing stock symbols does not become common until early 2009. Until then most usages were probably slang (e.g., $slang).
* October 26 - `has:links` begins matching.
* November 23 - `has:hashtags` begins matching.

#### 2007

* January 30 - First first-class @reply (in\_reply\_to\_user\_id), `reply_to_status_id:` begins matching.
* August 23 - Hashtags emerge as a common convention for organizing topics and conversations. First real use a week later.

#### 2009

* May 15 - `is:retweet`. Note that this Operator starts matching with the ‘beta’ release of official Retweets and its “Via @’ pattern. During this beta period, the Tweet verb is ‘post’ and the original Tweet is not included in the payload.
* August 13 - Final version of official Retweets is released with “RT @” pattern, a verb set to ‘share’, and the ‘retweet\_status’ attribute containing the original Tweet (thus approximately doubling the JSON payload size).

#### 2010

* March 6 - `has:geo`, `bounding_box:` and `point_radius:` geo Operators begin matching.
* August 28 - `has:videos` (Until February 2015, this Operator matches on Tweets with links to select video hosting sites such as youtube.com, vimeo.com, and vivo.com).

#### 2011

* July 20 - `has:media` and `has:images` begin matching. Native photos officially announced August 9, 2010.

#### 2014

* December 3 - (Approximately) _Some_ [Enhanced URL metadata](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) with HTML title and description begins in payloads. Enhanced metadata more fully emerged in May 2016.

#### 2015

* February 10 - `has:videos` matches on ‘native’ Twitter videos.
* February 17 - `has:profile_geo`, `profile_country:`, `profile_region:`, `profile_locality:` [Profile Geo](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo) Operators begin matching.
* February 17 - `place_country:` and `place:` Tweet geo Operators begin matching.

#### 2016

* May 1 - [Enhanced URL metadata](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) more fully available, and was officially announced as part of the [Gnip 2.0 launch in August 2016](https://blog.twitter.com/2016/gnip-2-is-here). No associated Operators for these metadata with Search APIs.

#### 2017

* February 22 - Poll metadata become available in enriched native format. No associated Operators for these metadata.

#### 2022

* September 27 - All Tweet objects created since this date have Edited Tweet metadata available. All Enterprise endpoints that provide Tweet objects were updated to provide this metadata starting on this date. The edit metadata provided includes edit\_history and edit\_controls objects. These metadata will not be returned for Tweets that were created before September 27, 2022. Currently, there are no Enterprise Operators available that match these metadata.  To learn more about Edit Tweet metadata, check out the [Edit Tweets fundamentals](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/edit-tweets) page.

#### 2022

* September 29 - All Tweet objects created since this date have Edited Tweet metadata available. All Enterprise endpoints that provide Tweet objects were updated to provide this metadata starting on this date. The edit metadata provided includes edit\_history and edit\_controls objects. These metadata will not be returned for Tweets that were created before September 27, 2022. Currently, there are no Enterprise Operators available matching these metadata.  To learn more about Edit Tweet metadata, check out the [Edit Tweets fundamentals](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/edit-tweets) page.