platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/integrate


## Integration guide

The Direct Messages endpoints v2 introduce conversations and conversation events as core Twitter API objects, and make a distinction between 1-1 and group conversations. 1-1 conversations always have two, and only two, participants, while group conversations can have two or more and memberships that can change.   

This page contains information on several tools and key concepts that you should be aware of as you integrate the Direct Messages lookup endpoints into your system. We’ve broken the page into two sections:

* Key Concepts
    * [Direct Message conversations](#direct-message-conversations)
    * [Shared conversation and event IDs across v1.1 and v2](#shared-conversation-and-event-ids)
    * [Direct Message event fields and expansions](#direct-message-event-fields-and-expansions)
    * [Conversation event types](#conversation-event-types)
    * [Authentication](#authentication)
    * [Developer portal, Projects, and Apps](#developer-portal-projects-and-apps)
    * [Rate limits](#rate-limits)
    * [Pagination](#pagination)
* [Helpful tools](#helpful-tools)