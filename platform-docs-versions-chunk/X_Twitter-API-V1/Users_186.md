platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/user-profile-images-and-banners


### Alternative image sizes for user profile images[¶](#alternative-image-sizes-for-user-profile-images "Permalink to this headline")

Obtain a user’s most recent profile image, along with the other components comprising their identity on Twitter, from [GET users/show](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show). The [user object](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/data-dictionary/overview/user-object) contains the `profile_image_url` and `profile_image_url_https` fields. These fields will contain the resized “normal” variant of the user’s uploaded image. This “normal” variant is typically 48px by 48px.

By modifying the URL, it is possible to retrieve other variant sizings such as “bigger”, “mini”, and “original”. Consult the table below for more examples:

|     |     |     |
| --- | --- | --- |
| Variant | Dimensions | Example URL |
| normal | 48x48 | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_normal.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_normal.png |
| bigger | 73x73 | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_bigger.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_bigger.png |
| mini | 24x24 | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_mini.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_mini.png |
| original | original | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3.png  <br>_Omit the underscore and variant to retrieve the original image. The images can be very large._ |