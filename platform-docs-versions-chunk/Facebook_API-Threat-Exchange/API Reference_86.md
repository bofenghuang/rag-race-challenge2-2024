platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/submitting-connections

## Use the API

Using the API, you can create connections via an `HTTP POST` request to the `/related` URI for a specific object:

https://graph.facebook.com/v2.8/<object\_id>/related

In this example, create a connection between the `facebook.com` domain object (`788497497903212`) and the 173.252.120.6 IP address object (`1061383593887032`), which `facebook.com` can resolve to via DNS.

https://graph.facebook.com/v2.8/788497497903212/related

POST DATA:
related\_id=1061383593887032
&amp;access\_token=<access\_token>

Data returned:

{
"success": true
}