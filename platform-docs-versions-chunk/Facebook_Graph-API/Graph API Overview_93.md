platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/error-handling


### Error Codes

| Code or Type | Name | What To Do |
| --- | --- | --- |
| OAuthException |     | If no subcode is present, the login status or access token has expired, been revoked, or is otherwise invalid. [Get a new access token](https://developers.facebook.com/docs/facebook-login/access-tokens#errors).<br><br>If a subcode is present, see the subcode. |
| 102 | API Session | If no subcode is present, the login status or access token has expired, been revoked, or is otherwise invalid. [Get a new access token](https://developers.facebook.com/docs/facebook-login/access-tokens#errors).<br><br>If a subcode is present, see the subcode. |
| 1   | API Unknown | Possibly a temporary issue due to downtime. Wait and retry the operation. If it occurs again, check that you are requesting an existing API. |
| 2   | API Service | Temporary issue due to downtime. Wait and retry the operation. |
| 3   | API Method | Capability or permissions issue. Make sure your app has the necessary capability or permissions to make this call. |
| 4   | API Too Many Calls | Temporary issue due to throttling. Wait and retry the operation, or examine your API request volume. |
| 17  | API User Too Many Calls | Temporary issue due to throttling. Wait and retry the operation, or examine your API request volume. |
| 10  | API Permission Denied | Permission is either not granted or has been removed. [Handle the missing permissions](https://developers.facebook.com/docs/facebook-login/permissions#handling). |
| 190 | Access token has expired | [Get a new access token](https://developers.facebook.com/docs/facebook-login/access-tokens#errors). |
| 200-299 | API Permission (Multiple values depending on permission) | Permission is either not granted or has been removed. [Handle the missing permissions](https://developers.facebook.com/docs/facebook-login/permissions#handling). |
| 341 | Application limit reached | Temporary issue due to downtime or throttling. Wait and retry the operation, or examine your API request volume. |
| 368 | Temporarily blocked for policies violations | Wait and retry the operation. |
| 506 | Duplicate Post | Duplicate posts cannot be published consecutively. Change the content of the post and try again. |
| 1609005 | Error Posting Link | There was a problem scraping data from the provided link. Check the URL and try again. |