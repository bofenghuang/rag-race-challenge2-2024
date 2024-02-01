platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-rules


## GET /rules/:rule\_id [¶](#get-rules-rule-id- "Permalink to this headline")

Retrieve an existing rule on the stream by rule ID. Note that all rules are assigned a unique ID by Twitter at the time of creation, rules that are deleted and recreated will receive a different unique rule ID.

#### Request Specifications

|     |     |
| --- | --- |
| **Request Method** | HTTP GET |
| **URL** | Found on the [Console - Products API Help tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/product), and uses the following structure:  <br>  <br>`https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label/rules/:rule_id.json` |
| **Rate Limit** | 60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream's API (POST and GET). |

  

**Example cURL Request**

The following example request demonstrates how to retrieve a rule by rule\_id using cURL on the command line.

    curl -v -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label/rules/:rule_id.json"

  

    curl -v -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/companyname/publishers/twitter/prod/rules/735163830813134848.json"

#### Response

The following responses may be returned by the API for these requests. Non-200 responses should be retried, utilizing an exponential backoff for subsequent requests.

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | The request was successful, and the current rule is returned in JSON format. |
| 400 | Bad Request | Generally relates to poorly formatted JSON, and includes an "Invalid JSON" message in the response. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 429 | Rate Limited | Your app has exceeded the limit on requests to add, delete, or list rules for this stream. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) contact support. |

  

**Example Response**

    HTTP/1.1 200 OK
    {
        "rules": [{
            "value": "from:twitterdev",
            "tag": "tweetsfromtwitterdev123",
            "id": 735163830813134848
            "id_str":"735163830813134848"
        }],
        "sent": "2016-06-01T15:52:37.341Z"
    }