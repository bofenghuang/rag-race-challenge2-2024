platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/annotations/overview


## Overview

Annotations have been added to the Tweet object from all v2 endpoints that return a Tweet object. Tweet annotations offer a way to understand contextual information about the Tweet itself. Though 100% of Tweets are reviewed, due to the contents of Tweet text, only a portion are annotated.

**Entity annotations (NER):** Entities are comprised of people, places, products, and organizations. Entities are delivered as part of the entity payload section. They are programmatically assigned based on what is explicitly mentioned (named-entity recognition) in the Tweet text.

**Context annotations:** Derived from the analysis of a Tweet’s text and will include a domain and entity pairing which can be used to discover Tweets on topics that may have been previously difficult to surface. At present, we’re using a list of 80+ domains to categorize Tweets. A CSV file of the available context annotation entities is available for download at our [Github repository](https://github.com/twitterdev/twitter-context-annotations).