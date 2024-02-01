platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/copyright-detection

## Check a published video

To check the copyright status for a video that has been published, send a `GET` request to the `/{ig-media-id}` endpoint with the `fields` parameter set to `copyright_check_information`.

### Sample Request

curl \-i \-X GET "https://graph.facebook.com/`v19.0`/{ig-media-id}?fields=copyright\_check\_information"
    

On success, your app receives a JSON response with the `id` set to the video being checked and the `copyright_check_information` object with the following:

* `status` set to a `status` object set to `completed`, `error`, `in_progress`, or `not_started`
* `copyright_matches` set to:
    * `false` – Returned when no copyright violations are detected
    * `true` – Returned when copyright violations are detected and includes the `copyright_check_information` object that contains information about the copyright owner, policy, mitigation steps, and sections of the media that violated the copyright.