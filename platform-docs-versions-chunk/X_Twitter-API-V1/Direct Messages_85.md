platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/conversation-management/overview

Overview

When creating an app to manage Direct Messages, having context of where the user came from or what application was responsible for sending the message can be important information for managing the conversation. Having this context can help improve analytics or determine the next action your app should take. To provide this context the following is available in Direct Message event objects when applicable.

## Event properties

Message create event properties for conversation management.

* [initiated\_via](https://developer.twitter.com/en/docs/direct-messages/conversation-management/guides/initiated-via)  
    Provides the Twitter entity (Tweet or Welcome Message) that preceded the Direct Message in conversation.
* [source\_app](https://developer.twitter.com/en/docs/direct-messages/conversation-management/guides/source-app)  
    Provides information about the Twitter app the authenticating account used to send the Direct Message.