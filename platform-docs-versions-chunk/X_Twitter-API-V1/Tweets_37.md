platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-oembed


## Parameters[¶](#parameters "Permalink to this headline")

| Name | Default | Description |
| --- | --- | --- |
| `url`required  <br>String |     | The URL of the Tweet to be embedded |
| `maxwidth`  <br>Int `[220..550]` | `325` | The maximum width of a rendered Tweet in whole pixels. A supplied value under or over the allowed range will be returned as the minimum or maximum supported width respectively; the reset width value will be reflected in the returned `width` property. Note that Twitter does not support the oEmbed `maxheight` parameter. Tweets are fundamentally text, and are therefore of unpredictable height that cannot be scaled like an image or video. Relatedly, the oEmbed response will not provide a value for `height`. Implementations that need consistent heights for Tweets should refer to the `hide_thread` and `hide_media` parameters below. |
| `hide_media`  <br>Boolean, String or Int | `false` | When set to `true`, `"t"`, or `1` links in a Tweet are not expanded to photo, video, or link previews. |
| `hide_thread`  <br>Boolean, String or Int | `false` | When set to `true`, `"t"`, or `1` a collapsed version of the previous Tweet in a conversation thread will not be displayed when the requested Tweet is in reply to another Tweet. |
| `omit_script`  <br>Boolean, String or Int | `false` | When set to `true`, `"t"`, or `1` the `<script>` responsible for loading `widgets.js` will not be returned. Your webpages should include their own reference to `widgets.js` for use across all Twitter widgets including [Embedded Tweets](https://developer.twitter.com/web/embedded-tweets). |
| `align`  <br>Enum `{left,right,center,none}` | `none` | Specifies whether the embedded Tweet should be floated left, right, or center in the page relative to the parent element. |
| `related`  <br>String |     | A comma-separated list of Twitter usernames related to your content. This value will be forwarded to [Tweet action intents](https://developer.twitter.com/web/intents) if a viewer chooses to reply, like, or retweet the embedded Tweet. |
| `lang`  <br>Enum([Language](https://developer.twitter.com/en/docs/twitter-for-websites/twitter-for-websites-supported-languages/overview)) | `en` | Request returned HTML and a rendered Tweet in the specified [Twitter language supported by embedded Tweets](https://developer.twitter.com/web/overview/languages). |
| `theme`  <br>Enum `{light, dark}` | `light` | When set to `dark`, the Tweet is displayed with light text over a dark background. |
| `link_color`  <br>String |     | Adjust the color of Tweet text links with a [hexadecimal color value](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet). |
| `widget_type`  <br>Enum `{video}` |     | Set to `video` to return a Twitter Video embed for the given Tweet. |
| `dnt`  <br>Boolean | `false` | When set to `true`, the Tweet and its embedded page on your site are not used for purposes that include [personalized suggestions](https://support.twitter.com/articles/20169421) and [personalized ads](https://support.twitter.com/articles/20170405). |