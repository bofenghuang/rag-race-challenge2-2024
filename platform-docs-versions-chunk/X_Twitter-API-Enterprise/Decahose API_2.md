platform: X
topic: Twitter-API-Enterprise
subtopic: Decahose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Decahose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/overview/decahose


## Decahose stream

[Enterprise](https://developer.twitter.com/en/products/twitter-api/enterprise)  

_This is an enterprise API available within our managed access levels only. To use this API, you must first set up an account with our enterprise sales team. [Learn more](https://developer.twitter.com/en/products/twitter-api/enterprise)_  

The Decahose delivers a 10% random sample of the realtime Twitter Firehose through a streaming connection. This is accomplished via a realtime sampling algorithm which randomly selects the data, while still allowing for the expected low-latency delivery of data as it is sent through the firehose by Twitter.

Below are some of the features available with Decahose:

* **Expanded and enhanced URLs:** - fully unwinds shortened URLs and provides additional metadata (page title and description)
* **Stream partitioning** - 2 partitions, each containing 50% of volume of the Decahose stream
* **Enhanced reliability** - geographic diversity of backend systems

Note: This data is delivered in bulk, and does not support additional filtering (e.g. for keywords).