platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

{

"data": [

{

"actionDate": "2022-08-26",

"actionTaken": "ACTION_ADVERTISING_REMOVED",

"reason": "REASON_TOS_INCOMPATABILITY",

"basis": "Government order.",

"details": "Incompatible with Terms and Conditions.",

"firstImpressionDate": "2022-08-25",

"affectedPlacements": [

{

"placement": "APPSTORE_TODAY_TAB",

"countriesOrRegions": [

"BE",

"FR"

]

}

],

"audienceRefinement": {

"ageTarget": true,

"genderTarget": false,

"locationTarget": true,

"customerTypeTarget": false

}

}

],

"dataStartDate": "2022-01-01",

"dataEndDate": "2022-09-01",

"pagination": {

"totalResults": 2,

"startIndex": 0,

"itemsPerPage": 50

}

}



Ad Repository API January 2024 21

Response properties



Parameter Type Description



actionDate string The date the restriction was enforced.



actionTaken string

The action taken on the restriction, Values are:

ACTION_ACCOUNT_SUSPENDED

ACTION_ADVERTISING_REMOVED



reason string