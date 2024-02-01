platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction


## Introduction

The Tweet is one of the primary resources on Twitter. In its simplest form, a Tweet can contain up to 280 characters and can be posted either publicly or privately, depending on an account’s settings. However, a variety of different objects can also be attached to Tweet, including media, a place, polls, and URLs. In addition, most Tweets can be edited for up to 30 minutes after being created. 

While there are a variety of different HTTP, selection, and delivery methods that can deliver, publish, and act upon Tweets, this group of REST endpoints simply returns a Tweet or group of Tweets, specified by a [Tweet ID](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-ids). While simple, these endpoints can be used to receive up-to-date details on a Tweet, verify that a Tweet is available, and examine its edit history. These endpoints are also important tools for managing [compliance events](https://developer.twitter.com/content/developer-twitter/content/developer-twitter/en/docs/twitter-api/enterprise/compliance-firehose-api/overview).

The Tweet lookup endpoint provides edited Tweet metadata. All objects for Tweets created since September 29, 2022, include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history is documented by an array of Tweet IDs, starting with the original ID.

This endpoint will always return the most recent edit, along with any edit history. Any Tweet collected after its 30-minute edit window has expired will represent its final version. To learn more about Edit Tweet metadata, check out the [Edit Tweets fundamentals](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/edit-tweets) page.

These endpoints utilize the GET HTTP method and return one or many [Tweet objects](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/object-model/tweet), which include fields such as the Tweet text, a timestamp from when it was created, and lists and metadata of hashtags, mentions, and photos, and more.   

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/tweets&method=get)