platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update


## Parameters[¶](#parameters "Permalink to this headline")

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| status | required | The text of the status update. URL encode as necessary. [t.co link wrapping](https://developer.twitter.com/en/docs/basics/tco) will affect character counts. |     |     |
| in\_reply\_to\_status\_id | optional | The ID of an existing status that the update is in reply to. **Note:** This parameter will be ignored unless the author of the Tweet this parameter references is mentioned within the status text. Therefore, you must include `@username` , where `username` is the author of the referenced Tweet, within the update. |     |     |
| auto\_populate\_reply\_metadata | optional | If set to `true` and used with `in_reply_to_status_id`, leading `@mentions` will be looked up from the original Tweet, and added to the new Tweet from there. This wil append `@mentions` into the metadata of an extended Tweet as a reply chain grows, until the limit on `@mentions` is reached. In cases where the original Tweet has been deleted, the reply will fail. | > `false` | > `true` |
| exclude\_reply\_user\_ids | optional | When used with `auto_populate_reply_metadata`, a comma-separated list of user ids which will be removed from the server-generated `@mentions` prefix on an extended Tweet. Note that the leading `@mention` cannot be removed as it would break the `in-reply-to-status-id` semantics. Attempting to remove it will be silently ignored. |     | > `786491,54931584` |
| attachment\_url | optional | In order for a URL to not be counted in the status body of an extended Tweet, provide a URL as a Tweet attachment. This URL must be a Tweet permalink, or Direct Message deep link. Arbitrary, non-Twitter URLs must remain in the status text. URLs passed to the `attachment_url` parameter not matching either a Tweet permalink or Direct Message deep link will fail at Tweet creation and cause an exception. |     | > `https://twitter.com/andypiper/status/903615884664725505` |
| media\_ids | optional | A comma-delimited list of `media_ids` to associate with the Tweet. You may include up to 4 photos or 1 animated GIF or 1 video in a Tweet. See [Uploading Media](https://developer.twitter.com/en/docs/media/upload-media/overview) for further details on uploading media. |     | `471592142565957632` |
| possibly\_sensitive | optional | If you upload Tweet media that might be considered sensitive content such as nudity, or medical procedures, you must set this value to `true`. If this parameter is included in your request, it will override the user’s preferences. Including any value other than `true`, `1`, or `t` will be interpreted as `false`. See [Media setting and best practices](https://support.twitter.com/articles/20169200) for more context. | > If left unspecified, the value applied to the newly created Tweet is derived from the user's preferences. | `true` |
| lat | optional | The latitude of the location this Tweet refers to. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there is no corresponding `long` parameter. |     | `37.7821120598956` |
| long | optional | The longitude of the location this Tweet refers to. The valid ranges for longitude are -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, if it is not a number, if `geo_enabled` is turned off, or if there no corresponding `lat` parameter. |     | `-122.400612831116` |
| place\_id | optional | A [place](https://developer.twitter.com/en/docs/geo/place-information/overview) in the world. |     | `df51dec6f4ee2b2c` |
| display\_coordinates | optional | Whether or not to put a pin on the exact coordinates a Tweet has been sent from. |     | `true` |
| trim\_user | optional | When set to either `true` , `t` or `1` , the response will include a user object including only the author's ID. Omit this parameter to receive the complete user object. | > `false` | `true` |
| card\_uri | optional | Associate an ads card with the Tweet using the `card_uri` value from any ads card response. |     | `card://853503245793641682` |