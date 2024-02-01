platform: X
topic: Twitter-API-V2
subtopic: Spaces
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Spaces.md
url: https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-by-creator-ids


### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `user_ids`  <br> Required | string | A comma separated list of user IDs (up to 100). |
| `expansions`  <br> Optional | enum (`invited_user_ids`, `speaker_ids`, `creator_id`, `host_ids`, `topics_ids`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned Space. Submit a list of desired expansions in a comma-separated list. The ID that represents the expanded data object will be included directly in the Space data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Space object.  <br>  <br>The following data objects can be expanded using this parameter:  <br><br>* The Spaces creator's user object<br>* The user objects of any Space co-host<br>* Any mentioned users’ object<br>* Any speaker's user object |
| `space.fields`  <br> Optional | enum (`host_ids`, `created_at`, `creator_id`, `id`, `lang`, `invited_user_ids`, `participant_count`, `speaker_ids`, `started_at`, `ended_at`, `subscriber_count`, `topic_ids`, `state`, `title`, `updated_at`, `scheduled_start`, `is_ticketed`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Space fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space) will deliver in each returned Space. Specify the desired fields in a comma-separated list. |
| `topic.fields`  <br> Optional | enum (`id`, `name`, `description`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific topic metadata in each returned Space topic object, if the creator of the Space set one or more topics. Specify the desired fields in a comma-separated list. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver in each returned Space. Specify the desired fields in a comma-separated list without spaces between commas and fields. While the user ID will be located in the original Space object, you will find this ID and all additional user fields in the `includes` data object. |