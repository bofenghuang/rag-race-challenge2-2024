platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits


### GET endpoints

The standard API rate limits described in this table refer to GET (read) endpoints. Note that endpoints not listed in the chart default to 15 requests per allotted user. All request windows are 15 minutes in length.  These rate limits apply to the standard API endpoints only, does not apply to premium APIs.

| Endpoint | Requests / window per user | Requests / window per app |
| --- | --- | --- |
| GET account/verify\_credentials | 75  | 0   |
| GET application/rate\_limit\_status | 180 | 180 |
| GET favorites/list | 75  | 75  |
| GET followers/ids | 15  | 15  |
| GET followers/list | 15  | 15  |
| GET friends/ids | 15  | 15  |
| GET friends/list | 15  | 15  |
| GET friendships/show | 180 | 15  |
| GET geo/id/:place\_id | 75  | 0   |
| GET help/configuration | 15  | 15  |
| GET help/languages | 15  | 15  |
| GET help/privacy | 15  | 15  |
| GET help/tos | 15  | 15  |
| GET lists/list | 15  | 15  |
| GET lists/members | 900 | 75  |
| GET lists/members/show | 15  | 15  |
| GET lists/memberships | 75  | 75  |
| GET lists/ownerships | 15  | 15  |
| GET lists/show | 75  | 75  |
| GET lists/statuses | 900 | 900 |
| GET lists/subscribers | 180 | 15  |
| GET lists/subscribers/show | 15  | 15  |
| GET lists/subscriptions | 15  | 15  |
| GET search/tweets | 180 | 450 |
| GET statuses/lookup | 900 | 300 |
| GET statuses/mentions\_timeline | 75  | 0   |
| GET statuses/retweeters/ids | 75  | 300 |
| GET statuses/retweets\_of\_me | 75  | 0   |
| GET statuses/retweets/:id | 75  | 300 |
| GET statuses/show/:id | 900 | 900 |
| GET statuses/user\_timeline | 900 | 1500 |
| GET trends/available | 75  | 75  |
| GET trends/closest | 75  | 75  |
| GET trends/place | 75  | 75  |
| GET users/lookup | 900 | 300 |
| GET users/search | 900 | 0   |
| GET users/show | 900 | 900 |
| GET users/suggestions | 15  | 15  |
| GET users/suggestions/:slug | 15  | 15  |
| GET users/suggestions/:slug/members | 15  | 15  |