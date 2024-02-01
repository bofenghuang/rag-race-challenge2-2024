platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/enterprise-operators


#  

Matches any Tweet with the given hashtag.

This operator performs an exact match, NOT a tokenized match, meaning the rule “2016” will match posts with the exact hashtag “2016”, but not those with the hashtag “2016election”

Example:  
(#social OR #pizza OR #2016election) -#planet

**Note**: that the hashtag operator relies on Twitter’s entity extraction to match hashtags, rather than extracting the hashtag from the body itself. See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.

@  

Matches any Tweet that mentions the given username.

The to: operator returns a subset match of the @mention operator.

Example:  
(@twitterdev OR @twitterapi OR @twittereng) -@jack

**Note**: that the mention operator relies on Twitter’s entity extraction to match mentioned users, rather than extracting the mention from the body itself. See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.  

"keyword1 keyword2"~N  

Commonly referred to as a proximity operator, this matches a Tweet where the keywords are no more than N tokens from each other.

If the keywords are in the opposite order, they can not be more than N-2 tokens from each other.

Can have any number of keywords in quotes.

N cannot be greater than 6.

Example:  
"social media"~5 OR "twitter API"~3 

  
**Note**: Only available with PowerTrack and Historical PowerTrack.

contains:

Substring match for Tweets that have the given substring in the body, regardless of tokenization. In other words, this does a pure substring match, and does not consider word boundaries.

Use double quotes to match substrings that contain whitespace or punctuation.

Example:  
(contains:social OR contains:"wikipedia.com") -contains:"buy now"

**Note**: Only available with PowerTrack and Historical PowerTrack.

from:  

Matches any Tweet from a specific user.

Example:  
(from:2244994945 OR from:twitterapi OR from:twittereng) -from:jack

The value must be the user’s Twitter numeric Account ID or username (excluding the @ character). See [HERE](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) for looking up numeric Twitter Account IDs.

to:  

Matches any Tweet that is in reply to a particular user.

Example:  
(to:2244994945 OR to:twitterapi OR to:twittereng) -to:jack

The value must be the user’s numeric Account ID or username (excluding the @ character). See [HERE](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup)  for looking up numeric Twitter Account IDs.  

url:  
Performs a tokenized (keyword/phrase) match on the expanded URLs of a Tweet (similar to url\_contains).  
  
Example:  
@twitterdev url:"developer.twitter.com"  
  
**Note:** When using PowerTrack or Historical PowerTrack, this operator will match on URLs contained within the original Tweet of a Quote Tweet. For example, if your rule includes url:"developer.twitter.com", and a Tweet contains that URL, any Quote Tweets of that Tweet will be included in the results. This is not the case when using the Search API.   
url\_title:  

_Available alias_: within\_url\_title: 

Performs a keyword/phrase match on the (new) expanded URL HTML title metadata. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) for more information on expanded URL enrichment.  
  
**Note**: Only available with PowerTrack and Historical PowerTrack.

url\_description:  

_Available alias_: within\_url\_description: 

Performs a keyword/phrase match on the (new) expanded page description metadata. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) for more information on expanded URL enrichment.  
  
  
**Note:** Only available with PowerTrack and Historical PowerTrack.

url\_contains:  

Matches Tweets with URLs that literally contain the given phrase or keyword. To search for patterns with punctuation in them (for example, google.com) enclose the search term in quotes.

Example:  
(url\_contains:"developer.twitter.com" OR url\_contains:wildfire) -url\_contains:reddit

**Note**: If you’re using the [Expanded URL](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) output format, we will match against the expanded URL as well.

bio:  

_Available alias_: user\_bio:

Matches a keyword or phrase within the user bio of a Tweet. This is a tokenized match within the contents of the 'description' field within the [User object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user).  
  
Example:  
(bio:engineer OR bio:"wordpress.com" OR bio:🚀) -bio:troll  
  
  
**Note:** Only available with PowerTrack and Historical PowerTrack.

bio\_name:  
Matches a keyword within the user bio name of a Tweet. This is a tokenized match within the contents of a user’s “name” field within the [User object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user).  
  
