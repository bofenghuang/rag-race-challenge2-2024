platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/Pagination

# Pagination

### [](#pagination)Pagination

An Pagination object offers API endpoints to call for the next or previous pages. The CrowdTangle API simply uses counts and offsets to paginate, so constructing your own pagination URLs is simple as well.

#### [](#properties)Properties

| Property | Type | Descriptions |
| --- | --- | --- |
| nextPage | string | The API URL to call for the next page, if available. |
| previousPage | string | The API URL to call for the previous page, if available. |