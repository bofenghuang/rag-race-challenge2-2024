platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-rules


## POST /rules \_method=delete [¶](#post-rules--method-delete- "Permalink to this headline")

Deletes requested existing rules by list of rule values or rule IDs currently on a stream.

#### Request Specifications

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **Authentication** | Basic Authentication. Your login credentials must be included in the header of the request. |
| **Content Type** | "application/json". The request should specify this as the "Content-type". |
| **URL** | Found on the API Help page, and uses the following structure:  <br>  <br>`https://data-api.twitter.com/rules/powertrack/accounts/{gnip_account_name}/publishers/twitter/{stream_label}.json?_method=delete` |
| **Character Encoding** | UTF-8 |
| **Request Body Format** | JSON |
| **Request Body Size Limit** | 5 MB |
| **Rate Limit** | 60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream's API (POST and GET). |

  

#### Request Body Content

Your request should provide rule data in the following formats:

    Content-type: "application/json"
    {
        "rules":
        [
            {"value":"rule1"},
            {"value":"rule2"}
        ]
    }

    Content-type: "application/json"
    {
        "rule_ids":
        [
            734938587381145604,
            734938587381174273
        ]
    }

**Example curl Request**

The following example request demonstrates how to add rules using cURL on the command line.

    curl -v -X POST -uexample@customer.com \
    "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=delete" \
    -d '{"rules":[{"value":"testrule"}]}"

    curl -v -X POST -uexample@customer.com \
    "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=delete" \
    -d '{"rule_ids":[734938587381145604,734938587381174273]}"

  

#### Responses

The following responses may be returned by the API for these requests. Non-200 responses should be retried following any necessary modifications to the rules being deleted.

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | Indicates that the rule data supplied with the request consisted of valid JSON. However, note that if no rules are found in the ruleset for the PowerTrack stream based on a case-sensitive search, no rules will be deleted. |
| 400 | Bad Request | Generally relates to poorly formatted JSON, and includes an "Invalid JSON" message in the response. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 429 | Rate Limited | Your app has exceeded the limit on requests to add, delete, or list rules for this stream. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/), contact support. |

  

**Example Responses**

    HTTP/1.1 200 OK
    {
        "summary": {
            "deleted": 3,
            "not_deleted": 0
        },
        "detail": [],
        "sent": "2016-06-01T15:46:48.654Z"
    }

  

    HTTP/1.1 200 OK
    {
        "summary": {
            "deleted": 0,
            "not_deleted": 3
        },
        "detail": [{
            "rule": {
                "value": "Pizza",
                "tag": null
            },
            "deleted": false,
            "message": "Rule does not exist"
        }, {
            "rule": {
                "value": "eggplant",
                "tag": null
            },
            "deleted": false,
            "message": "Rule does not exist"
        }, {
            "rule": {
                "value": "fish",
                "tag": null
            },
            "deleted": false,
            "message": "Rule does not exist"
        }],
        "sent": "2016-06-01T15:49:15.951Z"
    }

  

    HTTP/1.1 400 Bad Request
    {
        "error": {
            "message": "Invalid JSON. The body must be in the format {\"rules\":[{\"value\":\"rule1\", \"tag\":\"tag1\"}, {\"value\":\"rule2\"}]} or {\"rule_ids\": [rule_id1, rule_id2, rule_id3, rule_id4, rule_id5]}",
            "sent": "2013-08-16T00:50:00+00:00"
        }
    }

**Important note on rule management:** Rule sets are indexed by the value or ruleID, not the tag; therefore, all rule additions must reference the rule value or ruleID. In order to to make a tag update to an existing rule, you must first delete it and then add it back with the new tag value.

Rules must be unique per stream based on rule value, see below for a rule management example scenario:

**CREATE RULE**

Action: POST rule {"value":"#TwitterData","tag":"tagtextA"} {"summary":{"created":1,"not\_created":0},"detail":\[{"rule":{"value":"#TwitterData","tag":"tagtextA","id":961664522481119232,"id\_str":"961664522481119232"},"created":true}\],"sent":"2018-02-08T18:14:23.691Z"} System: {"value":"#TwitterData","tag":"tagtextA","id":961664522481119232,"id\_str":"961664522481119232"}

**FAILED ATTEMPT TO UPDATE TAG**

Action: POST rule {"value":"#TwitterData","tag":"tagtextB"} \*\*Rule tags cannot be "updated" - This request is ignored because rule value `#TwitterData` already exists. {"summary":{"created":0,"not\_created":1},"detail":\[{"rule":{"value":"#TwitterData","tag":"tagtextB","id":961664522481119232,"id\_str":"961664522481119232"},"created":false,"message":"A rule with this value already exists"} System: {"value":"#TwitterData","tag":"tagtextA","id":961664522481119232,"id\_str":"961664522481119232"}

**FAILED ATTEMPT TO DELETE BY TAG**

Action: POST method=delete rule {"tag":"tagtextA"} \*\*Rules cannot be deleted by tag. {"summary":{"deleted":0,"not\_deleted":1},"detail":\[{"rule":{"value":"","tag":null},"deleted":false,"message":"Rule does not exist"}\],"sent":"2018-02-08T18:42:37.004Z"} System: {"value":"#TwitterData","tag":"tagtextA","id":961664522481119232,"id\_str":"961664522481119232"}

**DELETE BY ID**

Action: POST method=delete rule {"rule\_ids":\[961664522481119232\]} {"summary":{"deleted":1,"not\_deleted":0},"detail":\[\],"sent":"2018-02-08T18:53:54.185Z"}

**DELETE BY VALUE**

Action: POST method=delete rule {"value":"#TwitterData"} {"summary":{"deleted":1,"not\_deleted":0},"detail":\[\],"sent":"2018-02-08T18:53:54.185Z"}

**RECREATE RULE- NOW WITH NEW ID**

Action: POST rule {"value":"#TwitterData","tag":"tagtextB"} {"summary":{"created":1,"not\_created":0},"detail":\[{"rule":{"value":"#TwitterData","tag":"tagtextB","id":961675641140609025,"id\_str":"961675641140609025"},"created":true}\],"sent":"2018-02-08T18:58:34.586Z"} System: {"value":"#TwitterData","tag":"tagtextB","id":961675641140609025,"id\_str":"961675641140609025"}