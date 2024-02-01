platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/api

Graph API Version

[v19.0](#)

# ThreatExchange API Overview

## Authenticate via an Access Token

The ThreatExchange APIs perform authentication via access tokens. After Facebook notifies you that your App can access ThreatExchange, use the [access token tool](https://developers.facebook.com/tools/accesstoken) to get an **App Token**. _Please note, app tokens give access to sensitive details to your app and should be treated like a password._

With the access token, test your access to ThreatExchange by retrieving the list of members in the exchange:

https://graph.facebook.com/threat\_exchange\_members?access\_token=<access\_token>

If this request does not return an error, you are now ready to begin exploring the ThreatExchange API!