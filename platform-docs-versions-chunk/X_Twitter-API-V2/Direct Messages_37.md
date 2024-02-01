platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/api-reference/get-dm_conversations-with-participant_id-dm_events


### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | The `id` of the Direct Message event. |
| `text` | string | The text included in the Direct Message. |
| `event_type` | string | The type of event. Possible values include MessageCreate, ParticipantsJoin, ParticipantsLeave. |
| `created_at` | date (ISO 8601) | The `timestamp` of the Direct Message event creation. |
| `sender_id` | string | The `id` of the user who sent the Direct Message. |
| `dm_conversation_id` | string | The `id` of the conversation the Direct Message belongs to. |
| `attachments` | object | The attached urls and media information for expansion. E.g. Media, Tweet, Card |
| `attachments.media_keys` | array | List of unique identifiers of media attached to a direct message. These identifiers use the same media key format as those returned by the [Media Library](https://developer.twitter.com/en/docs/ads/creatives/guides/media-library).  <br>  <br>You can obtain the expanded object in `includes.media` by adding `expansions=attachments.media_keys` in the request's query parameter. |
| `referenced_tweets` | array | Expansion of a "shared" Tweet in the Direct Message. If the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent. |
| `referenced_tweets.id` | string | The `id` of a "shared" Tweet in the Direct Message.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=referenced_tweets.id` in the request's query parameter. |
| `media.fields` | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `non_public_metrics`, `organic_metrics`, `promoted_metrics`, `alt_text`, `variants`) | Expansion of included media with its own fields. E.g. url, size, etc. When including the `expansions=attachments.media_keys` parameter, this includes a list of images, videos, and GIFs included in Tweets in the form of [media objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) with their default fields and any additional fields requested using the `media.fields` parameter, assuming there is a media attachment present in the returned Tweet(s).  <br>  <br>You can obtain the expanded object in `includes.media` by adding `expansions=media.fields` in the request's query parameter. |
| `user.fields` | string | The Expansion of user object via `sender_id`.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=user.fields` in the request's query parameter. |
| `meta` | object | This object contains information about the number of messages returned in the current request and pagination details. |
| `meta.next_token` | string | A value that encodes the next 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `meta.previous_token` | string | A value that encodes the previous 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `meta.result_count` | number | The number of results in the current page. |
| `errors` | object | Contains details about errors in a request for messages in a specified conversation. |