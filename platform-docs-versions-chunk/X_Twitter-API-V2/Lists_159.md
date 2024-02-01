platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/quick-start/pinned-list-lookup


### Steps to build a pinned List lookup request

#### Step one: Choose the List endpoint collection from Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “Pinned Lists”, and then choose "User's pinned Lists".  
 

#### Step two: Identify and specify the user

In order to retrieve a user’s pinned List, you must specify their user ID within the request. The user ID must correspond to the authenticating user’s ID, meaning that you must pass the Access Tokens associated with the user ID when authenticating your request. In this example, you can specify the ID belonging to your own user. You can find your ID in two ways:

1. Using the [users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference) by username endpoint, you can pass a username and receive the id field.
2. Looking at your Access Token, you will find that the numeric part is your user ID.

In Postman, navigate to the "Params" tab and enter this user ID into the "Value" column of the `id` parameter.

|     |     |
| --- | --- |
| **Key** | **Value** |
| `id` | 2244994945 (user ID) |

#### Step three: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default [List object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/lists) fields in your response: `id` and `name`.

If you would like to receive additional fields beyond `id` and `name`, you will have to specify those fields in your request with the [`field`](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields) and/or [`expansion`](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request a three additional sets of fields from different objects:

* The additional `follower_count` field in the primary List object.
* The full [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) using the expansion parameter.
* The additional  `tweet.created_at` field in the associated user object.
    

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| Key | Value | Returned fields |
| list.fields | follower\_count | `follower_count` |
| expansions | owner\_id | `includes.users.id,   includes.users.name,   includes.users.username` |
| user.fields | created\_at | `includes.users.created_at` |

You should now see a similar URL next to the “Send” button:

      `https://api.twitter.com/2/users/2244994945/pinned_lists?expansions=owner_id&list.fields=follower_count&user.fields=created_at`
    

Step four: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": [     {       "follower_count": 0,       "id": "1454155907651158017",       "name": "test list",       "owner_id": "2244994945"     }   ],   "includes": {     "users": [       {         "username": "TwitterDev",         "id": "2244994945",         "created_at": "2013-12-14T04:35:55.000Z",         "name": "Twitter Dev"       }     ]   },   "meta": {     "result_count": 1   } }`