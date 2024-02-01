platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities

## Entities for user object

Entities for User Objects describe URLs that appear in the user defined profile URL and description fields. They do not describe hashtags or user\_mentions. Unlike Tweet entities, user entities can apply to multiple fields within its parent object — to disambiguate, you will find a parent nodes called url and description that indicate which field contains the entitized URL.

In this example, the user url field contains a t.co link that is fully expanded within the entities/url/urls\[0\] node of the response. The user does not have a wrapped URL in their description.