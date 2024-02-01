platform: X
topic: Twitter-API-Overview
subtopic: Migrate
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Overview/Migrate.md
url: https://developer.twitter.com/en/docs/twitter-api/migrate/whats-new


### Discover new and updated response objects

The following six data objects are available with the v2 endpoints:

| **Object** | **Description** |
| --- | --- |
| **[Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet)** | The Tweet object has a long list of root-level fields, such as id, text, and created\_at. Tweet objects are also the parent object to several child objects including user, media, poll, and place. |
| **[User](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user)** | The user object contains X user account metadata describing the referenced user. |
| **[Spaces](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space)** | The Space object consists of fields such as state, host\_id, is\_ticketed, and even lang. |
| **[Lists](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space)** | The List object contains basic information about the requested list including description, member\_count, and owner\_id. |
| **[Media](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media)** | If a Tweet contains media (such as images), then the media object can be requested using the media.fields parameter and includes fields such as the media\_key, type, url, preview\_image\_url, and more. |
| **[Poll](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll)** | A poll included in a Tweet is not a primary object on any endpoint, but can be found and expanded in the Tweet object. |
| **[Place](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place)** | The place object consists of fields such as place\_id, geo object, country\_code, and more. This information can be used to identify Tweets and study Tweets by location. |