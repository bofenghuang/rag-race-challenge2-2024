platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/integrate/integrating-compliance-streams

Integrating compliance streams

The Tweet and User compliance streams are realtime streaming endpoints that delivers compliance events that occur on the Twitter platform. For an understanding of compliance events and how they are generated on Twitter, please reference our article, [Honoring User Intent on Twitter](https://developer.twitter.com/en/docs/twitter-api/compliance/streams/integrate/honoring-user-intent.html).

It is important to note that Tweet and User events are delivered independently and that each should be processed independently (i.e. a Tweet delete doesn’t imply a User event, and vice versa.) Several User events are not necessarily permanent and can toggle between states infinitely. These include: user\_delete,user\_undelete, user\_protect, user\_unprotect and user\_suspend, user\_unsuspend.

User\_deletes are followed by Tweet deletes 30 days later only if the user has not selected to user\_undelete their account. It is possible that a user\_delete is reversed by the user and deletes for all of their Tweets 30 days later do not occur.

User\_suspend is an action that remains true unless the user is subject to an user\_unsuspend event. These are not subject to any changes on a 30 day time period.

It is never suitable to display compliance events directly to users of your software or to otherwise incorporate them into your products or customer experiences. They are intended solely for maintaining compliance and honoring the actions of Twitter users.