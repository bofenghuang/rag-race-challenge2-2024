platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/integrate/manage-replies-in-realtime


## Manage replies in realtime

With the hide replies endpoint, you can build a workflow to helps your users hide replies that have a very high-probability of being irrelevant.

Useful apps often combine technologies so that they can be valuable to their users. This page shows how to hide replies by using the [Perspective API](https://www.perspectiveapi.com/). This API is an artificial intelligence trained by [Jigsaw](https://jigsaw.google.com/), a unit within Google, to detect toxic comments. The application logic will work in the following way:

1. It asks the user’s permission to read their Tweets and hide or unhide their replies.
2. It uses the [Account Activity API](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview.html) to detect incoming replies.
3. It asks the Perspective API to give a “score” (a number between 0 and 1) that indicates how confident their algorithm is that a comment is similar to toxic comments it’s seen in the past. (Perspective does not store the text sent to the service).
4. It calls hide replies if the algorithm’s score is very high.