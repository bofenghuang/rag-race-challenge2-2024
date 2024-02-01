platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/quick-start


### Step three: Specify the name for the new List  

When creating a new List with this endpoint, a name for the List is a required body parameter. Optionally, you can provide a description and specify whether the List is private.

In Postman, navigate to the “Body” tab and enter the name of the List as the value for the name parameter. Additionally, if you wish to add a description for the List, simply add a new key labeled description in the same fashion as the name, followed by the description of the List as the value. Making a List private will follow the same pattern, but only true or false values are accepted for this parameter. 

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Parameter type** |
| `name` | Name of the list (required) | body |
| description | Description for the list (optional) | body |
| private | true or false (optional) | body |

You should now see a similar URL next to the "Send" button:

      `https://api.twitter.com/2/lists`
    

Step four: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": {     "id": "1441162269824405510",     "name": "New list created from Postman"   } }`
    

If the returned response object contains an id and the name of your List, you have successfully created the List. 

To delete a List, select the “Delete a List” request also found in the “Lists” folder of the Twitter API v2 collection loaded in Postman. This endpoint requires the ID of the List you wish to delete. In the “Params” tab, enter the ID of the List you wish to delete as the value for the id column. 

On successful delete request, you will receive a response similar to the following example: 

      `{   "data": {     "deleted": true   } }`