platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/customer-feedback/overview

## Access & authentication

Customer feedback cards only display to users in the iOS or Android Twitter apps. They do not display on twitter.com, mobile.twitter.com, TweekDeck, or 3rd-party Twitter apps, even if a feedback request is sent. 

Customer feedback cards are only available to Twitter enterprise data customers.

* Your client app ID and a @username must each be added to an allowlist to get app ­level access to the API.
* Authentication is 3-­legged OAuth currently used with the Twitter public API.
* We must additionally add the @username to an allowlist for any accounts you wish to send Feedback requests FROM (either your customer’s handles or your own if used for testing purposes).