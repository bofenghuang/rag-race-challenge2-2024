platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/search-quality

### Recall

In principle, entities should be returned when (a) there is an exact match with search term(s), (b) the content is eligible to be retrieved, and (c) the total corpus of matching results does not exceed the technical query limit of 100,000 results.

We measured recall as follows:

(entities returned) ∩ (entities expected) / (entities expected)

The following table shows the average of daily recall values across test queries from November 8th, 2023 to November 15th, 2023.

| Endpoint | 20th percentile recall | Median |
| --- | --- | --- |
| Facebook Page | 96% | 98% |
| Facebook group | 93% | 96% |
| Facebook event | 90% | 93% |
| Facebook post | 85% | 92% |
| Instagram account | 98% | 99% |
| Instagram post | 90% | 94% |