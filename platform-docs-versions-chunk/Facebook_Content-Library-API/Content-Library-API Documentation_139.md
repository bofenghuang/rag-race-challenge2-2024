platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/search-quality


### Factors affecting recall

* False positives in the validation data (denominator of recall equation). In our tests, we have found that the validation dataset may occasionally include non-eligible entities for a given search term due to lags between real-time content visibility and privacy status and their representation in the databases used for validation (see validation data presented earlier). This means that true recall estimates are likely underestimated.
    
* Edge cases or gaps in coverage (true negatives). Indexing data at the scale which Meta operates means that occasionally some content may be imperfectly indexed or missed. Furthermore, internal data models may change, such as when new features for creating and sharing content on platform are added. Thus there may be a lag between when content is available on platform and when it is indexed. As we improve and scale the product, we appreciate any reported cases of missing data from search (see [Appendix](#appendix) on this page for details).
    
* Asynchronous delivery issues. The Meta Content Library and API’s entity loading mechanisms are complex and memory-intensive at scale. Occasionally, the loading process for an entity can become too memory-intensive and fail, resulting in the exclusion of that entity from the returned results.