**Note:** Only available with PowerTrack and Historical PowerTrack.bio\_location:  

_Available alias_: user\_bio\_location:

Matches tweets where the User object's location contains the specified keyword or phrase. This operator performs a tokenized match, similar to the normal keyword rules on the message body.

This location is part of the [User object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user), and is the account's 'home' lcoation, is a non-normalized, user-generated, free-form string, and is different from a Tweet's location (when available). 

**Note:** Only available with PowerTrack and Historical PowerTrack.

statuses\_count:  

_Available alias_: tweets\_count:

Matches Tweets when the author has posted a number of statuses that falls within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range  (for example, statuses\_count:1000..10000).  

Example:  
to:twitterapi statuses\_count:10

@twitterdev statuses\_count:1..10

**Note:** Only available with PowerTrack and Historical PowerTrack.

followers\_count:  

Matches Tweets when the author has a followers count within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range (for example, followers\_count:1000..10000).'

**Note:** Only available with PowerTrack and Historical PowerTrack.

friends\_count:  

_Available alias_: following\_count: 

Matches Tweets when the author has a friends count (the number of users they follow) that falls within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range (for example, friends\_count:1000..10000).

**Note:** Only available with PowerTrack and Historical PowerTrack.

listed\_count:  

_Available alias_: user\_in\_lists\_count:

Matches Tweets when the author has been listed within Twitter a number of times falls within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range (for example, listed\_count:10..100).

**Note:** Only available with PowerTrack and Historical PowerTrack.  

$

Matches any Tweet that contains the specified ‘cashtag’ entity.

Example:  
($TWTR OR $TSLA OR $BRK.A) -$F

**Note**: The cashtag operator relies on Twitter’s ‘symbols’ entity extraction to match cashtags, rather than trying to extract the cashtag from the body itself. See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.

retweets\_of:  

_Available alias_: retweets\_of\_user:

Matches Tweets that are Retweets of a specified user. Accepts both usernames and numeric Twitter Account IDs (NOT Tweet status IDs).  
  
Example:  
(retweets\_of:2244994945 OR retweets\_of:twitterapi OR retweets\_of:twittereng) -retweets\_of:jack  
  
