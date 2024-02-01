platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/user-profile-images-and-banners

### Outdated profile images[¶](#outdated-profile-images "Permalink to this headline")

If a 403 or 404 error is returned when trying to access a profile image, refresh the [user object](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/data-dictionary/overview/user-object) using [GET users/show](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show) to retrieve the most recent `profile_image_url` or `profile_image_url_https`. The URL may have changed, which happens for instance when the user updates their profile image.