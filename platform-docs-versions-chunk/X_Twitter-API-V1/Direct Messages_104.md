platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/custom-profiles/api-reference/get-profile-list

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **count** (optional) | Number of custom profile objects to be returned. Max of 50. Default is 20. |
| **cursor** (optional) | For paging through result sets greater than 1 page. Use the `next_cursor` property returned from the previous request. |

_Note:_ In rare cases a response may contain an empty custom profile object with `next_cursor` defined. The presence of a `next_cursor` property in the response indicates there are more custom profiles to retrieve.

## Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -X GET /1.1/custom_profiles/list.json?count=2&cursor=MTIzNDU2Nzg