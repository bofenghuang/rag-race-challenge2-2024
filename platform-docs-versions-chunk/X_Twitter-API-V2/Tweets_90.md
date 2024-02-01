platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/migrate/standard-to-twitter-api-v2


## Standard v1.1 timelines to Twitter API v2 timelines

If you have been working with the v1.1 timelines endpoints (statuses/user\_timeline and statuses/mentions\_timeline), the goal of this guide is to help you understand the similarities and differences between the standard and Twitter API v2 timelines endpoints so that you can migrate your current integration to the new version.

* **Similarities:**
    * Authentication:
        * OAuth 1.0a User Context (reverse chronological home timeline, user Tweet timeline and user mentions timeline)
        * OAuth 2.0 App-Only (user Tweet timeline)
    * Historical Access limit: User timeline (user Tweet timeline) provides access to most recent 3200 Tweets; mentions timeline (user mention timeline) provides access to most recent 800 mentions.
    * Support for Tweet edit history and metadata
    * Rate limits (user Tweet timeline)
    * Refresh polling: Ability to retrieve new results since the since\_id
    * Traversing timelines by Tweet IDs
    * Results specifications:
        * Results order: Results returned in reverse chronological order
        * Ability to exclude replies (user Tweet timeline only)
        * Ability to exclude Retweets (user Tweet timeline only)
* **Differences**
    * New Authentication capability: 
        * OAuth 2.0 App-Only (user mention timeline)
        * OAuth 2.0 Authorization Code Flow with PKCE (reverse chronological home timeline, user Tweet timeline and user mentions timeline)
    * Access requirements: Twitter API v2 App and Project requirements
    * Rate limits (user mention timeline and reverse chronological home timeline)
    * Different Request limit & Volume limit
    * Additional pagination method
        * Different max\_results (count) per response
    * Response data format
    * Request parameters  
        * Customized data format based on request parameters, including v2 fields and expansions
        * Additional available data: metrics, Tweet annotations, polls