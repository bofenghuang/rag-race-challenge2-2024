platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/versioning

## Versioning Strategy

Versioning for the Twitter API will be represented by version numbers declared in the route path for our endpoints:

https://api.twitter.com/2/tweets

We aim to release major versions of the Twitter API as necessary but no more frequently than every 12 months. A major version will be released when breaking changes are introduced in the API. We will publish migration guides when launching a new major version to help developers migrate over to the new version. 

A breaking change requires developers to change their code to maintain existing functionality in their app. Non-breaking changes will be additive and rolled out to the most recent version when ready, requiring no work on a developer’s end unless you would like to take advantage of the new functionality.

If a breaking change must be rolled out mid-cycle (for security or privacy reasons), this change will be made to the most recent version.