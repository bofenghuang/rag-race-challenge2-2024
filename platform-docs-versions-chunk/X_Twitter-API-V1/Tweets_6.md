platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/guides/standard-operators


## Integrating with standard search

Standard

One way to start testing searches for Tweets, is to first use the twitter.com/search UI, and build a query there.  There is not complete parity or completeness between the web interface and the standard search API, but this can help to get started.

Using the operators below and the search/tweets API, you can iterate on the result by adding more specificity, or negations to get the desired results.  As you get a satisfactory result set, the URL loaded in the browser will contain the proper query syntax that can be reused in the API endpoint. 

Here’s an example:  

* We want to search for Tweets referencing _TwitterDev_, the word _new_ and the word _premium_. First, we run the search on twitter.com/search: https://twitter.com/search?q=twitterdev%20new%20premium
* Replace “https://twitter.com/search” with “https://api.twitter.com/1.1/search/tweets.json” and you will get: https://api.twitter.com/1.1/search/tweets.json?q=twitterdev%20new%20premium
* Execute this URL to do the search in the API.  

Here's an example twurl command: `twurl /1.1/search/tweets.json?q=twitterdev%20new%20premium`

And the result:

{
	"statuses": \[{
				"created\_at": "Thu Feb 01 16:40:07 +0000 2018",
				"id": 959104084845453312,
				"id\_str": "959104084845453312",
				"text": "RT @TwitterAPI: New year, new access for our developer community! \\ud83c\\udf89\\n\\nToday, we\\u2019re launching our premium Search Tweets: Full-archive endpoin\\u2026",
				"truncated": false,
				"entities": {
					"hashtags": \[\],
					"symbols": \[\],
					"user\_mentions": \[{
						"screen\_name": "TwitterAPI",
						"name": "Twitter API",
						"id": 6253282,
						"id\_str": "6253282",
						"indices": \[3, 14\]
					}\],
					"urls": \[\]
				},
				"metadata": {
					"iso\_language\_code": "en",
					"result\_type": "recent"
				},
				"source": "\\u003ca href=\\"http:\\/\\/twitter.com\\" rel=\\"nofollow\\"\\u003eTwitter Web Client\\u003c\\/a\\u003e",
				"in\_reply\_to\_status\_id": null,
				"in\_reply\_to\_status\_id\_str": null,
				"in\_reply\_to\_user\_id": null,
				"in\_reply\_to\_user\_id\_str": null,
				"in\_reply\_to\_screen\_name": null,
				"user": {
					"id": 2244994945,
					"id\_str": "2244994945",
					"name": "Twitter Dev",
					"screen\_name": "TwitterDev",
					"location": "Internet",
					"description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\\/\\/t.co\\/mGHnxZU8c1 \\u2328\\ufe0f #TapIntoTwitter",
					"url": "https:\\/\\/t.co\\/FGl7VOULyL",
					"entities": {
						"u.......