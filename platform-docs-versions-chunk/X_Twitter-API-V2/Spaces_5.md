platform: X
topic: Twitter-API-V2
subtopic: Spaces
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Spaces.md
url: https://developer.twitter.com/en/docs/twitter-api/spaces/overview

## Roles in Spaces

These endpoints reflect the way Spaces work on the Twitter app. In Spaces, Twitter users can have defined roles depending on how they interact with and interact in a Space.  
 

### Creator (or primary host)

The primary Host is the user who created a Space, and the owner of the Space itself. Currently, Spaces can only have one Host, so the primary Host will be the only Host. In the [Spaces data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/spaces), the primary Host information will be in the creator\_id field, which can be expanded into a [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user).