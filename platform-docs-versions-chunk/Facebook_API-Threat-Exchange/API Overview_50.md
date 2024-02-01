platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/api-structure

# API Structure for ThreatExchange

ThreatExchange is a subset of API endpoints within the larger ecosystem of Facebook Graph APIs. It is recommended to review the [Graph API documentation](https://developers.facebook.com/docs/graph-api), as it covers key concepts: usage of access tokens for authentication, result pagination, and batching.

The ThreatExchange APIs are made up of various [objects](https://developers.facebook.com/docs/threat-exchange/reference/apis) and each object can have connections to other objects. For instance, a threat indicator is an object that can be connected to other threat indicators.

ThreatExchange also allows for multiple members to share the same threat indicator. Because there is the potential for a collision, we separate each member's submission into distinct [ThreatDescriptor](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor) objects, which are connected to their respective [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator)