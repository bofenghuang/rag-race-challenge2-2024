platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions


## How to use fields and expansions

By default, the Twitter API v2 data objects include a small number of default fields when making a request without the use of the [fields](https://developer.twitter.com/en/docs/twitter-api/fields.html) or [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions.html) parameters. This guide will show you how to use the `fields` and `expansions` query parameters in your request to receive additional objects and fields in your response.

In this guide, we will be requesting several fields in the following Tweet screenshot.  
 

  

As you can see in the screenshot, there are several visible pieces of information related to the Tweet, including the Tweet author, Tweet metrics, created timestamp, video, and video view count. There are also several pieces of data that are not visible within the screenshot, but are still available to request. 

When making a request to the API, the default response is simple, containing only the default Tweet fields (id and text). You will also only receive the primary object that returns with the given endpoint that you are using, and not any of the associated data objects that might relate to the primary object.

This simplicity, along with the fields and expansions parameters, enable you to request only those fields you require, depending on your use case.