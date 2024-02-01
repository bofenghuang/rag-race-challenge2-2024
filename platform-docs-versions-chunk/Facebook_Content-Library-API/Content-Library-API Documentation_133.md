platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/search-quality

### Precision

Only results which exactly match search terms should be returned, excluding, for instance, partial index matches (broom → broomstick) or fuzzy matches (broom → mop). Precision was measured as:

(returned entities matching query exactly) / (all returned entities)

The following table shows the range in average daily precision values across test queries by endpoint from November 8th, 2023 to November 15th, 2023.

| Endpoint | 20th percentile precision | Median precision |
| --- | --- | --- |
| Facebook Page | 99% | 99% |
| Facebook group | 99% | 99% |
| Facebook event | 99% | 99% |
| Facebook post | 99% | 99% |
| Instagram account | 97% | 98% |
| Instagram post | 98% | 99% |