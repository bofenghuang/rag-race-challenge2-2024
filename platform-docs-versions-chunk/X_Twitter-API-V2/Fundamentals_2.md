platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction

### Expanded objects

Additional objects related to the top-level object, such as media, place, poll, author (user) of the Tweet, and user's pinned-Tweet are available as expansions, which you can request using the [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions.html) query parameter.   
 

### Fields: defaults and requesting additional fields

If you make a request without any [fields](https://developer.twitter.com/en/docs/twitter-api/fields.html) parameters, you will receive just a few default fields for your top-level object and any expansion objects. For example, Tweets will return just the id and text of a Tweet by default. If you would like to request additional fields, such as the Tweet created\_at or lang fields, you will have to use the fields parameters.