platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting

### Best Practices

* When the limit has been reached, stop making API calls. Continuing to make calls will continue to increase your call count, which will increase the time before calls will be successful again.
    
* Spread out queries evenly to avoid traffic spikes.
    
* Use filters to limit the data response size and avoid calls that request overlapping data.
    
* Check the `X-App-Usage` HTTP header to see how close your app is to its limit and when you can resume making calls when the limit has been reached.
    
* If Users are being throttled, be sure your app is not the cause. Reduce the user’s calls or spread the user’s calls more evenly over time.