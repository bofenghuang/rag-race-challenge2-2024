platform: X
topic: Twitter-API-V2
subtopic: Spaces
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Spaces.md
url: https://developer.twitter.com/en/docs/twitter-api/spaces/overview

## Understanding the lifecycle of Spaces

Unlike other resources of the Twitter Developer Platform, Spaces have a set lifecycle. Spaces can be scheduled up to 14 days in advance of their intended start date, and become unavailable after they end. A host can also cancel a previously scheduled Space anytime before it starts.

Spaces are accessible while they are live; once ended, they will no longer be available for retrieval using the Spaces endpoints, and an error message will be returned to indicate this condition.

When your app handles Spaces data, you are responsible for returning the most up-to-date information, and that you remove data that is no longer available from the platform. The [Spaces lookup endpoint](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/introduction) can help you ensure you respect the expectations and intent of your users.