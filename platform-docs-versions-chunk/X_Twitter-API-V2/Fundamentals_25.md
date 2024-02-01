platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place


###   
Retrieving a place object

#### Sample Request

In the following request, we are requesting fields for the place object attached to the Tweet on the [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup) endpoint. Since place is a child object of a Tweet, the `geo.place_id` expansion is required. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl --request GET 'https://api.twitter.com/2/tweets?ids=1136048014974423040&expansions=geo.place_id&place.fields=contained_within,country,country_code,full_name,geo,id,name,place_type' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

####   
Sample Response  
 

      `{     "data": [         {             "text": "We’re sharing a live demo of the new Twitter Developer Labs program, led by a member of our DevRel team, @jessicagarson #TapIntoTwitter https://t.co/ghv7f4dW5M",             "id": "1136048014974423040",             "geo": {                 "place_id": "01a9a39529b27f36"             }         }     ],     "includes": {         "places": [             {                 "geo": {                     "type": "Feature",                     "bbox": [                         -74.026675,                         40.683935,                         -73.910408,                         40.877483                     ],                     "properties": {}                 },                 "country_code": "US",                 "name": "Manhattan",                 "id": "01a9a39529b27f36",                 "place_type": "city",                 "country": "United States",                 "full_name": "Manhattan, NY"             }         ]     } }`