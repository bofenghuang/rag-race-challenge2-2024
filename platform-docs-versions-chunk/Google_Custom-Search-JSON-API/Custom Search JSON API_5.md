platform: Google
topic: Custom-Search-JSON-API
subtopic: Custom Search JSON API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Google_Custom-Search-JSON-API/Custom Search JSON API.md
url: https://developers.google.com/custom-search/v1/introduction

This document will help you to get familiar with Custom Search JSON API and its usage.

## Before you start

### Create Programmable Search Engine

By calling the API user issues requests against an existing instance of Programmable Search Engine. Therefore, before using the API, you need to create one in the [Control Panel](https://programmablesearchengine.google.com/controlpanel/create) . Follow the [tutorial](https://developers.google.com/custom-search/docs/tutorial/creatingcse) to learn more about different configuration options. Once it is created, you can find the **Search Engine ID** in the **Overview** page's **Basic** section. This is the `cx` parameter used by the API.