platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/integrate

### Shared conversation and event IDs across v1.1 and v2

An important concept is that conversation and event IDs are shared across v1.1 and v2 versions of the Twitter Platform. This means both versions can be used together. For example, the Direct Messages v1.1 endpoints provide methods for returning a single event and for deleting events, methods not yet available with v2. Since IDs are common across v1.1 and v2, you can make v1.1 requests based on IDs provided by v2, or by referencing conversation IDs displayed in conversation URLs on the Twitter application.