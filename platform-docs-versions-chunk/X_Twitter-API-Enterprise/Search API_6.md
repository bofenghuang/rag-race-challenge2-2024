platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview


### Data Updates and Mutability

With the enterprise search APIs, some of the data within a Tweet is mutable, i.e. can be updated or changed after initial archival.

This mutable data falls into two categories:

* User object metadata:
    * User’s @handle (numeric ID does not ever change)
    * Bio description
    * Counts: statuses, followers, friends, favorites, lists
    * Profile location
    * Other details such as time zone and language
* Tweet statistics - i.e. anything that can be changed on the platform by user actions (examples below):
    * Favorites count
    * Retweet count

In most of these cases, the search APIs will return data as it exists on the platform at _query-time_, rather than Tweet generation time. However, in the case of queries using select operators (e.g. from, to, @, is:verified), this may not be the case. Data is updated in our index on a regular basis, with an increased frequency for most recent timeframes. As a result, in some cases, the data returned may not exactly match the current data as displayed on Twitter.com, but matches data at the time it was last indexed.

Note, this issue of inconsistency only applies to queries where the operator applies to mutable data. One example is filtering for usernames, and the best workaround would be to use user numeric IDs rather than @handles for these queries.