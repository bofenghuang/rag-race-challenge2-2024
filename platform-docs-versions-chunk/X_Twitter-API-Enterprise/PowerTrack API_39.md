platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/faq


###   
Error troubleshooting guide

**Code 429 - Rate Limited: Your app has exceeded the limit on requests to add, delete, or list rules for this stream**

You may be receiving the 429 error code because you are adding or deleting rules too quickly. If you are adding or deleting rules individually, this could add up and exceed the rate limit.

A workaround could be to add or delete several rules at one time.

For example, the below sample cURL command shows you how to delete several rules at once:

    curl -v -X POST -uexample@customer.com "https://gnip-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=delete" -d '{"rule_ids":[734938587381145604,734938587381174273]}"

  
You can learn more about adding or deleting rules and the relevant rate limits [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-rules).  
 

**Code 400**

A 400 error code normally indicates that the server was unable to process the request sent by the client due to poorly formatted JSON.

There are many reasons why this might be the case and you will need to double check the format of your JSON query.

For example, you may need to escape the quotes around the exact phrase match(es) in your rule (as in the example below):

{"rules":\[{"tag":"test1","value":"coffee OR \\"I love coffee\\""}\]}  

**  
Frequent Disconnects - I am experiencing frequent disconnections on the stream and one of the following messages is being returned. Why is this happening?**

`This stream has been disconnected because your client was unable to keep up with us.`

`This stream has been disconnected for operational reasons.`

This kind of error occurs when your stream is not keeping up with the speed at which we are delivering data and your app isn't consuming the data from the stream fast enough.

We allow delivery to get behind for a period of time, and we have a temporary staging buffer amount for each stream on our side; but if you don't catch up, we initiate a disconnect to allow you to reconnect at the current point in time. Please note that this may lead to data loss (for data that is within the buffer at the time of the full buffer disconnect).

These can occur around large spikes in data. Generally, we recommend using a buffer process for consuming data quickly that is separate from the processing process.

You can find out more about optimizing your app to prevent disconnects like this in our articles on [connection](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/disconnections-explained) and on consuming streaming data [here](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data) and [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/high-volume-social-data-events).