platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/conversation-management/guides/source-app

source\_app

# source\_app

Some Twitter accounts may make use of more than one application to send Direct Messages — such as when a human social care app is used alongside a separate bot app to manage the same account. In these cases, it can be helpful for developers to know which app was used to send a given message.

The new source\_app object will return this information for all DMs sent by an account. This object is included in the JSON payload for webhooks and REST endpoints. It is relevant on the read path only — Twitter automatically adds this information based on the app authentication used to post a DM. This value will not be returned in the response for POST events/new.json.

**Note:** This same pattern exists with Tweets with the source property, however the JSON structure is different. Please also note that this object will not be included for DMs received by an authenticating user and is only included for DMs sent by the authenticating user.