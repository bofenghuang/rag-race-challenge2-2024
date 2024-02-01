platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/best-practices

## Use Batch Requests for Improved Throughput

Batch requests allow you to make multiple requests to the Graph API using a single HTTP call. For more information on Graph API Batch Requests, review the following:

* [Making multiple API requests](https://developers.facebook.com/docs/graph-api/making-multiple-requests)
    
* [Batch requests documentation](https://developers.facebook.com/docs/reference/ads-api/batch-requests)
    

You can also query for multiple objects by ID using the following syntax:

https://graph.facebook.com/v2.8/?ids=\[id1,id2\]&amp;access\_token=<access\_token>

If you need to query for a specific field:

https://graph.facebook.com/v2.8/?ids=\[id1,id2\]&amp;fields=field1,field2&amp;access\_token=<access\_token>