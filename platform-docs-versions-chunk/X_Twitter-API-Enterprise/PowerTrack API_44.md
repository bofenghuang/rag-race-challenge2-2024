platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-rules


## POST /rules [¶](#post-rules- "Permalink to this headline")

Adds one or many rules to your PowerTrack stream's ruleset.

#### Request Specifications

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **Content Type** | "application/json". The request should specify this as the "Content-type". |
| **URL** | Found on the [Console - Products API Help tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/product), and uses the following structure:  <br>  <br>`https://data-api.twitter.com/rules/powertrack/accounts/{gnip_account_name}/publishers/twitter/{stream_label}.json` |
| **Character Encoding** | UTF-8 |
| **Request Body Format** | JSON |
| **Request Body Size Limit** | 5 MB |
| **Rate Limit** | 60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream's API (POST and GET). Rule addition requests will be processed serially and will be rejected if you have more than one rule request happening at the same time. |

  

#### Request Body Content

Your request should provide rule data in the following format with the defined Content-type: "application/json":

    {
        "rules":
        [
            {"value":"rule1","tag":"tag1"},
            {"value":"rule2","tag":"tag2"}
        ]
    }

  

**Example curl Request**

The following example requests demonstrate how to add rules using cURL on the command line, using JSON rules.

    curl -v -X POST -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json" -d '{"rules":[{"value":"rule1","tag":"tag1"},{"value":"rule2","tag":"tag2"}]}'

  

    curl -v -X POST -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json" -d @arrayofrulesfile_max5mb.json

  

    curl -v -X POST -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/companyname/publishers/twitter/prod.json" -d '{"rules":[{"value":"(#snow OR snowday OR "snow day" OR from:noaa) lang:en","tag":"4581245"},{"value":"(skiing OR boarding OR "hitting the slopes" OR from:OnTheSnow) lang:en","tag":"4581267"}]}'

  

#### Responses

The following responses may be returned by the API for these requests. Non-200 responses should be retried after making any necessary modifications in the rules.

| Status | Text | Description |
| --- | --- | --- |
| 201 | Created | The rule or rules were successfully added to your PowerTrack ruleset. |
| 400 | Bad Request | Generally relates to poorly formatted JSON, and includes an "Invalid JSON" message in the response. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 422 | Unprocessable Entity | Generally occurs due to an invalid rule, based on the PowerTrack rule restrictions. Requests fail or succeed as a batch. For these errors, each invalid rule and the reason for rejection is included in a JSON message in the response. Catch the associated exception to expose this message. |
| 429 | Rate Limited | Your app has exceeded the limit on requests to add, delete, or list rules for this stream. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) contact support or contact emergency if still unable to connect after 10 minutes. |

  

**Example Responses**

This response indicates that all rules (two in this case) were successfully created.

    HTTP/1.1 201 Created
    {
        "summary": {
            "created": 2,
            "not_created": 0
        },
        "detail": [{
            "rule": {
                "value": "(#snow OR snowday OR \"snow day\" OR from:noaa) lang:en",
                "tag": "4581245",
                "id": 734938587381145604
            },
            "created": true
        }, {
            "rule": {
                "value": "(skiing OR boarding OR \"hitting the slopes\" OR from:OnTheSnow) lang:en",
                "tag": "4581267",
                "id": 734938587381174273
            },
            "created": true
        }],
        "sent": "2016-05-24T02:46:28.402Z"
    }

This response indicates that one rule was successfully created, and two were not created because they already exist. Rules are indexed by rule value (syntax). For rules not created there is a 'message' field explaining why the rule could not be created.

    HTTP/1.1 201 Created
    {
        "summary": {
            "created": 1,
            "not_created": 2
        },
        "detail": [{
            "rule": {
                "value": "robot OR 🤖",
                "tag": "botrule123",
                "id": 734861971116285952
            },
            "created": true
        }, {
            "rule": {
                "value": "fish OR 🐟",
                "tag": "fishrule123"
            },
            "created": false,
            "message": "A rule with this value already exists"
        }, {
            "rule": {
                "value": "Pizza OR 🍕",
                "tag": "pizzarule123"
            },
            "created": false,
            "message": "A rule with this value already exists"
        }],
        "sent": "2016-05-23T21:42:01.661Z"
    }

The following responses indicate that no rules were created. In each case there is a 'message' field explaining why the rule could not be created. Note that when one or more rules are invalid, no rules are added (even rules with valid syntax).

  

    HTTP/1.1 422 Unprocessable Entity
    {
        "summary": {
            "created": 0,
            "not_created": 2
        },
        "detail": [{
            "rule": {
                "value": "streaming gnip contains:$twtr",
                "tag": null
            },
            "created": false,
            "message": "no viable alternative at input '$twtr' (at position 25)\n"
        }, {
            "rule": {
                "value": "streaming gnip contains:\"$twtr\"",
                "tag": null
            },
            "created": false
        }],
        "sent": "2016-06-01T15:41:27.451Z"
    }

  

    HTTP/1.1 422 Unprocessable Entity
    {
        "summary": {
            "created": 0,
            "not_created": 1
        },
        "detail": [{
            "rule": {
                "value": "-follow",
                "tag": null
            },
            "created": false,
            "message": "Rules must contain a non-negation term (at position 1)\nRules must contain at least one positive, non-stopword clause (at position 1)\n"
        }],
        "sent": "2016-05-23T18:34:25.218Z"
    }

  

    HTTP/1.1 422 Unprocessable Entity
    {
        "summary": {
            "created": 0,
            "not_created": 1
        },
        "detail": [{
            "rule": {
                "value": "streaming AND lang:en",
                "tag": null
            },
            "created": false,
            "message": "Ambiguous use of and as a keyword. Use a space to logically join two clauses, or \"and\" to find occurrences of and in text (at position 11)\n"
        }],
        "sent": "2016-05-23T21:39:49.612Z"
    }