platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule


### Operators

* **Essential:** Available when using any access level.
* **Elevated:** Available when using a Project with Pro, or Enterprise access.
* For some operators, an alternate name, or alias, is available. 

**Operator**[Type](#type)[Availability](#availability)DescriptionkeywordStandalone

Essential

Matches a keyword within the body of a Tweet. This is a tokenized match, meaning that your keyword string will be matched against the tokenized text of the Tweet body. Tokenization splits words based on punctuation, symbols, and Unicode basic plane separator characters.  
  
For example, a Tweet with the text “I like coca-cola” would be split into the following tokens: I, like, coca, cola. These tokens would then be compared to the keyword string used in your rule. To match strings containing punctuation (for example coca-cola), symbol, or separator characters, you must wrap your keyword in double-quotes.  
  
Example: pepsi OR cola OR "coca cola"emojiStandaloneEssentialMatches an emoji within the body of a Tweet. Similar to a keyword, emojis are a tokenized match, meaning that your emoji will be matched against the tokenized text of the Tweet body.  
  
Note that if an emoji has a variant, you must wrap it in double quotes to add to a rule.  
  
Example: (😃 OR 😡) 😬"exact phrase match"StandaloneEssentialMatches the exact phrase within the body of a Tweet.  
  
Example: ("Twitter API" OR #v2) -"filtered stream"#StandaloneEssentialMatches any Tweet containing a recognized hashtag, if the hashtag is a recognized entity in a Tweet.  
  
This operator performs an exact match, NOT a tokenized match, meaning the rule #thanku will match posts with the exact hashtag #thanku, but not those with the hashtag #thankunext.  
  
Example: #thankunext #fanart OR @arianagrande@StandaloneEssentialMatches any Tweet that mentions the given username, if the username is a recognized entity (including the @ character).  
  
Example: (@twitterdev OR @twitterapi) -@twitter$StandaloneEssentialMatches any Tweet that contains the specified ‘cashtag’ (where the leading character of the token is the ‘$’ character).  
  
Note that the cashtag operator relies on Twitter’s ‘symbols’ entity extraction to match cashtags, rather than trying to extract the cashtag from the body itself.  
  
Example: $twtr OR @twitterdev -$fbfrom:StandaloneEssentialMatches any Tweet from a specific user.  
The value can be either the username (excluding the @ character) or the user’s numeric user ID.  
  
You can only pass a single username/ID from: operator.  
  
Example: from:twitterdev OR from:twitterapi -from:twitterto:StandaloneEssentialMatches any Tweet that is in reply to a particular user.  
The value can be either the username (excluding the @ character) or the user’s numeric user ID.  
  
You can only pass a single username/ID per to: operator.  
  
Example: to:twitterdev OR to:twitterapi -to:twitterurl:StandaloneEssentialPerforms a tokenized match on any validly-formatted URL of a Tweet.  
  
This operator can matches on the contents of both the url or expanded\_url fields. For example, a Tweet containing "You should check out Twitter Developer Labs: https://t.co/c0A36SWil4" (with the short URL redirecting to https://developer.twitter.com) will match both the following rules:  
  
from:TwitterDev url:"https://developer.twitter.com"  
(because it will match the contents of entities.urls.expanded\_url)  
  
from:TwitterDev url:"https://t.co"  
(because it will match the contents of entities.urls.url)  
  
Tokens and phrases containing punctuation or special characters should be double-quoted (for example, url:"/developer"). Similarly, to match on a specific protocol, enclose in double-quotes (for example, url:"https://developer.twitter.com").  
  
You can only pass a single URL per url: operator.retweets\_of:StandaloneEssential

_Available alias:_ retweets\_of\_user:

Matches Tweets that are Retweets of the specified user. The value can be either the username (excluding the @ character) or the user’s numeric user ID.  
  
You can only pass a single username/ID per retweets\_of: operator.  
  
Example: retweets\_of:twitterdev OR retweets\_of:twitterapi

See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/users/lookup) for methods for looking up numeric Twitter Account IDs.

context:StandaloneEssentialMatches Tweets with a specific domain id and/or domain id, enitity id pair where \* represents a wildcard. To learn more about this operator, please visit our page on [Tweet annotations](https://developer.twitter.com/en/docs/twitter-api/annotations).  
  
You can only pass a single domain/entitie per context: operator.  
  
context:domain\_id.entity\_id  
context:domain\_id.\*  
context:\*.entity\_id  
  
Examples:  
context:10.799022225751871488  
(domain\_id.entity\_id returns Tweets matching that specific domain-entity pair)  
  
context:47.\*  
(domain\_id.\* returns Tweets matching that domain ID, with any domain-entity pair)  
  
context:\*.799022225751871488  
(\*.entity\_id returns Tweets matching that entity ID, with any domain-entity pair)entity:StandaloneEssentialMatches Tweets with a specific entity string value. To learn more about this operator, please visit our page on [annotations](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/annotations).  
  
You can only pass a single entity per entity: operator.  
  
entity:"string declaration of entity/place"  
  
Examples: entity:"Michael Jordan" OR entity:"Barcelona"conversation\_id:StandaloneEssentialMatches Tweets that share a common conversation ID. A conversation ID is set to the Tweet ID of a Tweet that started a conversation. As Replies to a Tweet are posted, even Replies to Replies, the conversation\_id is added to its JSON payload.  
  
You can only pass a single conversation ID per conversation\_id: operator.  
  
Example: conversation\_id:1334987486343299072 (from:twitterdev OR from:twitterapi)

bio:

StandaloneEssential

_Available alias:_ user\_bio:

Matches a keyword or phrase within the Tweet publisher's bio. This is a tokenized match within the contents of the description field within the [User object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/object-model/user).  
  
Example: bio:developer OR bio:"data engineer" OR bio:academic

bio\_name:StandaloneEssentialMatches a keyword within the Tweet publisher's user bio name. This is a tokenized match within the contents of a user’s “name” field within the [User object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/object-model/user).  
  
Example: bio\_name:phd OR bio\_name:md

bio\_location:

StandaloneEssential

_Available alias:_ user\_bio\_location:

Matches Tweets that are published by users whose location contains the specified keyword or phrase. This operator performs a tokenized match, similar to the normal keyword rules on the message body.  
  
This location is part of the [User object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/powertrack-api/guides/operators), matches on the 'location' field, and is a non-normalized, user-generated, free-form string. It is also different from a Tweet's location (see place:).  
  
Example: bio\_location:"big apple" OR bio\_location:nyc OR bio\_location:manhattan

place:StandaloneElevatedMatches Tweets tagged with the specified location or Twitter place ID. Multi-word place names (“New York City”, “Palo Alto”) should be enclosed in quotes.  
  
You can only pass a single place per place: operator.  
  
Note: See the [GET geo/search](https://developer.twitter.com/content/developer-twitter/en/docs/geo/places-near-location/api-reference/get-geo-search) standard v1.1 endpoint for how to obtain Twitter place IDs.  
  
Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.  
  
Example: place:"new york city" OR place:seattle OR place:fd70c22040963ac7place\_country:StandaloneElevatedMatches Tweets where the country code associated with a tagged place/location matches the given ISO alpha-2 character code.  
  
You can find a list of valid ISO codes on [Wikipedia](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).  
  
You can only pass a single ISO code per place\_country: operator.  
  
Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.  
  
Example: place\_country:US OR place\_country:MX OR place\_country:CApoint\_radius:StandaloneElevated

Matches against the place.geo.coordinates object of the Tweet when present, and in Twitter, against a place geo polygon, where the Place polygon is fully contained within the defined region.  
  
point\_radius:\[longitude latitude radius\]  

* Units of radius supported are miles (mi) and kilometers (km)  
    
* Radius must be less than 25mi  
    
* Longitude is in the range of ±180  
    
* Latitude is in the range of ±90  
    
* All coordinates are in decimal degrees  
    
* Rule arguments are contained within brackets, space delimited  
    

  
You can only pass a single geo polygon per point\_radius: operator.  
  
Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.  
  
Example: point\_radius:\[2.355128 48.861118 16km\] OR point\_radius:\[-41.287336 174.761070 20mi\]

bounding\_box:

StandaloneElevated

_Available alias:_ geo\_bounding\_box:

Matches against the place.geo.coordinates object of the Tweet when present, and in Twitter, against a place geo polygon, where the place polygon is fully contained within the defined region.  

  
bounding\_box:\[west\_long south\_lat east\_long north\_lat\]  
  

* west\_long south\_lat represent the southwest corner of the bounding box where west\_long is the longitude of that point, and south\_lat is the latitude.  
    
* east\_long north\_lat represent the northeast corner of the bounding box, where east\_long is the longitude of that point, and north\_lat is the latitude.  
    
* Width and height of the bounding box must be less than 25mi  
    
* Longitude is in the range of ±180  
    
* Latitude is in the range of ±90  
    
* All coordinates are in decimal degrees.  
    
* Rule arguments are contained within brackets, space delimited.  
    

  
You can only pass a single geo polygons per bounding\_box: operator.  
  
Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.  
  
Example: bounding\_box:\[-105.301758 39.964069 -105.178505 40.09455\]

is:retweetConjunction requiredEssentialMatches on Retweets that match the rest of the specified rule. This operator looks only for true Retweets (for example, those generated using the Retweet button). Quote Tweets will not be matched by this operator.  
  
Example: data @twitterdev -is:retweetis:replyConjunction requiredEssentialDeliver only explicit replies that match a rule. Can also be negated to exclude replies that match a rule from delivery.  
  
When used with the filtered stream, this operator matches on replies to an original Tweet, replies in quoted Tweets and replies in Retweets.  
  
Example: from:twitterdev is:replyis:quoteConjunction requiredEssentialReturns all Quote Tweets, also known as Tweets with comments.  
  
Example: "sentiment analysis" is:quoteis:verifiedConjunction requiredEssentialDeliver only Tweets whose authors are verified by Twitter.  
  
Example: #nowplaying is:verified\-is:nullcastConjunction requiredElevatedRemoves Tweets created for promotion only on ads.twitter.com that have a "source":"Twitter for Advertisers (legacy)" or "source":"Twitter for Advertisers".  
This operator must be negated.  
  
For more info on Nullcasted Tweets, see our page on [Tweet availability](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/guides/tweet-availability).  
  
Example: "mobile games" -is:nullcasthas:hashtagsConjunction requiredEssentialMatches Tweets that contain at least one hashtag.  
  
Example: from:twitterdev -has:hashtagshas:cashtagsConjunction requiredEssentialMatches Tweets that contain a cashtag symbol (with a leading ‘$’ character. For example, $tag).  
  
Example: #stonks has:cashtagshas:linksConjunction requiredEssentialThis operator matches Tweets which contain links and media in the Tweet body.  
  
Example: from:twitterdev announcement has:linkshas:mentionsConjunction requiredEssentialMatches Tweets that mention another Twitter user.  
  
Example: #nowplaying has:mentions

has:media

Conjunction requiredEssential

_Available alias:_ has:media\_link

Matches Tweets that contain a media object, such as a photo, GIF, or video, as determined by Twitter. This will not match on media created with Periscope, or Tweets with links to other media hosting sites.  
  
Example: (kittens OR puppies) has:media

has:imagesConjunction requiredEssentialMatches Tweets that contain a recognized URL to an image.  
  
Example: #meme has:images

has:video\_link

Conjunction requiredEssential

_Available alias:_ has:videos

Matches Tweets that contain native Twitter videos, uploaded directly to Twitter. This will not match on videos created with Periscope, or Tweets with links to other video hosting sites.  
  
Example: #icebucketchallenge has:video\_link

has:geoConjunction requiredEssentialMatches Tweets that have Tweet-specific geolocation data provided by the Twitter user. This can be either a location in the form of a Twitter place, with the corresponding display name, geo polygon, and other fields, or in rare cases, a geo lat-long coordinate.  
  
Note: Operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data.  
  
Example: recommend #paris has:geo -bakerysample:Conjunction requiredEssentialReturns a random percent sample of Tweets that match a rule rather than the entire set of Tweets. The percent value must be represented by an integer between 1 and 100 (for example, sample:10 will return a random 10% sample).  
  
This operator first reduces the scope of the stream to the percentage you specified, then the rule/filter is applied to that sampled subset. In other words, if you are using, for example, sample:10, each Tweet will have a 10% chance of being in the sample.  
  
This operator applies to the entire rule and requires all OR'd terms to be grouped.  
  
Example: #nowplaying @spotify sample:15lang:Conjunction requiredEssentialMatches Tweets that have been classified by Twitter as being of a particular language (if, and only if, the tweet has been classified). It is important to note that each Tweet is currently only classified as being of one language, so AND’ing together multiple languages will yield no results.  
  
You can only pass a single BCP 47 language identifier per lang: operator.  
  
Note: if no language classification can be made the provided result is ‘und’ (for undefined).  
  
Example: recommend #paris lang:en  
  
The list below represents the currently supported languages and their corresponding BCP 47 language identifier:  
  

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

followers\_count: Essential

Matches Tweets when the author has a followers count within the given range.

If a single number is specified, any number equal to or higher will match.

Example: followers\_count:500

Additionally, a range can be specified to match any number in the given range.

Example: followers\_count:1000..10000

tweets\_count:

 Essential

_Available alias:_ statuses\_count:

Matches Tweets when the author has posted a number of Tweets that falls within the given range.

If a single number is specified, any number equal to or higher will match.

Example: tweets\_count:1000

Additionally, a range can be specified to match any number in the given range.

Example: tweets\_count:1000..10000

following\_count:

 Essential

_Available alias:_ friends\_count:

Matches Tweets when the author has a friends count (the number of users they follow) that falls within the given range.

If a single number is specified, any number equal to or higher will match.

Example: following\_count:500

Additionally, a range can be specified to match any number in the given range.

Example: following\_count:1000..10000

listed\_count:

 Essential

_Available alias:_ user\_in\_lists\_count:

Matches Tweets when the author is included in the specified number of Lists. 

If a single number is specified, any number equal to or higher will match.

Example: listed\_count:10

Additionally, a range can be specified to match any number in the given range.

Example: listed\_count:10..100

url\_title:

 Essential

_Available alias:_ within\_url\_title:

Performs a keyword/phrase match on the expanded URL HTML title metadata.

Example: url\_title:snow  

url\_description:

 Essential

_Available alias:_ within\_url\_description:

Performs a keyword/phrase match on the expanded page description metadata.

Example: url\_description:weather

url\_contains: Essential

Matches Tweets with URLs that literally contain the given phrase or keyword. To search for patterns with punctuation in them (i.e. google.com) enclose the search term in quotes.

NOTE: This will match against the expanded URL as well.

Example: url\_contains:photos

source: Essential

Matches any Tweet generated by the given source application. The value must be either the name of the application or the application’s URL. Cannot be used alone.

Example: source:"Twitter for iPhone"

Note: As a Twitter app developer, Tweets created programmatically by your application will have the source of your application Name and Website URL set in your [app settings](https://developer.twitter.com/en/docs/apps/app-management.html). 

in\_reply\_to\_tweet\_id:

 Essential

_Available alias:_ in\_reply\_to\_status\_id:

Deliver only explicit Replies to the specified Tweet.

Example: in\_reply\_to\_tweet\_id:1539382664746020864

retweets\_of\_tweet\_id:

 Essential

_Available alias:_ retweets\_of\_status\_id:

Deliver only explicit (or native) Retweets of the specified Tweet. Note that the status ID used should be the ID of an original Tweet and not a Retweet. 

Example: retweets\_of\_tweet\_id:1539382664746020864