platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/search-quality


### Factors affecting precision

* String-matching used to validate precision is unable to approximate tokenization rules. Precision is checked using basic regular expression searches with strict definitions of word boundaries. However tokenization may be more flexible, especially with different language localizations, text involving unicode, URLs, and other patterns. The existence of these edge cases means that precision will be under-estimated to some extent.
    
* The search term was tokenized in a context-specific way. Occasionally words with unicode symbols, non-English characters, accent marks or URLs may be tokenized in a form that differs from its presented value. For instance, the content with the French word `congrégation` may be returned for a query on the English word `congregation`, despite the literal difference between the acute accented e and its English counterpart.
    
* The index has matched text not returned by the Meta Content Library or API. In some cases, content with complex, nested data models such as reshares may contain text fields that are tokenized and indexed but not returned by the Meta Content Library or API. We appreciate user feedback identifying such cases (see [Appendix](#appendix) on this page for details).
    
* For the Facebook posts endpoint, there is a known issue involving post reshare text being indexed but not returned in the Meta Content Library API. These posts may either have no visible text (since they are reshares), or the text returned may not contain any mention of the query term. We are exploring this issue further.