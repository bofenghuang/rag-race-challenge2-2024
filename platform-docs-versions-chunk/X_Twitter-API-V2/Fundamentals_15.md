platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/list


## List

The list object contains [Twitter Lists](https://help.twitter.com/en/using-twitter/twitter-lists) metadata describing the referenced List. The List object is the primary object returned in the List lookup endpoint. When requesting additional List fields on this endpoint, simply use the fields parameter `list.fields`.

At the moment, the List object cannot be found as a child object from any other data object. However, user objects can be found and expanded in the user resource. These objects are available for expansion by adding owner\_id to the expansions query parameter. Use the expansion with the field parameter: `list.fields` when requesting additional fields to complete the primary List object and user.fields to complete the expansion object.  
 

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- | --- |
| id (default) | string | The unique identifier of this List.<br><br>`"id": "2244994945"` | Use this to programmatically retrieve information about a specific Twitter List. |
| name (default) | string | The name of the List, as defined when creating the List. <br><br>`"name": "Twitter Lists"` |     |
| created\_at | date (ISO 8601) | The UTC datetime that the List was created on Twitter.<br><br>`"created_at": "2013-12-14T04:35:55.000Z"` | Can be used to determine how long a List has been on Twitter |
| description | string | A brief description to let users know about the List.<br><br>`"description": "People that are active members of the Bay area cycling community on Twitter."` |     |
| follower\_count | integer | Shows how many users follow this List,<br><br>"follower\_count": 198 |     |
| member\_count | integer | Shows how many members are part of this List.<br><br>"member\_count": 60 |     |
| private | boolean | Indicates if the List is private.<br><br>"private": false |     |
| owner\_id | string | Unique identifier of this List's owner.<br><br>`"owner_id": "1255542774432063488"` | Returns the List owner ID. Can potentially be used to find out if this specifc user owns any other Lists.<br><br>Can also be used to expand user objects. |     |