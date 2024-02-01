platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/replay-stream


### PowerTrack Replay Examples[¶](#powertrack-replay-examples "Permalink to this headline")

Connection to Replay to complete data during the 2018 New Year's eve disconnection:

    curl --compressed -v -uexample@customer.com 
"https://gnip-stream.gnip.com/replay/powertrack/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json?fromDate=201712312330&toDate=201801010130"

Important Note: When using PowerTrack Replay, you must first add or manage the rules currently on the replay stream. PowerTrack rules are not automatically added to a Replay stream from a normal PowerTrack stream. Rules can be managed through the Rules API for a Replay stream. Please see the [PowerTrack Rules API](https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/powertrack-rules) for specific details on managing rules.

Rules management on the PowerTrack replay:

curl -v -X POST -uexample@customer.com 
"https://gnip-api.twitter.com/rules/powertrack-replay/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json" 
-d '{"rules":\[{"value":"rule1","tag":"tag1"},{"value":"rule2"}\]}'