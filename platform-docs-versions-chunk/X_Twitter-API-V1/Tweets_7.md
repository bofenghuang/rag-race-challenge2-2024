platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/guides/standard-operators


### Important Practices

* Ensure all parameters are properly URL encoded.
* Limit your searches to 10 keywords and operators.
* Queries can be limited due to complexity. If this happens, the Search API will respond with the error: {"error":"Sorry, your query is too complex. Please reduce complexity and try again."}.
* The Search API is not a complete index of all Tweets, but instead an index of recent Tweets. The index includes between 6-9 days of Tweets.

**Example searches:**

When you are following an event that’s currently happening, you would be interested in search for recent Tweets using the event hashtag  

You want recent Tweets that contain the hashtag #superbowl

Your search URL is: https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result\_type=recent

`twurl /1.1/search/tweets.json?q=%23superbowl&result_type=recent`  

When you want to know what Tweets are coming from a specific location, with a specific language:

You want: all recent Tweets in Portuguese, near Maracanã soccer stadium in Rio de Janeiro

Your search URL is: https://api.twitter.com/1.1/search/tweets.json?q=geocode=-22.912214,-43.230182,1km&lang=pt&result\_type=recent

`twurl /1.1/search/tweets.json?q=geocode=-22.912214,-43.230182,1km&lang=pt&result_type=recent`  

When you want the most popular tweets of a specific user using a hashtag:

You want: popular Tweets from @Cmdr\_Hadfield mentioning the hashtag #nasa

Your search URL is: https://api.twitter.com/1.1/search/tweets.json?q=from%3ACmdr\_Hadfield%20%23nasa&result\_type=popular

`twurl /1.1/search/tweets.json?q=from%3ACmdr_Hadfield%20%23nasa&result_type=popular`  

**Standard search operators**  

The query can have operators that modify its behavior.  Below are examples that illustrate the available operators in standard search:

| Operator | Finds Tweets... |
| --- | --- |
| watching now | containing both “watching” and “now”. This is the default operator. |
| “happy hour” | containing the exact phrase “happy hour”. |
| love OR hate | containing either “love” or “hate” (or both). |
| beer -root | containing “beer” but not “root”. |
| #haiku | containing the hashtag “haiku”. |
| from:interior | sent from Twitter account “interior”. |
| list:NASA/astronauts-in-space-now | sent from a Twitter account in the NASA list astronauts-in-space-now |
| to:NASA | a Tweet authored in reply to Twitter account “NASA”. |
| @NASA | mentioning Twitter account “NASA”. |
| politics filter:safe | containing “politics” with Tweets marked as potentially sensitive removed. |
| puppy filter:media | containing “puppy” and an image or video. |
| puppy -filter:retweets | containing “puppy”, filtering out retweets |
| puppy filter:native\_video | containing “puppy” and an uploaded video, Amplify video, Periscope, or Vine. |
| puppy filter:periscope | containing “puppy” and a Periscope video URL. |
| puppy filter:vine | containing “puppy” and a Vine. |
| puppy filter:images | containing “puppy” and links identified as photos, including third parties such as Instagram. |
| puppy filter:twimg | containing “puppy” and a pic.twitter.com link representing one or more photos. |
| hilarious filter:links | containing “hilarious” and linking to URL. |
| puppy url:amazon | containing “puppy” and a URL with the word “amazon” anywhere within it. |
| superhero since:2015-12-21 | containing “superhero” and sent since date “2015-12-21” (year-month-day). |
| puppy until:2015-12-21 | containing “puppy” and sent before the date “2015-12-21”. |
| movie -scary :) | containing “movie”, but not “scary”, and with a positive attitude. |
| flight :( | containing “flight” and with a negative attitude. |
| traffic ? | containing “traffic” and asking a question. |

Please, make sure to [URL encode](http://en.wikipedia.org/wiki/URL_encoding) these queries before making the request. There are several online tools to help you to do that, or you can search at twitter.com/search and copy the encoded URL from the browser’s address bar. The table below shows some example mappings from search queries to URL encoded queries:

| Search query | URL encoded query |
| --- | --- |
| #haiku #poetry | %23haiku+%23poetry |
| “happy hour” :) | %22happy%20hour%22%20%3A%29 |

Note that the space character can be represented by “%20” or “+” sign.