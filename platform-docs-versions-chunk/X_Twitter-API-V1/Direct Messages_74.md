platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/buttons/api-reference/buttons


# Buttons

Buttons enable developers to add up to three call-to-action (CTA) buttons to any Direct Message or Welcome Message. These buttons can be used to open any URL from the Direct Message compose view. The text labels displayed on the buttons can be fully customized.

  
  

This feature is intended to make it easier for users to complete actions outside of Direct Messages, whether in a webview or in another part of the Twitter app. For instance, buttons can be used to:

* **Open a webview** to interact with a mobile web page that is better suited for completing an action than completing that action in messaging. For example, completing a credit card purchase or interacting with a side-by-side comparison of different products.
    
* **Compose a Tweet** at the end of a Direct Message interaction. For example, to tell others about a bot or share a coupon publicly. This can be accomplished by using the Tweet [web intents URL scheme](https://dev.twitter.com/web/intents).
    
* **Follow a user** account at the end of a Direct Message interaction. For example, as a final request from a business at the end of a customer service interaction. This can be accomplished using the Follow [web intents URL scheme](https://dev.twitter.com/web/intents).
    
* **Send a Direct Message** to a different account. For example, to direct a user from a marketing-related bot to a separate dedicated customer service @username to get help from a person. This can be accomplished using the Direct Message URL deep link scheme. Example below.
    
        https://twitter.com/messages/compose?recipient_id=3805104374