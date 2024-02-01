platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/replay-stream

### Sample streams Replay Examples (Stream Types include 'sample10' (i.e. decahose), 'firehose', 'mentions')[¶](#sample-streams-replay-examples-stream-types-include-sample10-i-e-decahose-firehose-mentions- "Permalink to this headline")

Decahose, firehose, mentions note- All partitions from volume streams are delievered in a single Replay connection.

    curl --compressed -v -uexample@customer.com 
"https://gnip-stream.gnip.com/replay/sample10/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json?fromDate=201712312330&toDate=201801010130"

### Compliance Replay Examples[¶](#compliance-replay-examples "Permalink to this headline")

Compliance note- All partitions from Compliance Firehose are delievered in a single Replay connection.

curl --compressed -v -uexample@customer.com 
"https://gnip-stream.gnip.com/replay/compliance/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json?fromDate=201712312330&toDate=201801010130"