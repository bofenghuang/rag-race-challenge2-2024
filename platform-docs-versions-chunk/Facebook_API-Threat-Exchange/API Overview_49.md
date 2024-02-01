platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/examples

## cURL

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.

curl -i -X GET \\
"https://graph.facebook.com/v2.4/threat\_indicators"\\
"?type=IP\_ADDRESS&text=proxy&access\_token=555%7C1234"

Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.

curl -i -X GET \\
"https://graph.facebook.com/v2.4/threat\_descriptors"\\
"?type=IP\_ADDRESS&owner=820763734618599&text=proxy&access\_token=555%7C1234"