platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/actor


### Data Dictionary

| Attribute | Type | Description |
| --- | --- | --- |
| objectType | string | **"objectType":** "person" |
| id  | string | The string representation of the unique identifier for this author. Example:<br><br>"id:twitter.com:2244994945" |
| link |     | "http://www.twitter.com/TwitterDev |
| displayName | String | The name of the user, as they’ve defined it. Not necessarily a person’s name. Typically capped at 50 characters, but subject to change. Example:<br><br>**"displayName":** "Twitter Dev" |
| preferredUsername | string | The screen name, handle, or alias that this user identifies themselves with. Unique but subject to change. Use `id` as a user identifier whenever possible. Typically a maximum of 15 characters long, but some historical accounts may exist with longer names. Example:<br><br>**"preferredUsername":** "TwitterDev" |
| location | object | **"location": {**<br><br>          **"objectType":** "place"**,**<br><br>          **"displayName":** "127.0.0.1"<br><br>        **}** |
| links | array | _Nullable_ . A URL provided by the user in association with their profile. Example:<br><br>       **"links": \[**<br><br>          **{**<br><br>            **"href":** "https://developer.twitter.com/en/community"**,**<br><br>            **"rel":** "me"<br><br>          **}**<br><br>        **\]** |
| summary | string | _Nullable_ . The user-defined UTF-8 string describing their account. Example:<br><br>**"summary":** "The voice of the #TwitterDev team..." |
| protected | Boolean | When true, indicates that this user has chosen to protect their Tweets. See [About Public and Protected Tweets](https://support.twitter.com/articles/14016-about-public-and-protected-tweets) . Example:<br><br>"protected": true |
| verified | Boolean | When true, indicates that the user has a verified account. See [Verified Accounts](https://support.twitter.com/articles/119135-faqs-about-verified-accounts) . Example:<br><br>"verified": false |
| followersCount | Int | The number of followers this account currently has. Under certain conditions of duress, this field will temporarily indicate “0”. Example:<br><br>"followers\_count": 21 |
| friendsCount | Int | The number of users this account is following (AKA their “followings”). Under certain conditions of duress, this field will temporarily indicate “0”. Example:<br><br>"friends\_count": 32 |
| listedCount | Int | The number of public lists that this user is a member of. Example:<br><br>"listed\_count": 9274 |
| favoritesCount | Int | The number of Tweets this user has liked in the account’s lifetime. British spelling used in the field name for historical reasons. Example:<br><br>"favourites\_count": 13 |
| statusesCount | Int | The number of Tweets (including retweets) issued by the user. Example:<br><br>"statuses\_count": 42 |
| postedTime | date | The UTC datetime that the user account was created on Twitter. Example:<br><br>**"postedTime":** "2013-12-14T04:35:55.036Z" |
| image | string | A HTTPS-based URL pointing to the user’s profile image. Example:<br><br>**"image":** "https://pbs.twimg.com/profile\_images/1283786620521652229/lEODkLTh\_normal.jpg" |