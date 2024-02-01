platform: Google
topic: Custom-Search-JSON-API
subtopic: Custom Search JSON API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Google_Custom-Search-JSON-API/Custom Search JSON API.md
url: https://developers.google.com/custom-search/v1/using_rest

### Search engine metadata

The `context` property has metadata describing the search engine that performed the search query. It includes the name of the search engine, and any [facet objects](https://developers.google.com/custom-search/docs/refinements#create) it provides for refining a search.

### Search results

The `items` array contains the actual search results. The search results include the URL, title and text snippets that describe the result. In addition, they can contain [rich snippet](https://developers.google.com/custom-search/docs/snippets) information, if applicable.

If the search results include a `promotions` property, it contains a set of [promotions](https://developers.google.com/custom-search/docs/promotions#sl).