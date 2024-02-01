platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/quick-start

## Import the Content Library API client

All calls are made using the Content Library API Client object. You only need to import the Content Library API client once per Jupyter notebook server session.

In code block examples in this documentation, select the R or Python tab to see the corresponding code. You can copy the code and paste it into your notebook.

RPython

    library(contentlibraryapi) 
    client <- ContentLibraryAPIClient$new(version='2')

    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version = "2")