platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/live_media

### cURL Example

#### Request

curl -X GET \\
  'https://graph.facebook.com/`v19.0`/17841405822304914/live\_media?fields=id,media\_type,media\_product\_type,owner,username,comments&access\_token=IGQVJ...'

#### Response

{
   "id":"90010498116233",
   "media\_type":"BROADCAST",
   "media\_product\_type":"LIVE",
   "owner":{
      "id":"17841405822304914"
   },
   "username":"jayposiris",
   "comments":{
      "data":\[
        {
            "hidden": false,
            "id": "17907364514064687",
            "like\_count": 0,
            "media": {
                "id": "17892642502701087"
            },
            "text": "@jayposiris",
            "timestamp": "2021-08-17T21:23:07+0000",
            "username": "bztest0316\_11",
            "from": {
                "id": "5895605157123796",
                "username": "bztest0316\_11"
            }
        }
      \]
   }
}

## Updating

This operation is not supported.