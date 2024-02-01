platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/tweet-timeline


## Filtering tips

Being familiar with the Twitter timeline of when and how new features were added can help you create more effective queries. Here, a query means a _filter_ or _rule_ that is applied by the Twitter historical APIs to the Tweet archive, using PowerTrack Operators to match on Tweet JSON. An example is the `lang:` Operator, which is used to match Tweets in a specified language. Twitter provides a language classification service (supporting over 50 languages), and Twitter APIs provide this metadata in the JSON that is generated for every Tweet. So, if a Tweet is written in Spanish the “lang” JSON attribute is set to “es”. So, if you build a filter with the `lang:es` clause, it will only match on Tweet messages classified as Spanish.

The timeline information can also help better interpret the Tweet data received. Say you were researching the sharing of content about the 2008 and 2012 Summer Olympics. If you applied only the `is:retweet` Operator to match on Retweets, no data would match in 2008. However, for 2012 there would likely be millions of Retweets. From this you potentially could erroneously conclude that in 2008 Retweets were not a user convention, or that simply no one Retweeted about those Olympics. Since Retweets became a first-class object in 2009, you need to add a `”RT @”` rule clause to help identify them in 2008.  

Both Retweets and Tweet language classifying are examples of Tweet attributes with a long history and many product details. Below we will discuss more details of these and other attribute classes important to matching on and understanding Twitter Data.  

#### Recognizing false negatives

When it comes to writing filters, one important takeaway is that the metadata Operators match on all have “born on” dates. If you build a filter with an Operator that acts on metadata introduced after the Tweet was posted, you’ll have a false negative. For example, say you are interested in all Tweets that mention ‘snow’ and share a video. If you build a rule with the `has:videos` Operator, which matches on Tweets with _native_ videos, that clause will not match any Tweets before 2015.

However, sharing of videos has been common on Twitter long before 2015. Before then users shared links to videos hosted elsewhere, but in 2015, Twitter built new ‘sharing video’ features directly into the platform. For finding these earlier Tweets of interest, you would include a rule clause such as `url:”youtube.com”`.  

Note, with the Search APIs, there are some examples of metadata being ‘backfilled’ as its index was rebuilt. One good example are $cashtags, which became widely used to discuss stock symbols in 2009. After the $cashtag operator was introduced in 2015, the Search index was rebuilt, and in the process the symbol entity was extracted from all Tweet bodies, including early 2006 when `$` was used mainly for slang; “I hope it $now$ $oon!”.  

#### Identifying and filtering on Tweet attributes important to your use-case

Some metadata, such as Twitter account numeric IDs, have existed since day one (and are an example of account metadata that never changes). Other metadata was not introduced until well after Twitter started in 2006. Examples of new metadata being introduced include Retweets metadata, Tweet locations, URL titles and descriptions, and ‘native’ media. Below are some of the most common types of Tweet attributes that have been fundamentally affected by these Twitter platform updates.

Filtering/matching behavior for these depends, in most cases, on which historical Tweet API is used. To help determine which product is the best fit for your research and use-case, the attribute details provided below include high-level product information.  

#### Twitter Profiles

Since at its core Twitter is a global real-time communication channel, research with Tweet data commonly has an emphasis on who is communicating. Often it is helpful to know where a Twitter user calls home. Often knowing that an account bio includes mentions of interests and hobbies can lead you to Tweets of interest. It is very common to want to listen for Tweets from accounts of interest. Profile attributes are key to all of these use-cases.

Every account on Twitter has a Profile that includes metadata such as Twitter @handle, display name, a short bio, home location (freeform text entered by a user), number of followers and many others. Some attributes never change, such as numeric user ID and when the account was created. Others usually change day-to-day, week-to-week, or month-to-month, such as number of Tweets posted and number of accounts followed and followers. Other account attributes can also change at any time, but tend to change less frequently: display name, home location, and bio.  

The JSON payload for every Tweet includes _account profile_ metadata for the Tweet’s author. If it is a Retweet, it also includes profile metadata for the account that posted the original Tweet.  

The mutability of a Tweet’s profile metadata depends entirely on the historical product used. The Search APIs serve up historical Tweets with the profile settings _as it is at the time of retrieval_. For Historical PowerTrack, the profile is _as it was at the time the Tweet was posted_, except for data before 2011. For Tweets older than 2011, the profile metadata reflects the profile as it was in September 2011.

#### Original Tweets and Retweets

Retweets are another example of user-driven conventions becoming official objects. Retweeting emerged as a way of ‘forwarding’ content to others. It started as a manual process of copying/pasting a Tweet and prepending it with a “RT @” pattern. This process was eventually automated via a new Retweet button, complete with new JSON metadata. The ‘official’ Retweet was born and the action of retweeting became a first-class Tweet event. Along with the new Retweet button, new metadata was introduced such as the complete payload of the original Tweet.

