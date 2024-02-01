platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/console/product

### Settings

The Settings tab allows you to switch the output format of the data in your stream, where multiple format options are supported. To switch the format, just use the radio buttons indicating the different options. The change will take effect upon reconnecting to the stream.  Note that updating this setting will take place immediately on the next request or connection and may break your parser with the new format. 

**Please note:** The recommended setting for getting the most data is "Leave data in the original format" which will return data in the enriched native format [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects.html).  Activity streams format is described [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects.html).