platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-container


### Fields

| Field Name | Description |
| --- | --- |
| `copyright_check_status` | Used to determine if an uploaded video is violating copyright. Key-values pairs return include:<br><br>* `matches_found` set to one of the following:<br>    * `true` – the video is violating copyright<br>    * `false` – the video is not violating copyright<br>* `status` set to one of the following:<br>    * `completed` – the detection process has finished<br>    * `error` – an error occurred during the detection process<br>    * `in_progress` – the detection process is ongoing<br>    * `not_started` – the detection process has not started |
| `id` | Instagram Container ID, represented in code examples as `{instagram-container-id}` |
| `status` | Publishing status. If `status_code` is `ERROR`, this value will be an [error subcode](https://developers.facebook.com/docs/instagram-api/reference/error-codes). |
| `status_code` | The container's publishing status. Possible values:<br><br>  <br><br>* `EXPIRED` — The container was not published within 24 hours and has expired.<br>* `ERROR` — The container failed to complete the publishing process.<br>* `FINISHED` — The container and its media object are ready to be published.<br>* `IN_PROGRESS` — The container is still in the publishing process.<br>* `PUBLISHED` — The container's media object has been published. |