See [HERE](https://dev.twitter.com/rest/reference/get/users/lookup) for looking up numeric Twitter Account IDs.  

retweets\_of\_status\_id:  

_Available alias_: retweets\_of\_tweet\_id:

Deliver only explicit Retweets of the specified Tweet. Note that the status ID used should be the ID of an original Tweet and not a Retweet.   
  
Example:  
retweets\_of\_status\_id:1293593516040269825  
  
**Note:** Only available with PowerTrack and Historical PowerTrack.

in\_reply\_to\_status\_id:  

_Available alias_: in\_reply\_to\_tweet\_id:

Deliver only explicit replies to the specified Tweet.  
  
Example:  
in\_reply\_to\_status\_id:1293593516040269825  
  
**Note:** Only available with PowerTrack and Historical PowerTrack.

sample:

Returns a random sample of Tweets that match a rule rather than the entire set of Tweets. Sample percent must be represented by an integer value between 1 and 100. This operator applies to the entire rule and requires any “OR’d” terms be grouped.

**Important Note:** The sample operator first reduces the scope of the firehose to X%, then the rule/filter is applied tio that sampled subset. If you are using, for example, **sample:10**, each Tweet has a 10% chance of being in the sample. 

The sampling is deterministic, and you will get the same data sample in realtime as you would if you pulled the data historically.

Example:  
#happybirthday sample:5  
"happy birthday"~5 sample:80

**Note:** Only available with PowerTrack and Historical PowerTrack.

source:Matches any Tweet generated by the given source application. The value must be either the name of the application, or the application’s URL.  **Cannot be used alone.  
**  
Example:  
#happybirthday source:"Twitter for iPhone"  
"This is a test Tweet from my TestingApp" source:MyTestAppName  
  
**Note**: As a Twitter app developer, Tweets created programattically by your application will have the source of your application Name and Website URL set in your [app settings](https://developer.twitter.com/en/docs/apps/app-management.html). The source operator seraches on the Tweet source attribute.  See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.  
lang:  

Matches Tweets that have been classified by Twitter as being of a particular language (if, and only if, the tweet has been classified). It is important to note that each Tweet is currently only classified as being of one language, so AND’ing together multiple languages will yield no results. This operator is not recommended to be used alone, matching volume will be very high. 

The list below represents the current supported languages and their corresponding BCP 47 language indentifier:

|     |     |     |     |
| --- | --- | --- | --- |
| Amharic: am | German: de | Malayalam: ml | Slovak: sk |
| Arabic: ar | Greek: el | Maldivian: dv | Slovenian: sl |
| Armenian: hy | Gujarati: gu | Marathi: mr | Sorani Kurdish: ckb |
| Basque: eu | Haitian Creole: ht | Nepali: ne | Spanish: es |
| Bengali: bn | Hebrew: iw | Norwegian: no | Swedish: sv |
| Bosnian: bs | Hindi: hi | Oriya: or | Tagalog: tl |
| Bulgarian: bg | Latinized Hindi: hi-Latn | Panjabi: pa | Tamil: ta |
| Burmese: my | Hungarian: hu | Pashto: ps | Telugu: te |
| Croatian: hr | Icelandic: is | Persian: fa | Thai: th |
| Catalan: ca | Indonesian: in | Polish: pl | Tibetan: bo |
| Czech: cs | Italian: it | Portuguese: pt | Traditional Chinese: zh-TW |
| Danish: da | Japanese: ja | Romanian: ro | Turkish: tr |
| Dutch: nl | Kannada: kn | Russian: ru | Ukrainian: uk |
| English: en | Khmer: km | Serbian: sr | Urdu: ur |
| Estonian: et | Korean: ko | Simplified Chinese: zh-CN | Uyghur: ug |
| Finnish: fi | Lao: lo | Sindhi: sd | Vietnamese: vi |
| French: fr | Latvian: lv | Sinhala: si | Welsh: cy |
| Georgian: ka | Lithuanian: lt |     |

Example:  

(@twitterdev OR to:twitterdev) lang:es  

**Note:** The language operator matches on the specific Tweet language determined by Twitter and set as the lang Tweet attribute.  See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.  If no language classification can be made for a Tweet, the Tweet lang will be set as ‘und’ (for undefined).

place:  

Matches Tweets tagged with the specified location _or_ Twitter place ID (see examples). Multi-word place names (“New York City”, “Palo Alto”) should be enclosed in quotes.

Example:  
(place:London OR place:"Great Britain") -place:USA  
place:fd70c22040963ac7

**Note:** See the [GET geo/search](https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-search) public API endpoint for how to obtain Twitter place IDs.

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

place\_country:  

Matches Tweets where the country code associated with a tagged [place/location](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo) matches the given ISO alpha-2 character code.

Example:  
place\_country:GB OR place\_country:AU OR place\_country:CA  

Valid ISO codes can be found here: [http://en.wikipedia.org/wiki/ISO\_3166-1\_alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

point\_radius:\[lon lat radius\]  

Matches against the Exact Location (x,y) of the Tweet when present, and in Twitter, against a “Place” geo polygon, where the Place is fully contained within the defined region.

* Radius must be less than 25mi.
* Units of radius supported are miles (mi) and kilometers (km).
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained with brackets, space delimited.

Example:  
point\_radius:\[-105.27346517 40.01924738 0.5mi\]

point\_radius:\[2.355128 48.861118 16km\]

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

bounding\_box:\[west\_long south\_lat east\_long north\_lat\]  

_Available alias_: geo\_bounding\_box:

Matches against the Exact Location (long, lat) of the Tweet when present, and in Twitter, against a “Place” geo polygon, where the Place is fully contained within the defined region.

* west\_long south\_lat represent the southwest corner of the bounding box where west-long is the longitude of that point, and south\_lat is the latitude.
* east\_long and north\_lat represent the northeast corner of the bounding box, where east\_long is the longitude of that point, and north\_lat is the latitude.
    * Width and height of the bounding box must be less than 25mi
    * Longitude is in the range of ±180
    * Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained with brackets, space delimited.

Example:  
bounding\_box:\[-105.301758 39.964069 -105.178505 40.09455\]

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

profile\_country:  

Exact match on the “countryCode” field from the “address” object in the Profile Geo enrichment.

Uses a normalized set of two-letter country codes, based on ISO-3166-1-alpha-2 specification. This operator is provided in lieu of an operator for “country” field from the “address” object to be concise.

profile\_region:  

Matches on the “region” field from the “address” object in the Profile Geo enrichment.

This is an exact full string match. It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use “one/two”, not “one\\/two”. Use double quotes to match substrings that contain whitespace or punctuation.

profile\_locality:  

Matches on the “locality” field from the “address” object in the Profile Geo enrichment.

This is an exact full string match. It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use “one/two”, not “one\\/two”. Use double quotes to match substrings that contain whitespace or punctuation.

profile\_subregion:  

Matches on the “subRegion” field from the “address” object in the [Profile Geo](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo) enrichment. In addition to targeting specific counties, these operators can be helpful to filter on a metro area without defining filters for every city and town within the region.

This is an exact full string match. It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use “one/two”, not “one\\/two”. Use double quotes to match substrings that contain whitespace or punctuation.

has:geo  

Matches Tweets that have Tweet-specific geo location data provided from Twitter. This can be either “geo” lat-long coordinate, or a “location” in the form of a Twitter [“Place”](https://dev.twitter.com/overview/api/places), with corresponding display name, geo polygon, and other fields.

**Note**: When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:profile\_geo  

_Available alias_: has:derived\_user\_geo

Matches Tweets that have any [Profile Geo](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo) metadata, regardless of the actual value.  
  

**Note**: When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:links

This operator matches Tweets that contain a link or referenced media in the "text" object of the payload.  

**Note:** In addition to this operator matching Tweets with a link in their text, it also matches Tweets with media (image, video, gif), and Quote Tweets.

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

is:retweet  

Deliver only explicit retweets that match a rule. Can also be negated to exclude retweets that match a rule from delivery and only original content is delivered.

This operator looks only for true Retweets. Quoted Tweets which do not use Twitter’s Retweet functionality will not be matched by this operator.

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

is:reply  
Delivers only explicit replies that match a rule. Can also be negated to exclude replies that match a rule from delivery (see example request below).  
  
When used with PowerTrack, this operator matches on replies to an original Tweet, replies in quoted Tweets and replies in Retweets. When used with the Search API, this operator only matches on replies to an original Tweet and excludes replies in quoted Tweets and replies in Retweets.  
  
Example:  
#contest123 is:reply  
@twitterdev -is:reply  
  

**Note**: When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

is:quote

Delivers only Quote Tweets, or Tweets that reference another Tweet, as identified by the "is\_quote\_status":true in Tweet payloads. Can also be negated to exclude Quote Tweets. 

Example:  
@twitterdev is:quote  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

is:verified  
Deliver only Tweets where the author is “verified” by Twitter. Can also be negated to exclude Tweets where the author is verified.  
  
Example:  
@twitterdev is:verified  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:mentions  
Matches Tweets that mention another Twitter user.  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:hashtags  
Matches Tweets that contain a hashtag.  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:media  

_Available alias_: has:media\_link

Matches Tweets that contain a media url classified by Twitter. For example, pic.twitter.com.  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:images  
Matches Tweets that contain a media url classified by Twitter. For example, pic.twitter.com.  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:videos  

_Available alias_: has:video\_link

Matches Tweets that contain native Twitter videos, uploaded directly to Twitter. This will not match on videos created with YouTube, Periscope, or Tweets with links to other video hosting sites.  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:symbols  

Matches Tweets that contain a cashtag symbol (with a leading ‘$’ character. For example, $tag).

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.