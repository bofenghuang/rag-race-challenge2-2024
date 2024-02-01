platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query


### Operators

**Operator**[Type](#type)[Availability](#availability)DescriptionkeywordStandaloneEssentialMatches a keyword within the body of a Tweet. This is a tokenized match, meaning that your keyword string will be matched against the tokenized text of the Tweet body. Tokenization splits words based on punctuation, symbols, and Unicode basic plane separator characters.  
  
For example, a Tweet with the text “I like coca-cola” would be split into the following tokens: I, like, coca, cola. These tokens would then be compared to the keyword string used in your query. To match strings containing punctuation (for example coca-cola), symbol, or separator characters, you must wrap your keyword in double-quotes.  
  
Example: pepsi OR cola OR "coca cola"emojiStandaloneEssentialMatches an emoji within the body of a Tweet. Similar to a keyword, emojis are a tokenized match, meaning that your emoji will be matched against the tokenized text of the Tweet body.  
  
Note that if an emoji has a variant, you must wrap it in double quotes to add to a query.  
  
Example: (😃 OR 😡) 😬"exact phrase match"StandaloneEssentialMatches the exact phrase within the body of a Tweet.  
  
Example: ("Twitter API" OR #v2) -"recent search"#StandaloneEssentialMatches any Tweet containing a recognized hashtag, if the hashtag is a recognized entity in a Tweet.  
  
This operator performs an exact match, NOT a tokenized match, meaning the rule #thanku will match posts with the exact hashtag #thanku, but not those with the hashtag #thankunext.  
  
Example: #thankunext #fanart OR @arianagrande@StandaloneEssentialMatches any Tweet that mentions the given username, if the username is a recognized entity (including the @ character).  
  
Example: (@twitterdev OR @twitterapi) -@twitter$StandaloneElevatedMatches any Tweet that contains the specified ‘cashtag’ (where the leading character of the token is the ‘$’ character).  
  
Note that the cashtag operator relies on Twitter’s ‘symbols’ entity extraction to match cashtags, rather than trying to extract the cashtag from the body itself.  
  
Example: $twtr OR @twitterdev -$fbfrom:StandaloneEssentialMatches any Tweet from a specific user.  
The value can be either the username (excluding the @ character) or the user’s numeric user ID.  
  
You can only pass a single username/ID per from: operator.  
  
Example: from:twitterdev OR from:twitterapi -from:twitterto:StandaloneEssentialMatches any Tweet that is in reply to a particular user.  
The value can be either the username (excluding the @ character) or the user’s numeric user ID.  
  
You can only pass a single username/ID per to: operator.  
  
Example: to:twitterdev OR to:twitterapi -to:twitterurl:StandaloneEssentialPerforms a tokenized match on any validly-formatted URL of a Tweet.  
  
This operator can matches on the contents of both the url or expanded\_url fields. For example, a Tweet containing "You should check out Twitter Developer Labs: https://t.co/c0A36SWil4" (with the short URL redirecting to https://developer.twitter.com) will match both the following rules:  
  
from:TwitterDev url:"https://developer.twitter.com"  
(because it will match the contents of entities.urls.expanded\_url)  
  
from:TwitterDev url:"https://t.co"  
(because it will match the contents of entities.urls.url)  
  
Tokens and phrases containing punctuation or special characters should be double-quoted (for example, url:"/developer"). Similarly, to match on a specific protocol, enclose in double-quotes (for example, url:"https://developer.twitter.com").retweets\_of:StandaloneEssentialMatches Tweets that are Retweets of the specified user. The value can be either the username (excluding the @ character) or the user’s numeric user ID.  
  
You can only pass a single username/ID per retweets\_of: operator.  
  
Example: retweets\_of:twitterdev OR retweets\_of:twitterapi

in\_reply\_to\_tweet\_id:

StandaloneEssential

_Available alias:_ in\_reply\_to\_status\_id:

Matches on replies to the specified Tweet. 

Example: in\_reply\_to\_tweet\_id:1539382664746020864 

retweets\_of\_tweet\_id:

StandaloneEssential

_Available alias:_ retweets\_of\_status\_id:

Matches on explicit (or native) Retweets of the specified Tweet. Note that the Tweet ID used should be the ID of an original Tweet and not a Retweet. 

Example: retweets\_of\_tweet\_id:1539382664746020864 

quotes\_of\_tweet\_id:

StandaloneEssential

_Available alias:_ quotes\_of\_status\_id:

Matches on Quote Tweets of the specified Tweet. Note that the Tweet ID used should be the ID of an original Tweet and not a Quote Tweet. 

Example: quotes\_of\_tweet\_id:1539382664746020864 

context:StandaloneEssential

Matches Tweets with a specific domain id/enitity id pair. To learn more about this operator, please visit our page on [annotations](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/annotations).  
  
You can only pass a single domain/entity per context: operator.  
  
context:domain\_id.entity\_id  

However, you can combine multiple domain/entities using the OR operator:

`(context:47.1139229372198469633 OR context:11.1088514520308342784)`

Examples:  
context:10.799022225751871488  
(domain\_id.entity\_id returns Tweets matching that specific domain-entity pair)  

entity:StandaloneEssential

Matches Tweets with a specific entity string value. To learn more about this operator, please visit our page on [annotations](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/annotations).

**Please note** that this is only available with recent search.

You can only pass a single entity: operator.

entity:"string declaration of entity/place"  
  
Examples: entity:"Michael Jordan" OR entity:"Barcelona"

conversation\_id:StandaloneEssentialMatches Tweets that share a common conversation ID. A conversation ID is set to the Tweet ID of a Tweet that started a conversation. As Replies to a Tweet are posted, even Replies to Replies, the conversation\_id is added to its JSON payload.  
  
You can only pass a single conversation ID per conversation\_id: operator.  
  
Example: conversation\_id:1334987486343299072 (from:twitterdev OR from:twitterapi)list:StandaloneElevated

**NEW** Matches Tweets posted by users who are members of a specified list. 

For example, if @twitterdev and @twitterapi were members of List 123, and you included list:123 in your query, your response will only contain Tweets that have been published by those accounts. You can find List IDs by using the [List lookup](https://developer.twitter.com/en/docs/twitter-api/lists/lists-lookup) endpoint.

**Please note** that you can only use a single list: operator per query, and you can only specify a single List per list: operator.

Example: list:123

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

bounding\_box:StandaloneElevated

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
  
Example: data @twitterdev -is:retweetis:replyConjunction requiredEssentialDeliver only explicit replies that match a rule. Can also be negated to exclude replies that match a query from delivery.  
  
Note: This operator is also available with the filtered stream endpoint. When used with filtered stream, this operator matches on replies to an original Tweet, replies in quoted Tweets, and replies in Retweets.  
  
Example: from:twitterdev is:replyis:quoteConjunction requiredEssentialReturns all Quote Tweets, also known as Tweets with comments.  
  
Example: "sentiment analysis" is:quoteis:verifiedConjunction requiredEssentialDeliver only Tweets whose authors are verified by Twitter.  
  
Example: #nowplaying is:verified\-is:nullcastConjunction requiredElevatedRemoves Tweets created for promotion only on ads.twitter.com that have a "source":"Twitter for Advertisers (legacy)" or "source":"Twitter for Advertisers".  
This operator must be negated.  
  
For more info on Nullcasted Tweets, see our page on [Tweet availability](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/guides/tweet-availability).  
  
Example: "mobile games" -is:nullcasthas:hashtagsConjunction requiredEssentialMatches Tweets that contain at least one hashtag.  
  
Example: from:twitterdev -has:hashtagshas:cashtagsConjunction requiredElevatedMatches Tweets that contain a cashtag symbol (with a leading ‘$’ character. For example, $tag).  
  
Example: #stonks has:cashtagshas:linksConjunction requiredEssentialThis operator matches Tweets which contain links and media in the Tweet body.  
  
Example: from:twitterdev announcement has:linkshas:mentionsConjunction requiredEssentialMatches Tweets that mention another Twitter user.  
  
Example: #nowplaying has:mentionshas:mediaConjunction requiredEssential

_Available alias:_ has:media\_link

Matches Tweets that contain a media object, such as a photo, GIF, or video, as determined by Twitter. This will not match on media created with Periscope, or Tweets with links to other media hosting sites.  
  
Example: (kittens OR puppies) has:media

has:imagesConjunction requiredEssentialMatches Tweets that contain a recognized URL to an image.  
  
Example: #meme has:imageshas:video\_linkConjunction requiredEssential

_Available alias:_ has:videos

Matches Tweets that contain native Twitter videos, uploaded directly to Twitter. This will not match on videos created with Periscope, or Tweets with links to other video hosting sites.  
  
Example: #icebucketchallenge has:video\_link

has:geoConjunction requiredElevatedMatches Tweets that have Tweet-specific geolocation data provided by the Twitter user. This can be either a location in the form of a Twitter place, with the corresponding display name, geo polygon, and other fields, or in rare cases, a geo lat-long coordinate.  
  
Note: Operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data.  
  
Example: recommend #paris has:geo -bakerylang:Conjunction requiredEssentialMatches Tweets that have been classified by Twitter as being of a particular language (if, and only if, the Tweet has been classified). It is important to note that each Tweet is currently only classified as being of one language, so AND’ing together multiple languages will yield no results.  
  
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