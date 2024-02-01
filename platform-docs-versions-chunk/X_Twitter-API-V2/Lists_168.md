platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference

API reference

## API reference index

For the complete API reference, select an endpoint from the list.  
  

### Pinned List lookup  

|     |     |
| --- | --- |
| **Returns the pinned Lists of the authenticated user** | `[GET /2/users/:id/pinned_lists](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/get-users-id-pinned_lists)` |

### Manage pinned List  

|     |     |
| --- | --- |
| **Pins a List on behalf of an authenticated user** | `[POST /2/users/:id/pinned_lists](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/post-users-id-pinned-lists)` |
| **Unpins a List on behalf of an authenticated user** | `[DELETE /2/users/:id/pinned_lists/:list_id](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/delete-users-id-pinned-lists-list_id)` |