platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/search-quality


### Other languages

We used the same methodology to measure the search quality of the queries in Arabic, German and Hindi. These languages were selected based on the language features that the team believe are most likely to impact search quality. The features that the team considered are diacritics (such as accents), non-Roman characters, and right-to-left. We also wanted to cover at least one non-English European language.

Based on the analysis, we learned:

* The overall search quality of all the new languages is about the same level as English single keywords.
    
* The precision is over 95% for all endpoints in new languages.
    
* Since the search quality is reasonable for these languages, we expect to see very similar results for most other languages too.
    

The following table shows all metric values across test queries by language and endpoint from November 8th, 2023 to November 15th, 2023. Representativeness is an average across all dimensions that are mentioned in the representativeness section.

| Language | Endpoint | Recall | Precision | Representativeness - paired t-test | Representativeness - Welch t-test |
| --- | --- | --- | --- | --- | --- |
| Arabic | Facebook Page | 96% | 99% | 93% | 99% |
| Arabic | Facebook group | 92% | 99% | 41% | 61% |
| Arabic | Facebook event | 82% | 99% | 80% | 97% |
| Arabic | Facebook post | 91  | 99% | 70% | 94% |
| Arabic | Instagram account | 93% | 99% | 87% | 91% |
| Arabic | Instagram post | 80% | 99% | 85% | 97% |
| German | Facebook Page | 97% | 99% | 96% | 99% |
| German | Facebook group | 95% | 99% | 76% | 95% |
| German | Facebook event | 95% | 99% | 67% | 94% |
| German | Facebook post | 88  | 99% | 73% | 96% |
| German | Instagram account | 99% | 99% | 95% | 99% |
| German | Instagram post | 91% | 98% | 88% | 99% |
| Hindi | Facebook Page | 96% | 99% | 93% | 99% |
| Hindi | Facebook group | 96% | 99% | 39% | 61% |
| Hindi | Facebook event | 87% | 99% | 77% | 96% |
| Hindi | Facebook post | 92  | 99% | 71% | 95% |
| Hindi | Instagram account | 97% | 99% | 94% | 100% |
| Hindi | Instagram post | 73% | 99% | 80% | 96% |

We are also aware of a few limitations that our system has for other languages. The limitations are as follows:

* Meta Content Library API does not read any keywords with “ß” in German or semi-space (half-space) in Arabic.
    
* In Arabic, a word can be written with and without diacritics. Content Library API can only find the exact match for each form. Thus, if a researcher wants to find all posts related to that keyword, they have to search all forms of those keywords to get full results. For example, if a researcher need to find all post related to term مهاجر, they need to search مُهاجِر or مُهاجر or مهاجِر or مهاجر to get all the results.