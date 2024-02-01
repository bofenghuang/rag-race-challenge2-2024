platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_image

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| image | required | The avatar image for the profile, base64-encoded. Must be a valid GIF, JPG, or PNG image of less than 700 kilobytes in size. Images with width larger than 400 pixels will be scaled down. Animated GIFs will be converted to a static GIF of the first frame, removing the animation. |     |     |
| include\_entities | optional | The _entities_ node will not be included when set to _false_ . |     | _false_ |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user objects. |     |     |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/account/update_profile_image.json?image=ABCDEFGH...`