Whether a Tweet is original or shared is a common filtering ‘switch.’ In some cases, only original content is needed. In other cases, Tweet engagement is of primary importance so Retweets are key. The PowerTrack `is:retweet` Operator enables users to either include or exclude Retweets. If pulling data from before August 2009, users need to have _two_ strategies for Retweet matching (or not matching). Before August 2009, the Tweet message itself needs to be checked, using exact phrase matching, for matches on the “@RT ” pattern. For periods after August 2009, the `is:retweet` Operator is available.  

#### Tweet language classifications

The language a Tweet is written in is a common interest. Tweet language can help infer a Tweet’s location and often only a specific language is needed for analysis or display. (Twitter profiles also have a preferred language setting.)

For filtering on a Tweet’s language classification, Twitter’s historical products ([Search API](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/search/overview/enterprise) and [Historical PowerTrack](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/batch-historical/overview)) are quite different. When the Search archive was built, all Tweets were backfilled with the Twitter language classification. Therefore the `lang:` Operator is available for the entire Tweet archive. With Historical PowerTrack, Twitter’s language classification metadata is available in the archive beginning on March 26, 2013. 

#### Geo-referencing Tweets

Being able to tell where a Tweet was posted (i.e., geo-referencing it) is important to many use-cases. There are three primary methods for geo-referencing Tweets:

* Geographical references in a Tweet message
* Tweets geo-tagged by the user.
* Account profile ‘home’ location set by a user

If geo-referencing is key to your use-case, be sure to review our [filtering tweets by location](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/filtering-tweets-by-location)and [tweet geo metadata](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/tweet-geo-metadata) tutorials.

##### Geographical references in a Tweet message

Matching on geographic references in the Tweet message, while often the most challenging method since it depends on local knowledge, is an option for the entire Tweet archive. Here is an example geo-referenced match from 2006 for the San Francisco area based on a ‘golden gate’ filter:

https://twitter.com/biz/statuses/28311

##### Tweets geo-tagged by the user

In November 2009 Twitter introduced its Tweet Geotagging API that enabled Tweets to be geo-tagged with an exact location. In June 2010 Twitter introduced Twitter Places that represent a geographic area on the venue, neighborhood, or town scale. Approximately 1-2% of Tweets are geo-tagged using either method.

The available geo-tagging history is dependent on the Historical API you are using. With the Search APIs the ability to start matching on Tweets with some Geo Operators started in March 2010, and with others on February 2015. If you are using Historical PowerTrack, geo-referencing starts on September 1, 2011. When the Historical PowerTrack archive was built, all geo-tagging before this date was not included.  

##### Account profile ‘home’ location set by a user

All Twitter users have the opportunity to set their Profile Location, indicating their home location. Millions of Twitter users provide this information, and it significantly increases the amount of geodata in the Twitter Firehose. This location metadata is a non-normalized, user-generated, free-form string. Approximately 30% of accounts have Profile Geo metadata that can be resolved to the country level.

As with Tweet geo, the methods to match and the time periods available depends on the Historical API you are using. Historical PowerTrack enables users to attempt their own custom matching on these free-form strings. To help make that process easier, Twitter also provides a [Profile Geo Enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/enrichments/overview/profile-geo) that performs the geocoding where possible, providing normalized metadata and corresponding Operators. Profile Geo Operators are available in both Historical PowerTrack and the Search APIs. With Historical PowerTrack, these Profile Geo metadata is available starting in June 2014. With the Search APIs, this metadata is available starting in February 2015.  

#### Shared links and media

Sharing web page links, photos and videos have always been a fundamental Twitter use-case. Early in its history, all of these actions involved including a URL link in the Tweet message itself. In 2011 Twitter integrated sharing photos directly into its user-interface. In 2016, native videos were added.

Given this history, there are a variety of filtering Operators used for matching on this content. There are a set of Operators that match on whether Tweets have shared links, photos, and videos. Also, since most URLs shared on Twitter are shortened to use up fewer of a Tweet’s characters (e.g. generated by a service such as bitly or tinyurl), Twitter provides data enrichments that generate a complete, expanded URL that can be matched on. For example, if you wanted to match on Tweets that included links discussing Twitter and Early-warning systems, a filter that references ‘severe weather communication’ would match a Tweet containing this [http://bit.ly/1XV1tG4](http://bit.ly/1XV1tG4) URL.  

In March 2012, the [expanded URL enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/enrichments/overview/expanded-and-enhanced-urls) was introduced. Before this time, the Tweet payloads included only the URL as provided by the user. So, if the user included a shortened URL it can be challenging to match on (expanded) URLs of interest. With both Historical PowerTrack and the Search APIs, these metadata are available starting in March 2012.  

In July 2016, the enhanced URL enrichment was introduced. This enhanced version provides a web site’s HTML title and description in the Tweet payload, along with Operators for matching on those. With Historical PowerTrack, these metadata become available in July 2016. With the Search APIs, these metadata begin emerging in December 2014.  

In September 2016 Twitter introduced ‘native attachments’ where a trailing shared link is not counted against the 140 Tweet character limit. Both URL enrichments still apply to these shared links.  

For other URL product-specific details on URL filtering, see the corresponding articles for more information.