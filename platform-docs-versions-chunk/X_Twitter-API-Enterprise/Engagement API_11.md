platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/guides/dev-getting-started-engagement-api


## Next steps

* Read through the [Engagement API's Overview page](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview) for general information about the product.
* Figure out [which Engagement API endpoint is right for you](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/selecting-engagement-endpoint).  
    
* Learn more about some of the recent changes to the Engagement API [here](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/understanding-recent-changes-to-eapi-metrics).
* Check out our [API references](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement) to learn more about how to programmatically access Tweet engagement metrics.
* [Key Characteristics](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/guides/key-characteristics.html) - serves as a one-page developer’s checklist of API features and details.  
      
    
* Explore our sample code:
    * [Example Ruby client](https://github.com/twitterdev/engagement-api-client-ruby). This example Engagement API Client helps manage the process of generating engagement metadata for large Tweet collections. The client has a helper feature that can surface ['Top Tweets.'](https://github.com/twitterdev/engagement-api-client-ruby#top-tweets) As engagement metrics are retrieved, on a Tweet-by-Tweet basis, this client maintains a list of 'Top Tweets' with the highest levels of engagement. For example, if you are processing 100,000 Tweets, it can compile the top 10 for Retweets or any other available metric. Project repository includes an extensive README, which serves as an additional source of ‘getting started’ material and orientation for how the API works.
    * [Example Python client](https://github.com/jeffakolb/Gnip-Insights-Interface). This example illustrating using OAuth with the Requests package. The client also has an aggregating function for the /historical endpoint that combines API results over an arbitrary time period longer than 28 days.