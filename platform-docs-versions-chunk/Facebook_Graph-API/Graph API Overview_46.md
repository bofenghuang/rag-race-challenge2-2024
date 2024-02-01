platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Pages

The Page Rate Limits may use either the Platform or BUC rate limit logic depending on the type of token used. Any Pages API calls that are made using a [Page](https://developers.facebook.com/docs/facebook-login/access-tokens#pagetokens) or [system user access token](https://developers.facebook.com/docs/marketing-api/businessmanager/systemuser#systemusertoken) use the rate limit calculation below. Any calls made with [application](https://developers.facebook.com/docs/facebook-login/access-tokens#apptokens) or [user access tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) are subject to application or User rate limits.

Requests made by your app to the Pages API using a Page access token or system User access token are counted against the app’s call count. An app’s call count is the number of calls it can make during a rolling one hour window and is calculated as follows:

`Calls within one hour = 4800 * Number of Engaged Users`

The Number of Engaged Users is the number of Users who engaged with the Page per 24 hours.

Requests made by your app to the Pages API using a User access token or App access token follow the [Platform Rate Limit logic](#platform-rate-limits).

To avoid [rate limiting](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#pages) issues when using the [Page Public Access Content feature](https://developers.facebook.com/docs/pages/overview/permissions-features#features), using a [system user access token](https://www.facebook.com/business/help/503306463479099) is recommended.