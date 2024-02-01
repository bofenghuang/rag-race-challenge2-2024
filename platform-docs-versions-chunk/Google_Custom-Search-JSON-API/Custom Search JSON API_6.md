platform: Google
topic: Custom-Search-JSON-API
subtopic: Custom Search JSON API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Google_Custom-Search-JSON-API/Custom Search JSON API.md
url: https://developers.google.com/custom-search/v1/introduction

### Identify your application to Google with API key

Custom Search JSON API requires the use of an API key. An API key is a way to identify your client to Google.

* [Programmable Search Engine](https://cse.google.com/) (free edition) users: Get a Key

After you have an API key, your application can append the query parameter `key=yourAPIKey` to all request URLs. The API key is safe for embedding in URLs, it doesn't need any encoding.

## API overview

### API operations

There is only one method to invoke in the Custom Search JSON API:

| Operation | Description | REST HTTP mapping |
| --- | --- | --- |
| [list](https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list) | Returns the requested search results from a Programmable Search Engine. | `GET` |