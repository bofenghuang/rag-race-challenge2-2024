platform: Google
topic: Custom-Search-JSON-API
subtopic: Custom Search JSON API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Google_Custom-Search-JSON-API/Custom Search JSON API.md
url: https://developers.google.com/custom-search/v1/site_restricted_api

## About the Custom Search Site Restricted JSON API

If your Programmable Search Engine is restricted to only searching specific sites (10 or fewer), you can use the Custom Search Site Restricted JSON API. This API is similar to the Custom Search JSON API except this version has no daily query limit. To use this version, confirm that you see 10 or fewer sites to search in the “Sites to Search” section of your Programmable Search Engine control panel, there are no global top level domain patterns, and that “Search the entire web” is set to OFF.

When using the Custom Search Site Restricted JSON API endpoint, be mindful that if your Programmable Search Engine configuration is changed so that it does not conform with the site restriction rules above, the Custom Search Site Restricted JSON API may not return the expected results.