platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference/post-tweets


### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `direct_message_deep_link`  <br> Optional | string | [Tweets a link directly to a Direct Message conversation](https://business.twitter.com/en/help/campaign-editing-and-optimization/public-to-private-conversation.html) with an account.  <br>  <br>Example: `{"text": "Tweeting a DM deep link!", "direct_message_deep_link": "https://twitter.com/messages/compose?recipient_id=2244994945"}` |
| `for_super_followers_only`  <br> Optional | boolean | Allows you to Tweet exclusively for [Super Followers](https://help.twitter.com/en/using-twitter/super-follows).  <br>  <br>Example: `{"text": "Hello World!", "for_super_followers_only": true}` |
| `geo`  <br> Optional | object | A JSON object that contains location information for a Tweet. You can only add a location to Tweets if you have geo enabled in your profile settings. If you don't have geo enabled, you can still add a location parameter in your request body, but it won't get attached to your Tweet |
| `geo.place_id`  <br> Optional | string | Place ID being attached to the Tweet for geo location.  <br>  <br>Example: `{"text": "Tweeting with geo!","geo": {"place_id": "5a110d312052166f"}}` |
| `media`  <br> Optional | object | A JSON object that contains media information being attached to created Tweet. This is mutually exclusive from Quote Tweet ID and Poll. |
| `media.media_ids`  <br> Optional | array | A list of Media IDs being attached to the Tweet. This is only required if the request includes the `tagged_user_ids`.  <br>  <br>Example: `{"text": "Tweeting with media!", "media": {"media_ids": ["1455952740635586573"]}}` |
| `media.tagged_user_ids`  <br> Optional | array | A list of User IDs being tagged in the Tweet with Media. If the user you're tagging doesn't have photo-tagging enabled, their names won't show up in the list of tagged users even though the Tweet is successfully created.  <br>  <br>Example: `{"text": "Tagging users in images!", "media": {"media_ids": ["1455952740635586573"], "tagged_user_ids": ["2244994945","6253282"]}}` |
| `poll`  <br> Optional | object | A JSON object that contains options for a Tweet with a poll. This is mutually exclusive from Media and Quote Tweet ID. |
| `poll.duration_minutes`  <br> Optional | number | Duration of the poll in minutes for a Tweet with a poll. This is only required if the request includes `poll.options`.  <br>  <br>Example: `{"text": "Tweeting with polls!", "poll": {"options": ["yes", "maybe", "no"], "duration_minutes": 120}}` |
| `poll.options`  <br> Optional | array | A list of poll options for a Tweet with a poll. For the request to be successful it must also include `duration_minutes` too.  <br>  <br>Example: `{"text": "Tweeting with polls!", "poll": {"options": ["yes", "maybe", "no"], "duration_minutes": 120}}"` |
| `quote_tweet_id`  <br> Optional | string | Link to the Tweet being quoted.  <br>  <br>Example: `{"text": "Yay!", "quote_tweet_id": "1455953449422516226"}` |
| `reply`  <br> Optional | object | A JSON object that contains information of the Tweet being replied to. |
| `reply.exclude_reply_user_ids`  <br> Optional | array | A list of User IDs to be excluded from the reply Tweet thus removing a user from a thread.  <br>  <br>Example: `{"text": "Yay!", "reply": {"in_reply_to_tweet_id": "1455953449422516226", "exclude_reply_user_ids": ["6253282"]}}` |
| `reply.in_reply_to_tweet_id`  <br> Optional | string | Tweet ID of the Tweet being replied to. Please note that `in_reply_to_tweet_id` needs to be in the request if `exclude_reply_user_ids` is present.  <br>  <br>Example: `{"text": "Excited!", "reply": {"in_reply_to_tweet_id": "1455953449422516226"}}` |
| `reply_settings`  <br> Optional | string | [Settings](https://blog.twitter.com/en_us/topics/product/2020/new-conversation-settings-coming-to-a-tweet-near-you) to indicate who can reply to the Tweet. Options include "mentionedUsers" and "following". If the field isn’t specified, it will default to everyone.  <br>  <br>Example:`{"text": "Tweeting with reply settings!", "reply_settings": "mentionedUsers"}` |
| `text`  <br> Optional | string | Text of the Tweet being created. This field is required if `media.media_ids` is not present.  <br>  <br>Example: `{"text": "Hello World!"}` |