platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/error-handling


## Error Responses

The following represents a common error response resulting from a failed API request:

{
  "error": {
    "message": "Message describing the error", 
    "type": "OAuthException", 
    "code": 190,
    "error\_subcode": 460,
    "error\_user\_title": "A title",
    "error\_user\_msg": "A message",
    "fbtrace\_id": "EJplcsCHuLu"
  }
}

* `message`: A human-readable description of the error.
* `code`: An error code. Common values are listed below, along with common recovery tactics.
* `error_subcode`: Additional information about the error. Common values are listed below.
* `error_user_msg`: The message to display to the user. The language of the message is based on the locale of the API request.
* `error_user_title`: The title of the dialog, if shown. The language of the message is based on the locale of the API request.
* `fbtrace_id`: Internal support identifier. When [reporting a bug](https://developers.facebook.com/bugs/) related to a Graph API call, include the `fbtrace_id` to help us find log data for debugging. However, this ID will expire shortly. To help the support team reproduce your issue, please attach a saved [graph explorer session](https://developers.facebook.com/tools/explorer/).