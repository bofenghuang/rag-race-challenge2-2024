platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search


## Methods [¶](#methods- "Permalink to this headline")

The base URI for enterprise search is `https://gnip-api.twitter.com/search/`.

| Method | Description |
| --- | --- |
| [POST /search/:product/accounts/:account\_name/:label](#SearchRequests) | Retrieve Tweets from the past 30 days that match the specified PowerTrack rule. |
| [POST /search/:product/accounts/:account\_name/:label/counts](#CountRequests) | Retrieve the number of Tweets from the past 30 days that match the specified PowerTrack rule. |

Where:

* `:product` indicates the search endpoint you are making requests to, either `30day` or `fullarchive`.
* `:account_name` is the (case-sensitive) name associated with your account, as displayed at console.gnip.com
* `:label` is the (case-sensitive) label associated with your search endpoint, as displayed at console.gnip.com

For example, if the TwitterDev account has the 30-Day search product with a label of 'prod' (short for production), the search endpoints would be:

* Data endpoint: [https://gnip-api.twitter.com/search/30day/accounts/TwitterDev/prod.json](https://gnip-api.twitter.com/search/30day/accounts/TwitterDev/prod.json)
* Counts endpoint: [https://gnip-api.twitter.com/search/30day/accounts/TwitterDev/prod/counts.json](https://gnip-api.twitter.com/search/30day/accounts/TwitterDev/prod/counts.json)

Your complete enterprise search API endpoint is displayed at [https://console.gnip.com](https://console.gnip.com/).

Below there are several example requests using a simple HTTP utility called curl. These examples use URLs with `:product`, `:account_name`, and `:label`. To use these examples, be sure to update the URLs with your details.