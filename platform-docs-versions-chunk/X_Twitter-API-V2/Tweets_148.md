platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate


### Filtering operator comparison

The four different versions (standard, enterprise, and v2) of search Tweets differ in which operators are available, and also have varying levels of operator availability within each version, which are explained below. 

Enterprise

* There are no sub-tiers of enterprise operators  
     

Twitter API v2

* **Free:** Available when using any Project
* **Basic:** Available when using any Project
* **Pro:** Available when using a Project 
* **Enterprise:** Available when using a Project 

You can learn more about each of these sets of operators in their respective guides:

* [Enterprise operators](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/guides/operators)
* [Twitter API v2 operators](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query)  
     

Now that we understand the different operator levels within Twitter API v2, here is the table that maps out operator availability for search Tweets (note that if the cell is left blank, the operator is not available):

| Search operator | Standard | Enterprise | v2  |
| --- | --- | --- | --- |
| keyword | Available  <br>q:keyword | Available | Basic & Pro |
| emoji | Available  <br>q:😄 | Available | Basic & Pro |
| “exact phrase” | Available | Available | Basic & Pro |
| #   | Available | Available | Basic & Pro |
| $   | Available | Available | Pro |
| @   | Available | Available | Basic & Pro |
| from: | Available | Available | Basic & Pro |
| to: | Available | Available | Basic & Pro |
| url: | Available | Available | Basic & Pro |
| retweets\_of: |     | Available | Basic & Pro |
| context: |     |     | Basic & Pro |
| entity: |     |     | Basic & Pro - Only available with recent search |
| conversation\_id: |     |     | Basic |
| place: |     | Available | Pro |
| place\_country: |     | Available | Pro |
| point\_radius: | geocode parameter | Available | Pro |
| bounding\_box: |     | Available | Pro |
| is:retweet | filter:retweets | Available | Basic & Pro |
| is:reply |     | Available | Basic & Pro |
| is:quote |     | Available | Basic & Pro |
| is:verified |     | Available | Basic & Pro |
| \-is:nullcast |     | Available | Pro |
| has:hashtags |     | Available | Basic & Pro |
| has:cashtags |     | Available | Pro |
| has:links | filter:links | Available | Basic & Pro |
| has:mentions |     | Available | Basic & Pro |
| has:media | filter:media | Available | Basic & Pro |
| has:images | filter:images, filter:twimg | Available | Basic & Pro |
| has:videos | filter:videos  <br>filter:native\_video | Available | Basic & Pro |
| has:geo |     | Available | Pro |
| lang: | lang - can be used as an operator or a parameter | Available | Basic & Pro |
| has:profile\_geo |     | Available |     |
| profile\_country |     | Available |     |
| profile\_locality |     | Available |     |
| profile\_region |     | Available |     |
| proximity |     | Available |     |
| :(  | Available |     |     |
| :)  | Available |     |     |
| ?   | Available |     |     |
| filter:periscope | Available |     |     |
| list: | Available |     | Pro |
| filter:replies | Available |     |     |
| filter:pro\_video | Available |     |     |
| filter:social | Available |     |     |
| filter:trusted | Available |     |     |
| filter:follows | Available |     |     |
| filter:has\_engagement | Available |     |     |
| include:antisocial | Available |     |     |
| include:offensive\_user | Available |     |     |
| include:antisocial\_offensive\_user | Available |     |     |
| include:sensitive\_content | Available |     |     |
| source: | Available |     |     |
| min\_replies: | Available |     |     |
| min\_retweets: | Available |     |     |
| min\_faves: | Available |     |     |
| card\_name: | Available |     |     |
| card\_domain: | Available |     |     |