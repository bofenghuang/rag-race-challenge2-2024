platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-groups

### Sample Usage

To create a privacy group:

curl -s -X POST \\
'https://graph.facebook.com/v14.0/threat\_privacy\_groups'\\
'?access\_token=REDACTED'\\
'&name=Testing+curl+post'\\
'&description=Testing+curl+post'\\
'&members\_can\_see=TRUE'

Data returned:

{"id":"1200716590320515"}

To edit:

curl -s -X POST \\
'https://graph.facebook.com/v14.0/1200716590320515'\\
'?access\_token=REDACTED'\\
'&name=Testing+curl+post'\\
'&description=Testing+curl+post+update'

Data returned:

{"success":true}