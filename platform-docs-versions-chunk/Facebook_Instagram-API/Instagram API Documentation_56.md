platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/copyright-detection

### Sample Request

curl \-i \-X GET "https://graph.facebook.com/`v19.0`/{ig-containter-id}?fields=copyright\_check\_status"
    

On success, your app receives a JSON response with a `copyright_check_status` object with the following key-value pairs:

* `status` set to `completed`, `error`, `in_progress`, or `not_started`
* `matches_found` set to:
    * `false` if none are detected
    * `true` if violations are detected and `author`, `content_title`, `matched_segments`, and `owner_copyright_policy` values

### Sample Responses

|     |     |
| --- | --- |
| #### Violation found<br><br>{<br>  "copyright\_check\_status": {<br>    "status": "complete",<br>    "matches\_found": true<br>  },<br>  "id": "{ig-containter-id}"<br>} | #### No violation found<br><br>{<br>  "copyright\_check\_status": {<br>      "status": "in\_progress",<br>      "matches\_found": false<br>  }<br>} |

[](#)