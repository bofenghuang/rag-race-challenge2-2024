platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/pagination?context=linkedin%2Fcontext

# Pagination

API calls that return a large number of entities are broken up into multiple pages of results. You might need to make multiple API calls with slightly varied paging parameters to iteratively collect all the data you are trying to gather.

Use the following query parameters to paginate through results:

## Parameters

| Name | Description | Default |
| --- | --- | --- |
| start | The index of the first item you want results for. | 0   |
| count | The number of items you want included on each page of results. There could be fewer items remaining than the value you specify. | 10  |

To paginate through results, begin with a `start` value of 0 and a `count` value of N. To get the next page, set `start` value to N, while the `count` value stays the same. Subsequent pages start at 2N, 3N, 4N, and so on.