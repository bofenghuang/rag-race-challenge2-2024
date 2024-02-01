platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_banner

POST account/update\_profile\_banner

post-account-update\_profile\_banner

# POST account/update\_profile\_banner

Uploads a profile banner on behalf of the authenticating user. More information about sizing variations can be found in [User Profile Images and Banners](https://developer.twitter.com/en/docs/accounts-and-users/user-profile-images-and-banners) and [GET users / profile\_banner](https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-users-profile_banner).

Profile banner images are processed asynchronously. The profile\_banner\_url and its variant sizes will not necessary be available directly after upload.

## HTTP Response Codes[¶](#http-response-codes "Permalink to this headline")

|     |     |
| --- | --- |
| Code(s) | Meaning |
| 200, 201, 202 | Profile banner image successfully uploaded |
| 400 | Either an image was not provided, or the image data could not be processed |
| 422 | The image could not be resized, or is too large. |