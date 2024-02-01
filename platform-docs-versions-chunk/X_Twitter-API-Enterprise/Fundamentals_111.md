platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules

Matching rules object

# Matching rules

The matching rules enrichment is an object of metadata that indicates which rule or rules matched the Tweets received. This is most commonly used with the PowerTrack stream.

Matching will be done via exact match on the terms contained in a rule, scanning the content of the activity with and without punctuation. Matching is not case sensitive. When the content is found to contain all terms defined in the rule, there will be a root-level a matching\_rules object indicating the rule(s) that led to the match.