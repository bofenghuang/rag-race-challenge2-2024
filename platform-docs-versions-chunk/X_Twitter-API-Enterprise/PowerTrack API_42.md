platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-rules

PowerTrack Rules API

powertrack-rules

# PowerTrack Rules API

Jump to on this page

[Methods](#Methods)

[Authentication](#Authentication)

[POST /rules](#AddRules)

[GET /rules](#ListRules)

[GET /rules/:rule\_id](#GetRule)

[POST /rules \_method=get](#GetRules)

[POST /rules \_method=delete](#DeleteRules)

[POST /validation](#ValidateRules)

## Methods [¶](#methods- "Permalink to this headline")

| Method | Description |
| --- | --- |
| [POST /rules](#AddRules) | Add rules to the stream |
| [GET /rules](#ListRules) | Retrieve all rules currently in place on the stream |
| [GET /rules/:rule\_id](#GetRule) | Retrieve an existing rule on the stream by rule ID |
| [POST /rules \_method=get](#GetRules) | Retrieve multiple rules on the stream by rule IDs |
| [POST /rules \_method=delete](#DeleteRules) | Delete rules from the stream |
| [POST /validation](#ValidateRules) | Validate PowerTrack rule syntax |