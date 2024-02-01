platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/conversation-management/guides/initiated-via

initiated\_via

When users communicate with businesses through Direct Messages, they may be guided by [Welcome Messages](https://dev.twitter.com/rest/direct-messages/direct-messages/welcome-messages) or led to a private conversation via a Direct Message deeplink. In these cases, it can be important for developers to know if another object preceded the DM in conversation. For example, Initiated Via helps a customer service agent see the full conversation history or enable a bot developer to perform A/B testing of different welcome messages.

The initiated\_via object in the Direct Message event object indicates the ID of the Twitter entity that directly preceded the DM in the sender’s context. Currently tweet\_id and welcome\_message\_id may be included. The initiated\_via object is only present if a Twitter entity directly preceded the DM.