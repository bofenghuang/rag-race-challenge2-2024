platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-rules


## POST /rules \_method=get [¶](#post-rules--method-get- "Permalink to this headline")

Retrieves requested existing rules by list of rule IDs currently on a stream.

#### Request Specifications

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | Found on the API Help page, and uses the following structure:  <br>  <br>`https://data-api.twitter.com/rules/powertrack/accounts/{gnip_account_name}/publishers/twitter/{stream_label}.json?_method=get` |
| **Character Encoding** | UTF-8 |
| **Request Body Format** | JSON |
| **Request Body Size Limit** | 5 MB |
| **Rate Limit** | 60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream's API (POST and GET). |
| **Compression** | Gzip compression is supported, but not required for these requests. |

  

**Example curl Request**

The following example request demonstrates how to add rules using cURL on the command line.

    curl -v -X POST -uexample@customer.com \
    "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=get" \
    -d '{"rule_ids":[734938587381145604,734938587381174273]}"

  

#### Response

The following responses may be returned by the API for these requests. Non-200 responses should be retried, utilizing an exponential backoff for subsequent requests.

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | The request was successful, and the current ruleset is returned in JSON format. |
| 400 | Bad Request | Generally relates to poorly formatted JSON, and includes an "Invalid JSON" message in the response. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 429 | Rate Limited | Your app has exceeded the limit on requests to add, delete, or list rules for this stream. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) contact support. |

  

**Example Response**

    HTTP/1.1 200 OK
    {
        "rules": [{
            "value": "from:furiouscamper",
            "tag": null,
            "id": 734938587381145604
        }, {
            "value": "fish 🐟",
            "tag": null,
            "id": 734938587381174273
        }],
        "sent": "2016-06-01T15:52:37.341Z"
    }

  

        {
        "error": {
            "message": "Invalid JSON. The body must be in the format {\"rules\":[{\"value\":\"rule1\", \"tag\":\"tag1\"}, {\"value\":\"rule2\"}]} or {\"rule_ids\": [rule_id1, rule_id2, rule_id3, rule_id4, rule_id5]}",
            "sent": "2013-08-16T00:50:00+00:00"
        }
    }