platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update_with_media


## Parameters[¶](#parameters "Permalink to this headline")

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| status | required | The text of your status update. URL encode as necessary. [t.co link wrapping](https://developer.twitter.com/en/docs/basics/tco) may affect character counts if the post contains URLs. You must additionally account for the `characters_reserved_per_media` per uploaded media, additionally accounting for space characters in between finalized URLs. **Note** : Request the `GET help / configuration &lt;/en/docs/developer-utilities/configuration/api-reference/get-help-c current` characters\_reserved\_per\_media`and`max\_media\_per\_upload\` values. |     | onfiguration>\`\_\_ endpoint to get the |
| media\[\] | required | Up to `max_media_per_upload` files may be specified in the request, each named `media[]` . Supported image formats are PNG, JPG and GIF, including animated GIFs of up to 3MB . This data must be either the raw image bytes or encoded as base64. **Note** : Request the `GET help / configuration &lt;/en/docs/developer-utilities/configuration/api-reference/get-help-c current` max\_media\_per\_upload`and`photo\_size\_limit\` values. | onfiguration>\`\_\_ endpoint to get the |     |
| possibly\_sensitive | optional | Set to `true` for content which may not be suitable for every audience. |     |     |
| in\_reply\_to\_status\_id | optional | The ID of an existing status that the update is in reply to. **Note** : This parameter will be ignored unless the author of the Tweet this parameter references is mentioned within the status text. Therefore, you must include `@username` , where `username` is the author of the referenced Tweet, within the update. |     |     |
| lat | optional | The latitude of the location this Tweet refers to. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there isn't a corresponding `long` parameter. |     | `37.7821120598956` |
| long | optional | The longitude of the location this Tweet refers to. The valid ranges for longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, not a number, `geo_enabled` is turned off, or if there not a corresponding `lat` parameter. |     | `-122.400612831116` |
| place\_id | optional | A place in the world identified by a Twitter place ID. Place IDs can be retrieved from geo/reverse\_geocode. |     | `df51dec6f4ee2b2c` |
| display\_coordinates | optional | Whether or not to put a pin on the exact coordinates a Tweet has been sent from. |     | `true` |
| enable\_dmcommands | optional | When set to `true`, enables shortcode commands for sending Direct Messages as part of the status text to send a Direct Message to a user. When set to `false`, it turns off this behavior and includes any leading characters in the status text. | > `true` | `true` |
| fail\_dmcommands | optional | When set to `true`, causes any status text that starts with shortcode commands to return an API error. When set to `false`, allows shortcode commands to be sent in the status text and acted on by the API. | > `false` | `false` |