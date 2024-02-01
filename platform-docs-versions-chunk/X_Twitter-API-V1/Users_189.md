platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/user-profile-images-and-banners


## Profile banners[¶](#profile-banners "Permalink to this headline")

Profile banners allow users to further customize the expressiveness of their profiles. Use [POST account/update\_profile\_banner](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_banner) to upload a profile banner on behalf of a user.

Profile banners come in a variety of display-enhanced sizes. The variant sizes are available through a request to [GET users/profile\_banner](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/manage-account-settings/api-reference/get-users-profile_banner) or by modifying the final path component of the `profile_banner_url` found in a user object according to the table below.

The profile banner data available at each size variant’s URL is in PNG format.

The following sizes are available:

|     |     |
| --- | --- |
| Dimensions | Example URL |
| 1500x500 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/1500x500 |
| 600x200 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/600x200 |
| 300x100 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/300x100 |

The following sizes are available for the certain screen types:

|     |     |     |
| --- | --- | --- |
| Screen Type | Dimensions | Example URL |
| web | 520x260 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/web |
| web\_retina | 1040x520 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/web\_retina |
| ipad | 626x313 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/ipad |
| ipad\_retina | 1252x626 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/ipad\_retina |
| mobile | 320x160 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/mobile |
| mobile\_retina | 640x320 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/mobile\_retina |