platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/overview

### Terminology

To avoid confusion around the term "friends" and "followers" with respect to the API endpoints, below is a definition of each:

**Friends** - we refer to "friends" as the Twitter users that a specific user follows (e.g., following). Therefore, the GET friends/ids endpoint returns a collection of user IDs that the specified user follows.

**Followers** - refers to the Twitter users that follow a specific user. Therefore, making a request to the GET followers/ids endpoint returns a collection of user IDs for every user following the specified user.