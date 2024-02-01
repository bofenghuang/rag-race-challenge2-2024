platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/integrate


## Integration guide

The Direct Messages endpoints v2 introduce conversations and conversation events as core Twitter API objects, and makes a distinction between one-to-one and group conversations. One-to-one conversations always have two, and only two, participants, while group conversations can have two or more and memberships that can change.   

This page contains information on several tools and key concepts that you should be aware of as you integrate the Manage Direct Messages endpoints into your system. We’ve broken the page into two sections:

* Key Concepts
    * [Direct Message conversations](#direct-message-conversations)  
        
    * [Shared conversation and event IDs across v1.1 and v2](#shared-conversation-and-event-ids)
    * [Including media attachments and referencing Tweets](#including-media-attachments-and-referencing-tweets)
    * [Authentication](#authentication)  
        
    * [Developer portal, Projects, and developer Apps](#developer-portal-projects-and-developer-apps)  
        
    * [Rate limits](#rate-limits)  
        
* [Helpful tools](#helpful-tools)