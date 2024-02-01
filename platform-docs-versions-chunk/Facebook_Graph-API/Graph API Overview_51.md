platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting

### Best Practices

* When the limit has been reached, stop making API calls. Continuing to make calls will continue to increase your call count, which will increase the time before calls will be successful again.
* Check the `X-Business-Use-Case-Usage` HTTP header to see how close your ad account is to its limit and when you can resume making calls.
* Verify the error code and API endpoint to confirm the throttling type.
* Switch to other ad accounts and come back to this account later.
* It is better to create a new ad than to change existing ones.
* Spread out queries evenly between two time intervals to avoid sending traffic in spikes.
* Use filters to limit the data response size and avoid calls that request overlapping data.