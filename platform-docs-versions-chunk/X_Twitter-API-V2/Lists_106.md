platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/quick-start/manage-list-members


### Steps to build a manage List member request

#### Step one: Choose the List endpoint collection from Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “List members”, and then choose "Add a member".  
 

#### Step two: Specify the user to add

Manage List member endpoints require two IDs: the ID of the List and the ID of the user to add. You can find the user’s ID using the [users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference) and pass a username to receive the id field.

The target ID can be any valid user ID. In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the id path variable. Navigate to the “Body” tab and ID of the user you wish to add as the value for the user\_id parameter. Be sure not to include any spaces before or after any ID.

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Parameter type** |
| `id` | The List ID | path |
| user\_id | The target user ID you wish to add as a member | body |

You should now see a similar URL next to the "Send" button:

      `https://api.twitter.com/2/lists/1441162269824405510/members`
    

Step three: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": {     "is_member": true   } }`
    

If the returned response object contains a true value for the key is\_member, you have successfully added the user as a member of the List. 

To remove a member from a List, select the “Remove a member” request also found in the “Lists” folder of the Twitter API v2 collection loaded in Postman. This endpoint requires the ID of the List and the user ID of the member you wish to remove. In the “Params” tab, enter the ID of the List as the value for the id column and ID of the user to be removed as the value for the  user\_id column. 

On successful delete request, you will receive a response similar to the following example:

      `{   "data": {     "is_member": false   } }`