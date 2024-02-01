platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### Error Messages[¶](#error-messages "Permalink to this headline")

| Code | Message |
| --- | --- |
| 214 | Webhook URL does not meet the requirements. |
| 214 | Too many resources already created. |
| 214 | Webhook URL does not meet the requirements. Invalid CRC token or json response format. |
| 214 | High latency on CRC GET request. Your webhook should respond in less than 3 seconds. |
| 214 | Non-200 response code during CRC GET request (i.e. 404, 500, etc). |

_HTTP 403_

    {
      "errors": [
        {
          "code": 214,
          "message": "Too many resources already created."
        }
      ]
    }

## GET account\_activity/webhooks[¶](#get-account-activity-webhooks "Permalink to this headline")

Returns all URLs and their statuses for the given application.

We mark a URL as invalid if it fails the daily validation check. In order to re-enable the URL, call the update endpoint.