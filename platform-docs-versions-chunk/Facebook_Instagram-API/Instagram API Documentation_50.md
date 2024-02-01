platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/content-publishing

## Troubleshooting

If you are able to create a container for a video but the [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish#creating) endpoint does not return the published media ID, you can get the container's publishing status by querying the `GET /{ig-container-id}?fields=status_code` endpoint. This endpoint will return one of the following:

* `EXPIRED` — The container was not published within 24 hours and has expired.
* `ERROR` — The container failed to complete the publishing process.
* `FINISHED` — The container and its media object are ready to be published.
* `IN_PROGRESS` — The container is still in the publishing process.
* `PUBLISHED` — The container's media object has been published.

We recommend querying a container's status once per minute, for no more than 5 minutes.

[](#)

## Errors

See the [Error Codes](https://developers.facebook.com/docs/instagram-api/reference/error-codes) reference.

[](#)

[](#)