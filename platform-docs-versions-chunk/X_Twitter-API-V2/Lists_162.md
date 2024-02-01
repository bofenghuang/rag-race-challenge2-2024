platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/quick-start/manage-pinned-lists


### Steps to build a manage pinned List request

#### Step one: Choose the List endpoint collection from Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “Pinned Lists”, and then choose "Pin a List".  
 

#### Step two: Specify the List to pin

Manage pinned List endpoints require two IDs: one for the user (the authenticated user to pin a List) and the target List (the List to be pinned). The user’s ID must correspond to the authenticating user’s ID, meaning that you must pass the Access Tokens associated with the user ID when authenticating your request. In this case, you can specify the ID belonging to your user. You can find your ID in two ways:

1. Using the [users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference) by username endpoint, you can pass a username and receive the id field.
2. Looking at your Access Token, you will find that the numeric part is your user ID.

The target List ID can be any valid list. In Postman, navigate to the "Params" tab, and enter the user ID into the "Value" column of the id path variable. Navigate to the “Body” tab and ID of the List you wish to pin as the value for the list\_id  parameter. Be sure not to include any spaces before or after any ID.

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Parameter type** |
| `id` | The user ID | path |
| list\_id | The target List ID to be pinned | body |

You should now see a similar URL next to the "Send" button:

      `https://api.twitter.com/2/users/2244994945/pinned_lists`
    

Step three: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": {     "pinned": true   } }`
    

You have successfully pinned the target List if the returned response object contains a true value for the key pinned. 

To unpin a List, select the Unpin List” request also found in the “Lists” folder of the Twitter API v2 collection loaded in Postman. This endpoint requires the authenticated user ID and the ID of the List to be unpinned. In the “Params” tab, enter the user ID as the value for the id column and ID of the List to be unpinned as the value for the  list\_id column. 

On successful delete request, you will receive a response similar to the following example:

      `{   "data": {     "pinned": false   } }`