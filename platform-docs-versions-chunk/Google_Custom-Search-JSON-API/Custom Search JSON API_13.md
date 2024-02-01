platform: Google
topic: Custom-Search-JSON-API
subtopic: Custom Search JSON API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Google_Custom-Search-JSON-API/Custom Search JSON API.md
url: https://developers.google.com/custom-search/v1/using_rest


### Search request metadata

The search metadata includes:

* `url` property, which has information about the [OpenSearch template](http://www.opensearch.org/Specifications/%0AOpenSearch/1.1#OpenSearch_URL_template_syntax) used for the results returned in this request.
* `queries` property, which is an array of objects describing the characteristics of possible searches. The name of each object in the array is either the name of an [OpenSearch query role](http://www.opensearch.org/Specifications/OpenSearch/1.1#Local_role_values) or one of the two custom roles defined by this API: `previousPage` and `nextPage` . Possible query role objects include:
    * `request`: Metadata describing the query for the current set of results.
        * This role is always present in the response.
        * It is always an array with just one element.
        * `nextPage`: Metadata describing the query to use for the next page of results.
            * This role is not present if the current results are the last page. **Note:** This API returns up to the first 100 results only.
            * When present, it is always a array with just one element.
    * `previousPage`: Metadata describing the query to use for the previous page of results.
        * Not present if the current results are the first page.
        * When present, it is always a array with just one element.