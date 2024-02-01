platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


## FAQ

#### What do we consider an API call?

All calls count towards the rate limits, not just individual API requests. For example, you can make a single API request specifying multiple IDs, but each ID counts as one API call.

The following table illustrates this concept.

| Example Request(s) | Number of API Calls |
| --- | --- |
| `GET https://graph.facebook.com/photos?ids=4`<br><br>`GET https://graph.facebook.com/photos?ids=5`<br><br>`GET https://graph.facebook.com/photos?ids=6` | 3   |
| `GET https://graph.facebook.com/photos?ids=4,5,6` | 3   |

We strongly recommend specifying multiple IDs in one API request when possible, as this improves performance of your API responses.

#### I'm building a scraper, is there anything else I should worry about?

If you are building a service that scrapes data, please read [our scraping terms](https://www.facebook.com/apps/site_scraping_tos_terms.php?hc_location=ufi).

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)