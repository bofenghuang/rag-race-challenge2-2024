platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/search-quality

### Factors affecting representativeness

* Representativeness issues generally stem from the same factors affecting recall. In these cases there is a population of entities which are either (a) not returned by the Meta Content Library API due to gaps in indexing / delivery, or (b) incorrectly included in the validation dataset adding noise to the calculation. If these groups of entities have similar properties along the data dimensions tested they can influence the representativeness metrics
    
* The per-query bias test uses a probabilistic statistical test which uses an alpha = 0.05 cutoff by convention. Thus for each test term there is a 5% probability that the test will be a false positive (Type I error rate).
    

## Appendix