platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-users-id-list_memberships


### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`owner_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned List. The ID that represents the expanded data object will be included directly in the List data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original user object. At this time, the only expansion available to endpoints that primarily return List objects is `expansions=owner_id`. You will find the expanded user data object living in the `includes` response object. |
| `list.fields`  <br> Optional | enum (`created_at`, `follower_count`, `member_count`, `private`, `description`, `owner_id`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [List fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/lists) will deliver with each returned List objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified List fields will display directly in the List data objects. |
| `max_results`  <br> Optional | integer | The maximum number of results to be returned per page. This can be a number between 1 and 100. By default, each page will return 100 results. |
| `pagination_token`  <br> Optional | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the next\_token returned in your previous response. To go back one page, pass the previous\_token returned in your previous response. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with the users object. Specify the desired fields in a comma-separated list without spaces between commas and fields. The user fields will only be returned if you have included `expansions=owner_id` query parameter in your request. You will find this ID and all additional user fields in the `included` data object. |