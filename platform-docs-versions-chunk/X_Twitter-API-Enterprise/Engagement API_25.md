platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/guides/interpreting-metrics


### Video metrics

There are a couple of different metrics that represent impressions of media within Twitter. The first of which is our video views metric, which relies on the MRC standard of 50% of the video in view for at least two seconds. The second is Media Views, that includes all views (autoplay and click) of your media counted across videos, vines, gifs, and images.

The video views metric is available for owned Tweets via the /28hour and /historical endpoints, as well as for all unowned Tweets via the /totals endpoint. 

While the video views metric within the Twitter user interface is using the same MRC standard, please note that you may see a discrepancy between the video views metric displayed in the Twitter owned and operated platforms (mobile app and website) and the number that you receive via the different Engagement API endpoints.

* The video views provided by the /totals endpoint and the Twitter user interface will display the video view aggregated across all Tweets in which the given video has been posted. That means that the metric delivered via /totals and displayed in the Twitter UI includes the combined views from any instance where the video has been Retweeted or reposted in separate Tweets.
* The video views provided by the /28hour and /historical Engagement API endpoints will just include those views generated by the specific Tweet for which you are pulling metrics.   
     

Please note that we do not deliver video views for Tweets that are older than 1800 days. Instead, we deliver an object that lists the Tweets that are older than 1800 days. You will still receive all other metrics for your requested Tweets in a separate object. Here is an example response:

      `{   "unsupported_for_video_views_tweet_ids": [     "479311209565413376",     "477139122520219648"   ],   "grouping name": {     "479311209565413376": {       "favorites": "69",       "impressions": "1692",       "retweets": "142",       "video_views": "0"     },     "477139122520219648": {       "favorites": "10",       "impressions": "1023",       "retweets": "6",       "video_views": "0"     },     "1397568983931392004": {       "favorites": "268",       "impressions": "26803",       "retweets": "56",       "video_views": "17902"     }   } }`
    

The Media Views metric is only available for owned Tweets with the /28hour and /historical endpoints.