platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-ig-accounts

# Guide to Instagram accounts data

You can perform searches for Instagram creator, business, and certain personal accounts by calling the Meta Content Library API client's `search_ig_accounts()` method.

For personal accounts, only those that have account privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT07vXMxIWruG0ty60Iv36MZ5K8q6gRPHWRWmm2xDePX7SLoU8VJzyP4TuwlkRVspGtLV6Qwya5mtIvQQgnNuRRhvwhmWdnsu_HyPpimv4rmdDADR1W8PwHuXNL3KZW7PBWKpKs97lG8k5uf), and have either a [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT2-FmhBrURs62X-uOb58Y5x96_t6l4vX_YcMm3Vtcq7oMh9Us1f-QY8RpAR_3I39ZARALrVF5l9RsCbBDe7B0FAPeqpR7k8Nl_HrKBAKVQQgJWf_KTPaYXQ43zD7yUzGmEmbSFCN0k3f6m9) or 50,000 or more followers are included. This document describes the \`search\_ig\_accounts()\` method and its syntax and parameters, and shows how to perform basic queries using the method.

All of the examples in this document assume you have already created a Python or R Jupyter notebook and have created a client object. See [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-account) for detailed information about the fields that are available on an Instagram account node.