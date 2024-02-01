platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines


### Using since\_id for the greatest efficiency

Applications which process a timeline, wait some quantity of time, and then need to process new Tweets which have been added since the last time the timeline was processed can make one more optimization using the since\_id parameter.

Consider the previous example where Tweets 1 through 10 were processed. Now imagine that Tweets 11 through 18 were added to the timeline since the processing in the previous example began. An inefficient approach to process the new Tweets would be to iterate from the start of the list until Tweet 10 appeared. This causes two Tweets which have already been processed to be returned again.

This problem is avoided by setting the since\_id parameter to the greatest ID of all the Tweets your application has already processed. Unlike max\_id the since\_id parameter is not inclusive, so it is not necessary to adjust the ID in any way. As shown in the following image, Twitter will only return Tweets with IDs higher than the value passed for since\_id.

Applications which use both the max\_id and since\_id parameters correctly minimize the amount of redundant data they fetch and process, while retaining the ability to iterate over the entire available contents of a timeline.