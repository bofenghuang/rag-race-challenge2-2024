platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/welcome-messages/guides/setting-default-welcome-message


# Setting a Default Welcome Message

Without a default Welcome Message, users are presented with an empty Direct Message conversation view or the state of the previous conversation.  A Welcome Message may be set to default so that it is presented to the user when a Welcome Message deeplink is not used. Use a default Welcome Message to provide context to users including what services are provided, when they can receive response or provide Quick Reply options to start an automated conversation flow. All features available to Direct Messages can be used in a default Welcome Message.

When a Welcome Message is set as default, it will be presented to the user in the following scenarios:

* Direct Message compose view opened for the first time.
* Direct Message compose view opened for the first time since leaving a conversation.
* Direct Message compose view opened after no message activity for 7 days.

**Note:** Specifying a Welcome Message in a [deeplink](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/guides/deeplinking-to-welcome-message) will always override the default Welcome Message. Deeplinking without a defined Welcome Message will follow default Welcome Message behavior defined above.

To set a default Welcome Message:

1. Create a new Welcome Message with [POST direct\_messages/welcome\_messages/new](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message). Take note of the returned Welcome Message ID.
2. Create a new Welcome Message Rule using the Welcome Message ID with [POST direct\_messages/welcome\_messages/rules/new](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message-rule).  
    

**Note:** Although an account can have many Welcome Messages, an account may only have a single “default” Welcome Message and only a single rule. If you have previously created a rule, you must [delete](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/delete-welcome-message-rule) the current rule before creating a new one. See [POST direct\_messages/welcome\_messages/rules/new](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message-rule) documentation for more information regarding the future of rules.