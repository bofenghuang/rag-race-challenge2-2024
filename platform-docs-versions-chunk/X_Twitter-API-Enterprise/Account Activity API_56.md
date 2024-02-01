platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/migration/us-ss-migration-guide


### Deprecated event types

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Description** | **Event Name** | **Source** | **Target** | **Target Object** |
| User deletes a Tweet | delete | Current user | Current User | Tweet |
| Followed user deletes a Tweet | delete | Followed user | Followed user | Tweet |
| User unfavorites a Tweet | unfavorite | Current user | Tweet author | Tweet |
| User’s Tweet is unfavorited | unfavorite | Unfavoriting user | Current user | Tweet |
| User unfollows someone | unfollow | Current user | Followed user | Null |
| User creates a list | list\_created | Current user | Current user | List |
| User deletes a list | list\_destroyed | Current user | Current user | List |
| User edits a list | list\_updated | Current user | Current user | List |
| User adds someone to a list | list\_member\_added | Current user | Added user | List |
| User is added to a list | list\_member\_added | Adding user | Current user | List |
| User removes someone from a list | list\_member\_removed | Current user | Removed user | List |
| User is removed from a list | list\_member\_removed | Removing user | Current user | List |
| User subscribes to a list | list\_user\_subscribed | Current user | List owner | List |
| User’s list is subscribed to | list\_user\_subscribed | Subscribing user | Current user | List |
| User unsubscribes from a list | list\_user\_unsubscribed | Current user | List owner | List |
| User’s list is unsubscribed from | list\_user\_unsubscribed | Unsubscribing user | Current user | List |
| User updates their profile | user\_update | Current user | Current user | Null |
| User updates their protected status | user\_update | Current user | Current user | Null |