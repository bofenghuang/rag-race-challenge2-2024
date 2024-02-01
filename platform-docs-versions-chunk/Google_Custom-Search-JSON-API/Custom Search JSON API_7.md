platform: Google
topic: Custom-Search-JSON-API
subtopic: Custom Search JSON API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Google_Custom-Search-JSON-API/Custom Search JSON API.md
url: https://developers.google.com/custom-search/v1/introduction


### API data model

The result of a search query to the Custom Search JSON API is a JSON object that includes three types of data:

* Metadata describing the requested search (and, possibly, related search requests)
* Metadata describing the Programmable Search Engine
* Search results

See the Response data section of [Using REST](https://developers.google.com/custom-search/v1/using_rest#response_data) for more details.

The data model is based on the OpenSearch 1.1 Specification. In addition to the standard OpenSearch properties, the Custom Search JSON API defines two custom properties and two custom query roles:

* Custom properties
    * `cx`: The identifier of the Programmable Search Engine.
    * `safe`: A description of the safe search level for filtering the returned results.
* Custom query roles
    * `nextPage`: A role that indicates the query can be used to access the next logical page of results, if any.
    * `previousPage`: A role that indicates the query can be used to access the previous logical page of results, if any.