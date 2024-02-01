platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/poll-metadata

### Tweet Payload

Poll Tweets will contain the following metadata in the “entities.polls” object in the payload:

* An “options” array with up to four options that include the position (1-4) and option text
* Poll expiration date
* Poll duration

See the sample payload below for further reference.