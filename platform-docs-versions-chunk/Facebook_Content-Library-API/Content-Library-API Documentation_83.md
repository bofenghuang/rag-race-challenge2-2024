platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/adv-search

# Advanced search guidelines

Meta Content Library and API have a search functionality that supports AND, OR, and NOT operators. Query strings are passed as the `q` parameter as in this example (select the tab for the language of your choice):

RPython

    response <- client$search_posts(q=“dogs | cats & pets”)

    response = client.search_posts(q=“dogs | cats & pets”)