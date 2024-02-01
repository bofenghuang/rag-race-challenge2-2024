platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/rate-limits


### Twitter API v2 rate limits - Basic

The following table lists the rate limits for the Twitter API v2 Basic access. These rate limits are also documented on each endpoint's API Reference page and also displayed in the  [developer portal](https://developer.twitter.com/en/docs/developer-portal)'s products section.

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| **Endpoint** | **#Requests** | **Window of time** | **Per** | **Part of the Tweet pull cap?** | **Effective 30-day limit** |
| DELETE\_2\_lists\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_lists\_param\_members\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_tweets\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_id\_bookmarks\_tweet\_id | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_blocking\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_followed\_lists\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_following\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_likes\_param | 5   | 15 minutes | per user | no  | 14,400 |
| 100 | 24 hours | per user | no  | 3,000 |
| DELETE\_2\_users\_param\_muting\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_pinned\_lists\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_retweets\_param | 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_compliance\_jobs | 5   | 15 minutes | per app | no  | 14,400 |
| GET\_2\_compliance\_jobs\_param | 5   | 15 minutes | per app | no  | 14,400 |
| GET\_2\_dm\_conversations\_param\_dm\_events | 3   | 15 minutes | per user | no  | 8,640 |
| GET\_2\_dm\_conversations\_with\_param\_dm\_events | 3   | 15 minutes | per user | no  | 8,640 |
| GET\_2\_dm\_events | 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_lists\_id | 5   | 15 minutes | per user | no  | 14,400 |
| 5   | 15 minutes | per app | no  | 14,400 |     |
| GET\_2\_lists\_id\_members | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_lists\_id\_tweets | 5   | 15 minutes | per user | yes | 10,000 |
| 25  | 15 minutes | per app | yes | 10,000 |
| GET\_2\_spaces | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_spaces\_by\_creator\_ids | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_spaces\_param | 25  | 15 minutes | per app | no  | 72,000 |
| 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_spaces\_param\_buyers | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_spaces\_param\_tweets | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_spaces\_search | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_tweets | 15  | 15 minutes | per user | yes | 10,000 |
| 15  | 15 minutes | per app | yes | 10,000 |
| GET\_2\_tweets\_counts\_recent | 5   | 15 minutes | per app | no  | 14,400 |
| GET\_2\_tweets\_param | 15  | 15 minutes | per user | yes | 10,000 |
| 15  | 15 minutes | per app | yes | 10,000 |
| GET\_2\_tweets\_param\_liking\_users | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_tweets\_param\_quote\_tweets | 5   | 15 minutes | per user | yes | 10,000 |
| 5   | 15 minutes | per app | yes | 10,000 |
| GET\_2\_tweets\_param\_retweeted\_by | 5   | 15 minutes | per app | yes | 10,000 |
| 5   | 15 minutes | per user | yes | 10,000 |     |
| GET\_2\_tweets\_search\_recent | 60  | 15 minutes | per app | yes | 10,000 |
| 60  | 15 minutes | per user | yes |     |
| GET\_2\_users | 500 | 24 hours | per app | no  | 15,000 |
| 100 | 24 hours | per user | no  | 3,000 |
| GET\_2\_users\_by | 100 | 24 hours | per user | no  | 3,000 |
| 500 | 24 hours | per app | no  | 15,000 |
| GET\_2\_users\_by\_username\_param | 100 | 24 hours | per user | no  | 3,000 |
| 500 | 24 hours | per app | no  | 15,000 |
| GET\_2\_users\_by\_username\_param\_followers | 100 | 24 hours | per user | no  | 3,000 |
| 500 | 24 hours | per app | no  | 15,000 |
| GET\_2\_users\_by\_username\_param\_mentions | 25  | 15 minutes | per app | no  | 72,000 |
| 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_users\_by\_username\_param\_tweets | 25  | 15 minutes | per app | yes | 10,000 |
| 5   | 15 minutes | per user | yes | 10,000 |
| GET\_2\_users\_id\_bookmarks | 10  | 15 minutes | per user | no  | 28,800 |
| GET\_2\_users\_id\_list\_memberships | 25  | 15 minutes | per app | no  | 72,000 |
| 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_users\_id\_owned\_lists | 500 | 24 hours | per app | no  | 15,000 |
| 100 | 24 hours | per user | no  | 3,000 |
| GET\_2\_users\_id\_pinned\_lists | 100 | 24 hours | per user | no  | 3,000 |
| 500 | 24 hours | per app | no  | 15,000 |
| GET\_2\_users\_me | 250 | 24 hours | per user | no  | 7,500 |
| GET\_2\_users\_param | 500 | 24 hours | per user | no  | 15,000 |
| 100 | 24 hours | per app | no  | 3,000 |
| GET\_2\_users\_param\_blocking | 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_users\_param\_following\_spaces | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_users\_param\_liked\_tweets | 5   | 15 minutes | per app | yes | 10,000 |
| 5   | 15 minutes | per user | yes | 10,000 |
| GET\_2\_users\_param\_mentions | 15  | 15 minutes | per app | yes | 10,000 |
| 10  | 15 minutes | per user | yes | 10,000 |
| GET\_2\_users\_param\_muting | 100 | 24 hours | per user | no  | 3,000 |
| GET\_2\_users\_param\_timelines\_reverse\_chronological | 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_users\_param\_tweets | 10  | 15 minutes | per app | yes | 10,000 |
| 5   | 15 minutes | per user | yes | 10,000 |
| POST\_2\_compliance\_jobs | 15  | 15 minutes | per app | no  | 43,200 |
| POST\_2\_dm\_conversations | 5   | 15 minutes | per user | no  | 14,400 |
| 500 | 24 hours | per app | no  | 15,000 |
| 50  | 24 hours | per user | no  | 1,500 |
| POST\_2\_dm\_conversations\_param\_messages | 500 | 24 hours | per app | no  | 15,000 |
| 50  | 24 hours | per user | no  | 1,500 |
| 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_dm\_conversations\_with\_param\_messages | 500 | 24 hours | per app | no  | 15,000 |
| 50  | 24 hours | per user | no  | 1,500 |
| 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_lists | 100 | 24 hours | per user | no  | 3,000 |
| POST\_2\_lists\_param\_members | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_tweets | 100 | 24 hours | per user | no  | 3,000 |
| 1667 | 24 hours | per app | no  | 50,010 |
| POST\_2\_users\_id\_bookmarks | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_blocking | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_followed\_lists | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_following | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_likes | 200 | 24 hours | per user | no  | 6,000 |
| 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_muting | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_pinned\_lists | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_retweets | 5   | 15 minutes | per user | no  | 14,400 |
| PUT\_2\_lists\_param | 5   | 15 minutes | per user | no  | 14,400 |
| PUT\_2\_tweets\_param\_hidden | 5   | 15 minutes | per user | no  | 14,400 |