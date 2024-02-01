platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/migrate


###   
  
  
Filtering operator comparison

The two different versions (enterprise, and v2) of Tweet counts differ in which operators are available, and also have varying levels of operator availability within each version, which are explained below.

Enterprise

* There are no sub-tiers of enterprise operators. All enterprise operators are available to all enterprise users.  
      
    

Twitter API v2

* **Core:** These operators are available to any v2 user.
* **Advanced:** These operators are only available to users that have been approved for Academic Research access.  
      
    

You can learn more about each of these sets of operators in their respective guides:

* [Enterprise operators](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/guides/operators)
* [Twitter API v2 operators](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query)  
      
    

Now that we understand these different operator levels within Twitter API v2, here is the table that maps out operator availability for Tweet counts (note that if the cell is left blank, the operator is not available):

|     | Enterprise | v2  |
| --- | --- | --- |
| keyword | Available | Core |
| emoji | Available | Core |
| “exact phrase” | Available | Core |
| #   | Available | Core |
| $   | Available | Advanced |
| @   | Available | Core |
| from: | Available | Core |
| to: | Available | Core |
| url: | Available | Core |
| retweets\_of: | Available | Core |
| context: |     | Core |
| entity: |     | Core - Only available with recent search |
| conversation\_id: |     | Core |
| place: | Available | Advanced |
| place\_country: | Available | Advanced |
| point\_radius: | Available | Advanced |
| bounding\_box: | Available | Advanced |
| is:retweet | Available | Core |
| is:reply | Available | Core |
| is:quote | Available | Core |
| is:verified | Available | Core |
| \-is:nullcast | Available | Advanced |
| has:hashtags | Available | Core |
| has:cashtags | Available | Advanced |
| has:links | Available | Core |
| has:mentions | Available | Core |
| has:media | Available | Core |
| has:images | Available | Core |
| has:videos | Available | Core |
| has:geo | Available | Advanced |
| lang: | Available | Core |
| list: |     | Advanced |
| has:profile\_geo | Available |     |
| profile\_country | Available |     |
| profile\_locality | Available |     |
| profile\_region | Available |     |
| proximity | Available |     |