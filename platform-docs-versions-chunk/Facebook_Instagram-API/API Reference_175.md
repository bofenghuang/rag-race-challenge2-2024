platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_comment

### Fields

| Field | Description |
| --- | --- |
| `id`  <br>**Default**  <br>_String_ | ID of the IG Comment. |
| `like_count`  <br>_String_ | Number of times the IG Comment has been liked. |
| `media`  <br>_String_ | ID of the IG Media on which the IG Comment was made. Use [Field Expansion](#field-expansion) to get additional fields on the returned IG Media entity. |
| `text`  <br>**Default**  <br>_String_ | Text of the IG Comment. |
| `timestamp`  <br>**Default**  <br>_String_ | IG Comment creation date formatted in ISO 8601. |

### Response

### Sample Request

curl -X GET \\
  'https://graph.facebook.com/`v19.0`/17841405309211844?fields=mentioned\_comment.comment\_id(17873440459141021){timestamp,like\_count,text,id}&access\_token=IGQVJ...'

#### Sample Response

{
  "mentioned\_comment": {
    "timestamp": "2017-05-03T16:09:08+0000",
    "like\_count": 185,
    "text": "Shout out to @metricsaurus",
    "id": "17873440459141021"
  },
  "id": "17841405309211844"
}