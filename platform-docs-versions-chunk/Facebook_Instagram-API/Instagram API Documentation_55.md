platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/copyright-detection

# Copyright Detection

This guide shows you how to detect copyright violations for a video uploaded or published to Instagram using the Instagram Graph API.

## Before you start

Before you start you will need the following:

* All requirements and limitations for accessing the Instagram Container and Instagram Media endpoints apply

### Best practices

When testing an API call, you can include the `access_token` parameter set to your access token. However, when making secure calls from your app, use the [access token class.](https://developers.facebook.com/docs/facebook-login/guides/access-tokens#portabletokens)

## Check an uploaded video

To check the copyright status for a video that have been uploaded, but not yet published, send a `GET` request to the `/{ig-containter-id}` endpoint with the `fields` parameter set to `copyright_check_status`.