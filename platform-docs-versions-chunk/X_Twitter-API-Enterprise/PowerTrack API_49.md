platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-rules


## POST /validation [¶](#post-validation- "Permalink to this headline")

Validates PowerTrack rules.

**Note:** Using this endpoint will not impact your PowerTrack streams.

#### Request Specifications

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | Found on the API Help page in console, and uses the following structure:  <br>  <br>`https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label/validation.json` |
| **Character Encoding** | UTF-8 |
| **Request Body Format** | JSON |
| **Request Body Size Limit** | 5 MB |
| **Rate Limit** | 60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream's API (POST and GET). |

  

**Example curl Request**

The following example request demonstrates how to add rules using cURL on the command line.

    curl --compressed -v -uexample@customer.com \
    "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label/validation.json" \
    -d '{
        "rules": [{
            "value": "Pizza OR 🍕 OR \"🍕\" sample:100"
        }, {
            "value": "from:contains:heart"
        }, {
            "value": "fish AND bird"
        }, {
            "value": "(((\"#quotedhashtag\""
        }, {
            "value": "bounding_box:[-71.199636,42.230046,-70.979909,42.398619]"
        }, {
            "value": "from:jack"
        }]
    }'

#### Response

The following responses may be returned by the API for these requests. Non-200 responses should be retried, utilizing an exponential backoff for subsequent requests.

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | The request was successful, and the rule validation result is returned. |
| 400 | Bad Request | Generally relates to poorly formatted JSON, and includes an "Invalid JSON" message in the response. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 429 | Rate Limited | Your app has exceeded the limit on requests to add, delete, or list rules for this stream. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/), contact support. |

  

**Example Response**

This response indicates that one rule is valid and five are not valid. For rules that are not valid, there is a 'message' field explaining why the rule is not valid.

    HTTP/1.1 200 OK
    {
        "summary": {
            "valid": 1,
            "not_valid": 5
        },
        "detail": [{
            "rule": {
                "value": "from:jack",
                "tag": null
            },
            "valid": true
        }, {
            "rule": {
                "value": "Pizza OR 🍕 OR \"🍕\" sample:100",
                "tag": null
            },
            "valid": false,
            "message": "The sample operator cannot be used with an OR. To use the sample operator with an OR in the rule, the ORed clauses must be grouped together with parenthesis.  For example, to get 10% of activites that have term1 or term2, the rule should be (excluding the single quotes) '(term1 OR term2) sample:10' (at position 21)\n"
        }, {
            "rule": {
                "value": "from:contains:heart",
                "tag": null
            },
            "valid": false,
            "message": "Cannot parse rule at ':' (position 14)\n"
        }, {
            "rule": {
                "value": "fish AND bird",
                "tag": null
            },
            "valid": false,
            "message": "Ambiguous use of and as a keyword. Use a space to logically join two clauses, or \"and\" to find occurrences of and in text (at position 6)\n"
        }, {
            "rule": {
                "value": "(((\"#quotedhashtag\"",
                "tag": null
            },
            "valid": false,
            "message": "mismatched input 'EOF' expecting ')' (at position 20)\n\n"
        }, {
            "rule": {
                "value": "bounding_box:[-71.199636,42.230046,-70.979909,42.398619]",
                "tag": null
            },
            "valid": false,
            "message": "Cannot parse rule at '71.199636,42.230046,-70.979909,42.398619' (position 16)\n"
        }],
        "sent": "2017-03-16T02:33:01.827Z"
    }