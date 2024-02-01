platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview


### Available operators

Enterprise search APIs support rules with up to 2,048 characters. The enterprise search APIs support the operators listed below. For detailed descriptions see [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/guides/search-api/enterprise-operators). 

|     |     |     |     |
| --- | --- | --- | --- |
| **Matching on Tweet contents:** | **Matching on accounts of interest:** | **Tweet attributes:** | **Geospatial operators:** |
| * keyword<br>* “quoted phrase”<br>* “keyword1 keyword2”~N<br>* #<br>* @<br>* $<br>* url:<br>* lang: | * from:<br>* to:<br>* retweets\_of: | * is:retweet  <br>    <br>* has:mentions<br>* has:hashtags<br>* has:media<br>* has:videos<br>* has:images<br>* has:links<br>* has:symbols<br>* is:verified  <br>    <br>* \-is:nullcast (negation only operator) | * bounding\_box:\[west\_long south\_lat east\_long north\_lat\]<br>* point\_radius:\[lon lat radius\]<br>* has:geo<br>* place:<br>* place\_country:<br>* has:profile\_geo<br>* profile\_country:<br>* profile\_region:<br>* profile\_locality: |

  
Notes: Do not embed/nest operators ("#cats") will resolve to cats with the search APIs.   The ‘lang:’ operator and all ‘is:’ and ‘has:’ operators cannot be used as standalone operators and must be combined with another clause (e.g. @twitterdev has:links).    

Search APIs use a limited set of operators due to tokenization/matching functionality. enterprise real-time and batched historical APIs provide additional operators. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/operators-by-product) for more details.  

For more details, please see the [Getting started with operators](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/rules-and-filtering/building-a-rule) guide.