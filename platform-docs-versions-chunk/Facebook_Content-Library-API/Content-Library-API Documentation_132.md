platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/search-quality

### Rank recall

Results which represent the _top N_ results ordered by creation time or views should also be complete. For Meta Content Library, which returns a truncated list of ranked results, we generated a _ranked_ version of recall which is calculated as follows:

(top N entities) ∩ (top N expected entities) / (top N expected entities)

The following table shows the average of daily recall values for the top 1000 results ranked by creation time and view across test queries from November 8th, 2023 to November 15th, 2023.

| Endpoint | 20th percentile ranked recall | Median ranked recall |
| --- | --- | --- |
| Facebook post (ranked by creation time) | 86% | 92% |
| Instagram post (ranked by creation time) | 64% | 75% |
| Facebook post (ranked by view) | 52% | 63% |
| Instagram post (ranked by view) | 62% | 73% |