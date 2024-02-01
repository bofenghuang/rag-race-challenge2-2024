platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/error-codes

# Error Codes

This page describes the error messages that can be returned by the Instragram Graph API. The sample response below shows an example of code `3600` and subcode `2207004` with the subsequent error codes defined.

### Sample Response

{
  "error": 
    {
      "message": "The image size is too large.",
      "type": "OAuthException",
      "code": 36000,
      "error\_subcode": 2207004,
      "is\_transient": false,
      "error\_user\_title": "Image size too large",
      "error\_user\_msg": "The image is too large to download. It should be less than 8 MiB.",
      "fbtrace\_id": "A6LJylpZRKw2xKLFsAP-cJh"
   }
 }