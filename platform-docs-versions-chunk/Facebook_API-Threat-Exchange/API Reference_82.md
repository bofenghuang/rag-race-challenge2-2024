platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/reacting

## React Using the API

To express an opinion about descriptor 952030561511282 using the API, append your access token and issue a **POST** to:

    https://graph.facebook.com/v4.0/952030561511282?reactions=HELPFUL,SAW_THIS_TOO
    
    

To retrieve the reactions of everyone else, append your access token and issue a `GET` to.

    https://graph.facebook.com/v4.0/952030561511282?fields=id,my_reactions,reactions
    
    

The `my_reactions` field shows your own reactions, and the `reactions` field is a map from the possible [ReactionType](https://developers.facebook.com/docs/threat-exchange/reference/apis/reaction-type) to the apps that reacted with that type. If there are no reactions, the field is empty.

## Share Feedback

_Reactions_ are a growing feature. To provide feedback about reactions, contact threatexchange@fb.com, or use the bug nub in the TEUI.