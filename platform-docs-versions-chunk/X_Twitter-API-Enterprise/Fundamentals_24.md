platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet


### Additional Tweet attributes

Twitter APIs that provide Tweets (e.g. the GET statuses/lookup endpoint) may include these additional Tweet attributes:

| Attribute | Type | Description |
| --- | --- | --- |
| current\_user\_retweet | Object | _Perspectival_ Only surfaces on methods supporting the include\_my\_retweet parameter, when set to true. Details the Tweet ID of the user’s own retweet (if existent) of this Tweet. Example:<br><br>"current\_user\_retweet": {<br>  "id": 6253282,<br>  "id\_str": "6253282"<br>} |
| scopes | Object | A set of key-value pairs indicating the intended contextual delivery of the containing Tweet. Currently used by Twitter’s Promoted Products. Example:<br><br>"scopes":{"followers":false} |
| withheld\_copyright | Boolean | When present and set to “true”, it indicates that this piece of content has been withheld due to a [DMCA complaint](http://en.wikipedia.org/wiki/Digital_Millennium_Copyright_Act) . Example:<br><br>"withheld\_copyright": true |
| withheld\_in\_countries | Array of String | When present, indicates a list of uppercase [two-letter country codes](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) this content is withheld from. Twitter supports the following non-country values for this field:<br><br>“XX” - Content is withheld in all countries “XY” - Content is withheld due to a DMCA request.<br><br>Example:<br><br>"withheld\_in\_countries": \["GR", "HK", "MY"\] |
| withheld\_scope | String | When present, indicates whether the content being withheld is the “status” or a “user.”<br><br>Example:<br><br>"withheld\_scope": "status" |