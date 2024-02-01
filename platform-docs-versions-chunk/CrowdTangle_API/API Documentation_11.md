platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/Links


## [](#get-links)GET /links

Retrieve a set of posts matching a certain link. This will return up to 1000 posts. This endpoint only pulls data from CrowdTangle. To access interaction metrics across the entirety of Facebook, [use this Graph API endpoint.](https://developers.facebook.com/docs/graph-api/reference/v10.0/url)

#### [](#endpoint)Endpoint

`GET https://api.crowdtangle.com/links`

#### [](#parameters)Parameters

Note: **Please use startDate!** Our system works much more quickly (and with much less strain) when it only has to search a subset of dates for your data. If you're looking only for posts in 2019, put in a startDate of 2019-01-01 and our system will know it can ignore years' worth of data. If the URL you're interested in was published yesterday, put that in and it will return very quickly! We're not making startDate mandatory, but please strongly consider using it!

| Parameter | Default | Options | Description |
| --- | --- | --- | --- |
| count | 100 | 1 - 1000 | The number of posts to return. |
| endDate | now | \-  | The latest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd”. |
| includeHistory | `null` (does not include) | `true` | Includes timestep data for growth of each post returned. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle. |
| link | `null` | \-  | The link to query by. Required. |
| includeSummary | `false` | `true`, `false` | Adds a "summary" section with AccountStatistics for each platform that has posted this link. It will look beyond the count requested to summarize across the time searched. Requires a value for startDate. |
| offset | 0   | \>= 0 | The number of posts to offset (generally used for pagination). Pagination links will also be provided in the response. |
| platforms | `null` (i.e., all platforms) | `facebook`, `instagram`, `reddit` (reddit is not currently available for the ACADEMICS vertical) | The platforms from which to retrieve links. This value can be comma-separated. |
| searchField | `null` (i.e., does not support query strings) | `Include_query_strings` | Allows you to search URLs containing query strings. |
| startDate | 0000-00-00 | \-  | The earliest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). |
| sortBy | `date` | `subscriber_count`, `total_interactions` | The method by which to order posts (defaults to the most recent). If `subscriber_count`, a startDate is required. |

#### [](#response)Response

This returns the same response as [/posts](https://github.com/CrowdTangle/API/wiki/Posts). There is no option for pagination on a links request.