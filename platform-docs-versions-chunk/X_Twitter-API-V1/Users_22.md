platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_banner


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| banner | required | The Base64-encoded or raw image data being uploaded as the user's new profile banner. |     |     |
| width | optional | The width of the preferred section of the image being uploaded in pixels. Use with _height_ , _offset\_left_ , and _offset\_top_ to select the desired region of the image to use. |     |     |
| height | optional | The height of the preferred section of the image being uploaded in pixels. Use with _width_ , _offset\_left_ , and _offset\_top_ to select the desired region of the image to use. |     |     |
| offset\_left | optional | The number of pixels by which to offset the uploaded image from the left. Use with _height_ , _width_ , and _offset\_top_ to select the desired region of the image to use. |     |     |
| offset\_top | optional | The number of pixels by which to offset the uploaded image from the top. Use with _height_ , _width_ , and _offset\_left_ to select the desired region of the image to use. |     |     |