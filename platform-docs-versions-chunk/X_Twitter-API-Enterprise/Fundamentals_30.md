platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user


### User Data Dictionary

| Attribute | Type | Description |
| --- | --- | --- |
| id  | Int64 | The integer representation of the unique identifier for this User. This number is greater than 53 bits and some programming languages may have difficulty/silent defects in interpreting it. Using a signed 64 bit integer for storing this identifier is safe. Use `id_str` to fetch the identifier to be safe. See [Twitter IDs](https://developer.twitter.com/en/docs/twitter-ids) for more information. Example:<br><br>"id": 6253282 |
| id\_str | String | The string representation of the unique identifier for this User. Implementations should use this rather than the large, possibly un-consumable integer in `id`. Example:<br><br>"id\_str": "6253282" |
| name | String | The name of the user, as they’ve defined it. Not necessarily a person’s name. Typically capped at 50 characters, but subject to change. Example:<br><br>"name": "Twitter API" |
| screen\_name | String | The screen name, handle, or alias that this user identifies themselves with. screen\_names are unique but subject to change. Use `id_str` as a user identifier whenever possible. Typically a maximum of 15 characters long, but some historical accounts may exist with longer names. Example:<br><br>"screen\_name": "twitterapi" |
| location | String | _Nullable_ . The user-defined location for this account’s profile. Not necessarily a location, nor machine-parseable. This field will occasionally be fuzzily interpreted by the Search service. Example:<br><br>"location": "San Francisco, CA" |
| derived | Arrays of Enrichment Objects | Enterprise APIs only Collection of Enrichment metadata derived for user. Provides the [_Profile Geo_](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo) Enrichment metadata. See referenced documentation for more information, including JSON data dictionaries. Example:<br><br>"derived":{"locations": \[{"country":"United States","country\_code":"US","locality":"Denver"}\]} |
| url | String | _Nullable_ . A URL provided by the user in association with their profile. Example:<br><br>"url": "https://developer.twitter.com" |
| description | String | _Nullable_ . The user-defined UTF-8 string describing their account. Example:<br><br>"description": "The Real Twitter API." |
| protected | Boolean | When true, indicates that this user has chosen to protect their Tweets. See [About Public and Protected Tweets](https://support.twitter.com/articles/14016-about-public-and-protected-tweets) . Example:<br><br>"protected": true |
| verified | Boolean | When true, indicates that the user has a verified account. See [Verified Accounts](https://support.twitter.com/articles/119135-faqs-about-verified-accounts) . Example:<br><br>"verified": false |
| followers\_count | Int | The number of followers this account currently has. Under certain conditions of duress, this field will temporarily indicate “0”. Example:<br><br>"followers\_count": 21 |
| friends\_count | Int | The number of users this account is following (AKA their “followings”). Under certain conditions of duress, this field will temporarily indicate “0”. Example:<br><br>"friends\_count": 32 |
| listed\_count | Int | The number of public lists that this user is a member of. Example:<br><br>"listed\_count": 9274 |
| favourites\_count | Int | The number of Tweets this user has liked in the account’s lifetime. British spelling used in the field name for historical reasons. Example:<br><br>"favourites\_count": 13 |
| statuses\_count | Int | The number of Tweets (including retweets) issued by the user. Example:<br><br>"statuses\_count": 42 |
| created\_at | String | The UTC datetime that the user account was created on Twitter. Example:<br><br>"created\_at": "Mon Nov 29 21:18:15 +0000 2010" |
| profile\_banner\_url | String | The HTTPS-based URL pointing to the standard web representation of the user’s uploaded profile banner. By adding a final path element of the URL, it is possible to obtain different image sizes optimized for specific displays. For size variants, please see [User Profile Images and Banners](https://developer.twitter.com/en/docs/accounts-and-users/user-profile-images-and-banners) .<br><br>Example:<br><br>"profile\_banner\_url": "https://si0.twimg.com/profile\_banners/819797/1348102824" |
| profile\_image\_url\_https | String | A HTTPS-based URL pointing to the user’s profile image. Example:<br><br>"profile\_image\_url\_https":<br>"https://abs.twimg.com/sticky/default\_profile\_images/default\_profile\_normal.png" |
| default\_profile | Boolean | When true, indicates that the user has not altered the theme or background of their user profile. Example:<br><br>"default\_profile": false |
| default\_profile\_image | Boolean | When true, indicates that the user has not uploaded their own profile image and a default image is used instead. Example:<br><br>"default\_profile\_image": false |