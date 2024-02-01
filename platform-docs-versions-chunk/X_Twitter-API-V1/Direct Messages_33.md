platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/welcome-messages/guides/deeplinking-to-welcome-message

# Deeplinking to a Welcome Message

Every Welcome Message can be deeplinked to. When a user follows the deeplink, the Direct Message compose view will be opened with the specified Welcome Message presented. Deeplinks can be used anywhere from a website, an app, a Tweet or even another Direct Message conversation.

To create a Welcome Message deeplink:

1. Create a new Welcome Message with [POST direct\_messages/welcome\_messages/new](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message). Take note of the returned Welcome Message ID.  
    
2. Construct a Direct Message deeplink with the recipient\_id and welcome\_message\_id query string parameters defined.  
    

Example Direct Message Deeplink:  

https://twitter.com/messages/compose?recipient\_id= 3805104374&welcome\_message\_id=12345

**Note:** You can create as many Welcome Messages as you require and all Welcome Messages can be deeplinked to.

Deeplinking from a Tweet