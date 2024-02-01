platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-lists-id


### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this List. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The name of this List. |
| `created_at` | date (ISO 8601) | Creation time of this List.  <br>  <br>To return this field, add `list.fields=created_at` in the request's query parameter. |
| `private` | boolean | Indicates if this List has been set to private. The List (in other words, if this is publicly viewed or not).  <br>  <br>To return this field, add `list.fields=private` in the request's query parameter. |
| `follower_count` | integer | Number of users who follow this List.  <br>  <br>To return this field, add `list.fields=follower_count` in the request's query parameter. |
| `member_count` | integer | Number of users who are a member of this List.  <br>  <br>To return this field, add `list.fields=member_count` in the request's query parameter. |
| `owner_id` | string | Unique identifier of this List's owner. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `list.fields=owner_id` in the request's query parameter. |
| `description` | string | A brief description of this List, if the owner provided one.  <br>  <br>To return this field, add `list.fields=description` in the request's query parameter. |
| `includes.users` | array | When including the `expansions=owner_id` parameter, this includes the referenced List owner in the form of a [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |