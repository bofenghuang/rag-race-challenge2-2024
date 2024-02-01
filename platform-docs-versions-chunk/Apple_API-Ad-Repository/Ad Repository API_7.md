platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

offset integer no The offset pagination that limits the number of returned

records. The default is 0.



limit integer no The maximum number of entries to return per page. The

default is 50.



Ad Repository API January 2024 4

Response example

The AdRepositoryEntity object is returned:



{

"data": [

{

"id": 1582276305,

"name": "TripTrek",

"type": "APP"

},

{

"id": 819221,

"name": "Trip Trek, Inc.",

"type": "DEVELOPER"

}

],

"pagination": {

"totalResults": 2,

"startIndex": 0,

"itemsPerPage": 15

}

}



Ad Repository API January 2024 5

Response properties



Parameter Type Description



id integer A unique identifier. If the type is APP , the id will be an appId . If

the type is DEVELOPER, the id is a developerId.



name string The entity name on whose behalf the advertising was presented.



type string Values are APP , DEVELOPER



pagination integer Returned pagination results.



totalResults: The total number of entries that return for the

operation.