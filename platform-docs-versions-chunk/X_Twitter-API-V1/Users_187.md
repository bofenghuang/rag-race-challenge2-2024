platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/user-profile-images-and-banners

### Default profile images[¶](#default-profile-images "Permalink to this headline")

Some users may not have uploaded a profile image. Users who have not uploaded a profile image can be identified by the `default_profile_image` field of their user object having a `true` value.

The `profile_image_url` and `profile_image_url_https` URLs provided for users in this case will indicate Twitter’s default profile photo, which is [https://abs.twimg.com/sticky/default\_profile\_images/default\_profile\_normal.png](https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png).

The table above can be used to determine how to retrieve different size variants of the default image.