platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction


## Introduction

Searching for Tweets is an important feature used to surface Twitter conversations about a specific topic or event. While this functionality is present in Twitter, these endpoints provide greater flexibility and power when filtering for and ingesting Tweets so you can find relevant data for your research more easily; build out near-real-time ‘listening’ applications; or generally explore, analyze, and/or act upon Tweets related to a topic of interest. 

We offer two endpoints that allow you to search for Tweets: Recent search and full-archive search. Both of these REST endpoints share a common design and features, including their use of a single search query to filter for Tweets around a specific topic. These search queries are created with a set of operators that match on Tweet and user attributes, such as message keywords, hashtags, and URLs. Operators can be combined into queries with boolean logic and parentheses to help refine the queries matching behavior. 

Both the recent search and the full-archive search endpoints provide edited Tweet metadata. All objects for Tweets created since September 29, 2022, include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history is documented by an array of Tweet IDs, starting with the original ID.

These endpoints will always return the most recent edit, along with any edit history. Any Tweet collected after its 30-minute edit window will represent its final version. To learn more about Edit Tweet metadata, check out the [Edit Tweets fundamentals](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/edit-tweets) page.

Once you’ve set up your query and start receiving Tweets, these endpoints support navigating the results both by time and Tweet ID ranges. This is designed to support two common use cases: 

* **Get historical**: Requests are for a period of interest, with no focus on the real-time nature of the data. A single request is made, and all matching data is delivered using pagination as needed. This is the default mode for Search Tweets.
* **Polling** or **listening**: Requests are made in a "any new Tweets since my last request?" mode. Requests are made on a continual basis, and typically there is a use case focused on near real-time 'listening' for Tweets of interest.  
     

Many operators and query limits are exclusive to [Enterprise access](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level), meaning that you must use keys and tokens from an App within a [Project](https://developer.twitter.com/en/docs/projects) with Enterprise access to utilize the additional functionality. You can learn more about this in the endpoint sections below.

Both the recent search and the full-archive search endpoints returned Tweets contribute to the monthly [Tweet cap](https://developer.twitter.com/en/docs/twitter-api/tweet-caps).

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).