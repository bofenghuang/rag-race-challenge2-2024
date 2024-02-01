platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/rate-limits


### Tips to avoid being rate limited

The tips below are there to help you code defensively and reduce the possibility of being rate limited. Some application features that you may want to provide are simply impossible in light of rate-limiting, especially around the freshness of results. If real-time information is an aim of your application, look into the filtered and sampled stream endpoints.   
 

#### Caching

Store API responses in your application or on your site if you expect a lot of use. For example, don’t try to call the Twitter API on every page load of your website landing page. Instead, call the API infrequently and load the response into a local cache. When users hit your website load the cached version of the results.  
 

#### Prioritize active users

If your site keeps track of many Twitter users (for example, fetching their current status or statistics about their Twitter usage), consider only requesting data for users who have recently signed into your site.  
 

#### Adapt to the search results

If your application monitors a high volume of search terms, query less often for searches that have no results than for those that do. By using a back-off you can keep up to date on queries that are popular but not waste cycles requesting queries that very rarely change. Alternatively, consider using the filtered stream endpoint and filter with your search queries. 

#### Denylist

If an application abuses the rate limits, it will be denied. Denied apps are unable to get a response from the Twitter API. If you or your application has been denied and you think there has been a mistake, you can use our [Platform Support forms](https://support.twitter.com/forms/platform) to request assistance. Please include the following information:

1. Explain why you think your application was denied.
2. If you are no longer being rate limited, describe in detail how you fixed the problem.