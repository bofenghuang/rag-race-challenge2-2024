platform: Facebook
topic: Graph-API
subtopic: Insights Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Insights Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/insights


### Limitations

* Page Insights data is only available on Pages with 100 or more likes.
    
* Most metrics will update once every 24 hours.
    
* Only the last two years of insights data is available.
    
* The values for `period` are calculated from the initial collection of the data point.
    
* "Period" in the tables below only refers to the time frame for which the metric can be accessed in an aggregated form.
    
* The value "lifetime" means the time period for which the insights data is available. By default, this time period is 2 years or shorter.
    
* Only 90 days of insights can be viewed at one time when using the `since` and `until` parameters.
    
* When using `since` and `until`, the `since` date data will be included in the first `value` returned.
    
* Unique impression insights values are calculated independently.
    
    * Total page reach may not always be exactly equal to the sum of paid and non-paid unique values.
        
    * Total page reach may not always be exactly equal to the sum of `viral_unique` and `organic_unique`.
        
    
* When an organic post is boosted, metrics for paid post impressions will include both organic and paid reach.
    
* Demographic metrics, such as age, gender, and location, are only returned if there is data for 100 or more people.
    
* Breakdown metrics for Page post and Page view insights will only return non-zero values.
    
* Several video related metrics only return accurate values if the person requesting the metric is the Page video post creator.
    
* If you reshare a video post of another Page and retrieve its insights, the metrics return a value of 0. Metrics that return 0 for resharers are denoted with "Returns 0 for reshared videos" in their description.
    
* If you neglect to indicate a specific metric or metrics for the endpoint, you will receive an error response with code `3001`, with subcode `1504028` and an error message that states: "No metric was specified to be fetched. Please specify one or more metrics to be fetched and try again."
    
* Interactions on Reels are not included.