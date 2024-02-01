platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


## Calling the API

The following requirements apply to YouTube Data API requests:

1. Every request must either specify an API key (with the `key` parameter) or provide an OAuth 2.0 token. Your API key is available in the [Developer Console's](https://console.developers.google.com/) **API Access** pane for your project.
    
2. You **must** send an authorization token for every insert, update, and delete request. You must also send an authorization token for any request that retrieves the authenticated user's private data.
    
    In addition, some API methods for retrieving resources may support parameters that require authorization or may contain additional metadata when requests are authorized. For example, a request to retrieve a user's uploaded videos may also contain private videos if the request is authorized by that specific user.
    
3. The API supports the OAuth 2.0 authentication protocol. You can provide an OAuth 2.0 token in either of the following ways:
    
    * Use the `access_token` query parameter like this: `?access_token=``oauth2-token`
    * Use the HTTP `Authorization` header like this: `Authorization: Bearer` `oauth2-token`
    
    Complete instructions for implementing OAuth 2.0 authentication in your application can be found in the [authentication guide](https://developers.google.com/youtube/v3/guides/authentication).