platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting

### Users

Graph API requests made with a [user access token](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) are counted against that user’s call count. A user’s call count is the number of calls a user can make during a rolling one hour window. Due to privacy concerns, we do not reveal actual call count values for users.

Note that a user’s call count can be spread over multiple apps. For example, a user could make X calls through App1 and Y calls through App2. If X+Y exceeds the user’s call count that user will be rate limited. This does not necessarily mean that any app is doing something wrong; it could be that the user is using multiple apps or is misusing the API.