platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet


### Tweet Data Dictionary

Below you will find the data dictionary for these ‘root-level’ attributes, as well as links to child object data dictionaries.

| Attribute | Type | Description |
| --- | --- | --- |
| created\_at | String | UTC time when this Tweet was created. Example:<br><br>"created\_at": "Wed Oct 10 20:19:24 +0000 2018" |
| id  | Int64 | The integer representation of the unique identifier for this Tweet. This number is greater than 53 bits and some programming languages may have difficulty/silent defects in interpreting it. Using a signed 64 bit integer for storing this identifier is safe. Use `**id_str**` to fetch the identifier to be safe. See [Twitter IDs](https://developer.twitter.com/en/docs/twitter-ids) for more information. Example:<br><br>"id":1050118621198921728 |
| id\_str | String | The string representation of the unique identifier for this Tweet. Implementations should use this rather than the large integer in `**id**`. Example:<br><br>"id\_str":"1050118621198921728" |
| text | String | The actual UTF-8 text of the status update. See [twitter-text](https://github.com/twitter/twitter-text/blob/master/rb/lib/twitter-text/regex.rb) for details on what characters are currently considered valid. Example:<br><br>"text":"To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm" |
| source | String | Utility used to post the Tweet, as an HTML-formatted string. Tweets from the Twitter website have a source value of `**web**`.<br><br>Example:<br><br>"source":"Twitter Web Client" |
| truncated | Boolean | Indicates whether the value of the `**text**` parameter was truncated, for example, as a result of a retweet exceeding the original Tweet text length limit of 140 characters. Truncated text will end in ellipsis, like this `**...**` Since Twitter now rejects long Tweets vs truncating them, the large majority of Tweets will have this set to `**false**` . Note that while native retweets may have their toplevel `**text**` property shortened, the original text will be available under the `**retweeted_status**` object and the `**truncated**` parameter will be set to the value of the original status (in most cases, `**false**` ). Example:<br><br>"truncated":true |
| in\_reply\_to\_status\_id | Int64 | _Nullable._ If the represented Tweet is a reply, this field will contain the integer representation of the original Tweet’s ID. Example:<br><br>"in\_reply\_to\_status\_id":1051222721923756032 |
| in\_reply\_to\_status\_id\_str | String | _Nullable._ If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s ID. Example:<br><br>"in\_reply\_to\_status\_id\_str":"1051222721923756032" |
| in\_reply\_to\_user\_id | Int64 | _Nullable._ If the represented Tweet is a reply, this field will contain the integer representation of the original Tweet’s author ID. This will not necessarily always be the user directly mentioned in the Tweet. Example:<br><br>"in\_reply\_to\_user\_id":6253282 |
| in\_reply\_to\_user\_id\_str | String | _Nullable._ If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s author ID. This will not necessarily always be the user directly mentioned in the Tweet. Example:<br><br>"in\_reply\_to\_user\_id\_str":"6253282" |
| in\_reply\_to\_screen\_name | String | _Nullable._ If the represented Tweet is a reply, this field will contain the screen name of the original Tweet’s author. Example:<br><br>"in\_reply\_to\_screen\_name":"twitterapi" |
| user | [User object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user) | The user who posted this Tweet. See User data dictionary for complete list of attributes.<br><br>Example highlighting select attributes:<br><br> { "user": {<br>    "id": 6253282,<br>    "id\_str": "6253282",<br>    "name": "Twitter API",<br>    "screen\_name": "TwitterAPI",<br>    "location": "San Francisco, CA",<br>    "url": "https://developer.twitter.com",<br>    "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",<br>    "verified": true,<br>    "followers\_count": 6129794,<br>    "friends\_count": 12,<br>    "listed\_count": 12899,<br>    "favourites\_count": 31,<br>    "statuses\_count": 3658,<br>    "created\_at": "Wed May 23 06:01:13 +0000 2007",<br>    "utc\_offset": null,<br>    "time\_zone": null,<br>    "geo\_enabled": false,<br>    "lang": "en",<br>    "contributors\_enabled": false,<br>    "is\_translator": false,<br>    "profile\_background\_color": "null",<br>    "profile\_background\_image\_url": "null",<br>    "profile\_background\_image\_url\_https": "null",<br>    "profile\_background\_tile": null,<br>    "profile\_link\_color": "null",<br>    "profile\_sidebar\_border\_color": "null",<br>    "profile\_sidebar\_fill\_color": "null",<br>    "profile\_text\_color": "null",<br>    "profile\_use\_background\_image": null,<br>    "profile\_image\_url": "null",<br>    "profile\_image\_url\_https": "https://pbs.twimg.com/profile\_images/942858479592554497/BbazLO9L\_normal.jpg",<br>    "profile\_banner\_url": "https://pbs.twimg.com/profile\_banners/6253282/1497491515",<br>    "default\_profile": false,<br>    "default\_profile\_image": false,<br>    "following": null,<br>    "follow\_request\_sent": null,<br>    "notifications": null<br>  }<br>} |
| coordinates | [Coordinates](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo#coordinates-dictionary) | _Nullable._ Represents the geographic location of this Tweet as reported by the user or client application. The inner coordinates array is formatted as [geoJSON](http://www.geojson.org/) (longitude first, then latitude). Example:<br><br>"coordinates":<br>{<br>    "coordinates":<br>    \[<br>        -75.14310264,<br>        40.05701649<br>    \],<br>    "type":"Point"<br>} |
| place | [Places](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo#place-dictionary) | _Nullable_ When present, indicates that the tweet is associated (but not necessarily originating from) a Place  Example:<br><br>"place":<br>{<br>  "attributes":{},<br>   "bounding\_box":<br>  {<br>     "coordinates":<br>     \[\[<br>           \[-77.119759,38.791645\],<br>           \[-76.909393,38.791645\],<br>           \[-76.909393,38.995548\],<br>           \[-77.119759,38.995548\]<br>     \]\],<br>     "type":"Polygon"<br>  },<br>   "country":"United States",<br>   "country\_code":"US",<br>   "full\_name":"Washington, DC",<br>   "id":"01fbe706f872cb32",<br>   "name":"Washington",<br>   "place\_type":"city",<br>   "url":"http://api.twitter.com/1/geo/id/0172cb32.json"<br>} |
| quoted\_status\_id | Int64 | This field only surfaces when the Tweet is a quote Tweet. This field contains the integer value Tweet ID of the quoted Tweet. Example:<br><br>"quoted\_status\_id":1050119905717055488 |
| quoted\_status\_id\_str | String | This field only surfaces when the Tweet is a quote Tweet. This is the string representation Tweet ID of the quoted Tweet. Example:<br><br>"quoted\_status\_id\_str":"1050119905717055488" |
| is\_quote\_status | Boolean | Indicates whether this is a Quoted Tweet. Example:<br><br>"is\_quote\_status":false |
| quoted\_status | Tweet | This field only surfaces when the Tweet is a quote Tweet. This attribute contains the Tweet object of the original Tweet that was quoted. |
| retweeted\_status | Tweet | Users can amplify the broadcast of Tweets authored by other users by Retweeting . Retweets can be distinguished from typical Tweets by the existence of a `**retweeted_status**` attribute. This attribute contains a representation of the _original_ Tweet that was retweeted. Note that retweets of retweets do not show representations of the intermediary retweet, but only the original Tweet. (Users can also unretweet a retweet they created by deleting their retweet.) |
| quote\_count | Integer | _Nullable._ Indicates approximately how many times this Tweet has been quoted by Twitter users. Example:<br><br>"quote\_count":33<br><br>Note: This object is only available with the Premium and Enterprise tier products. |
| reply\_count | Int | Number of times this Tweet has been replied to. Example:<br><br>"reply\_count":30<br><br>Note: This object is only available with the Premium and Enterprise tier products. |
| retweet\_count | Int | Number of times this Tweet has been retweeted. Example:<br><br>"retweet\_count":160 |
| favorite\_count | Integer | _Nullable._ Indicates approximately how many times this Tweet has been liked by Twitter users. Example:<br><br>"favorite\_count":295 |
| entities | [Entities](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) | Entities which have been parsed out of the text of the Tweet. Additionally see [Entities in Twitter Objects](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/entities.html) . Example:<br><br>"entities":<br>{<br>    "hashtags":\[\],<br>    "urls":\[\],<br>    "user\_mentions":\[\],<br>    "media":\[\],<br>    "symbols":\[\]<br>    "polls":\[\]<br>} |
| extended\_entities | [Extended Entities](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) | When between one and four native photos or one video or one animated GIF are in Tweet, contains an array 'media' metadata. This is also available in Quote Tweets. Additionally see [Entities in Twitter Objects](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/extended-entities.html) . Example:<br><br>"entities":<br>{<br>    "media":\[\]<br>} |
| favorited | Boolean | _Nullable._ Indicates whether this Tweet has been liked by the authenticating user. Example:<br><br>"favorited":true |
| retweeted | Boolean | Indicates whether this Tweet has been Retweeted by the authenticating user. Example:<br><br>"retweeted":false |
| possibly\_sensitive | Boolean | _Nullable._ This field indicates content may be recognized as sensitive. The Tweet author can select within their own account preferences and choose “Mark media you tweet as having material that may be sensitive” so each Tweet created after has this flag set.<br><br>This may also be judged and labeled by an internal Twitter support agent.<br><br>"possibly\_sensitive":false |
| filter\_level | String | Indicates the maximum value of the filter\_level parameter which may be used and still stream this Tweet. So a value of `**medium**` will be streamed on `**none**`, `**low**`, and `**medium**` streams.<br><br>Example:<br><br>"filter\_level": "low" |
| lang | String | _Nullable._ When present, indicates a [BCP 47](http://tools.ietf.org/html/bcp47) language identifier corresponding to the machine-detected language of the Tweet text, or `**und**` if no language could be detected. <br><br> Example:<br><br>"lang": "en" |
| edit\_history | Object | Unique identifiers indicating all versions of a Tweet. For Tweets with no edits, there will be one ID. For Tweets with an edit history, there will be multiple IDs, arranged in ascending order reflecting the order of edits, with the most recent version in the last position of the array. <br><br>The Tweet IDs can be used to hydrate and view previous versions of a Tweet.<br><br>Example:<br><br>edit\_history": {<br>    "initial\_tweet\_id": "1283764123"<br>    "edit\_tweet\_ids": \["1283764123", "1394263866"\]<br>  } |
| edit\_controls | Object | When present, indicates how long a Tweet is still editable for and the number of remaining edits. Tweets are only editable for the first 30 minutes after creation and can be edited up to five times. <br><br>The Tweet IDs can be used to hydrate and view previous versions of a Tweet.<br><br>Example:<br><br>"edit\_controls": {  <br>     "editable\_until\_ms": 123<br>     "edits\_remaining": 3   <br>  } |
| editable | Boolean | When present, indicates if a Tweet was eligible for edit when published. This field is not dynamic and won't toggle from True to False when a Tweet reaches its editable time limit, or maximum number of edits. The following Tweet features will cause this field to be false:<br><br>* Tweets is promoted<br>* Tweet has a poll<br>* Tweet is a non-self-thread reply<br>* Tweet is a retweet (note that Quote Tweets are eligible for edit)<br>* Tweet is nullcast<br>* Community Tweet<br>* Superfollow Tweet<br>* Collaborative Tweet |
| matching\_rules | Array of Rule Objects | Present in _filtered_ products such as Twitter Search and PowerTrack. Provides the _id_ and _tag_ associated with the rule that matched the Tweet. More on matching rules [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules.html). With PowerTrack, more than one rule can match a Tweet. <br><br>Example:<br><br>"matching\_rules": " \[{<br>        "tag": "twitterapi emojis",<br>        "id": 1050118621198921728,<br>        "id\_str": "1050118621198921728"<br>    }\]" |
|     |     |     |