platform: Google
topic: Custom-Search-JSON-API
subtopic: Custom Search JSON API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Google_Custom-Search-JSON-API/Custom Search JSON API.md
url: https://developers.google.com/custom-search/v1/using_rest


## Making a request

REST, or [Representational State Transfer](http://en.wikipedia.org/wiki/Representational_State_Transfer), in the Custom Search JSON API is somewhat different from traditional REST. Instead of providing access to resources, the API provides access to a service. As a result, the API provides a single URI that acts as the service endpoint.

You can retrieve results for a particular search by sending an HTTP `GET` request to its URI. You pass in the details of the search request as query parameters. The format for the Custom Search JSON API URI is:

    https://www.googleapis.com/customsearch/v1?[parameters]
    

Three query `[parameters]` are required with each search request:

* **API key** - Use the `key` query parameter to [identify your application](https://developers.google.com/custom-search/json-api/v1/introduction#identify_your_application_to_google_with_api_key).
* **Programmable Search Engine ID** - Use `cx` to specify the Programmable Search Engine you want to use to perform this search. The search engine must be created with the [Control Panel](https://cse.google.com/all) Note: The Search Engine ID (cx) can be of different format (e.g. 8ac1ab64606d234f1)
    
* **Search query** - Use the `q` query parameter to specify your search expression.
    

All other [query parameters](https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list) are optional.

Here is an example of a request which searches a test Programmable Search Engine for _lectures_:

GET https://www.googleapis.com/customsearch/v1?key=INSERT\_YOUR\_API\_KEY&cx=017576662512468239146:omuauf\_lfve&q=lectures

**Note:** The limit on the length of the search request should be within 2048 characters.