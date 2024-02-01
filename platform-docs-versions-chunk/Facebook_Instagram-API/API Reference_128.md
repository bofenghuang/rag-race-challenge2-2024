platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights


### Metrics and Periods

Some of these metrics are deprecated for v18.0. They will be deprecated for all versions beginning Dec 11, 2023. Please use the alternative metrics listed. See the [Changelog](https://developers.facebook.com/docs/instagram-api/changelog) for more information.

Metrics that support `lifetime` periods will have results returned in an array of 24 hour periods, with periods ending on UTC−07:00. `audience_*` metrics do not support `since` and `until` [range](#range) parameters.

| Metric | Compatible Period | Description |
| --- | --- | --- |
| `audience_city`  <br>_Deprecated for v18.0+_ | `lifetime` | Cities of followers for whom we have demographic data.<br><br>  <br><br>* Does not include current day's data.<br>* Not available on IG Users with fewer than 100 followers.<br>* Only top 45 cities with highest values returned.<br>* Does not support `since` and `until` parameters.<br>* Response does not include the `end_time` JSON property.<br><br>**Alternative metric:** `follower_demographics`  <br>**Breakdown:** `city` |
| `audience_country`  <br>_Deprecated for v18.0+_ | `lifetime` | Countries of followers for whom we have demographic data.<br><br>  <br><br>* Does not include current day's data.<br>* Not available on IG Users with fewer than 100 followers.<br>* Only top 45 countries with highest values returned.<br>* Does not support `since` and `until` parameters.<br>* Response does not include the `end_time` JSON property.<br><br>**Alternative metric:** `follower_demographics`  <br>**Breakdown:** `country` |
| `audience_gender_age`  <br>_Deprecated for v18.0+_ | `lifetime` | The gender and age distribution of followers for whom we have demographic data. Possible values: `M` (male), `F` (female), `U` (Uncategorised).<br><br>  <br><br>* Does not include current day's data.<br>* Not available on IG Users with fewer than 100 followers.<br>* Does not support `since` and `until` parameters.<br>* Response does not include the `end_time` JSON property.<br><br>**Alternative metric:** `follower_demographics`  <br>**Breakdown:** `age`, `gender` |
| `audience_locale`  <br>_Deprecated for v18.0+_ | `lifetime` | **Note:** This metric is no longer supported.<br><br>  <br><br>Locales by country codes of followers for whom we have demographic data.<br><br>  <br><br>* Does not include current day's data.<br>* Not available on IG Users with fewer than 100 followers.<br>* Only top 45 locales with highest values returned.<br>* Does not support `since` and `until` parameters.<br>* Response does not include the `end_time` JSON property.<br><br>**Alternative metric:** N/A |
| `email_contacts` | `day` | Total number of taps on the email link in the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile. |
| `follower_count` | `day` | Total number of new followers each day within the specified range. Returns a maximum of 30 days worth of data. Not available on IG Users with fewer than 100 followers. |
| `get_directions_clicks` | `day` | Total number of taps on the directions link in the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile. |
| `impressions` | `day`, `week`, `days_28` | Total number of times the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) have been viewed. Includes ad activity generated through the API, Facebook ads interfaces, and the Promote feature. Does not include profile views. |
| `online_followers` | `lifetime` | Total number of the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) followers who were online during the specified range. Not available on IG Users with fewer than 100 followers. |
| `phone_call_clicks` | `day` | Total number of taps on the call link in the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile. |
| `profile_views` | `day` | Total number of users who have viewed the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile within the specified period. |
| `reach` | `day`, `week`, `days_28` | Total number of unique users who have viewed at least one of the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media). Repeat views and views across different IG Media owned by the IG User by the same user are only counted as a single view. Includes ad activity generated through the API, Facebook ads interfaces, and the Promote feature. |
| `text_message_clicks` | `day` | Total number of taps on the text message link in the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile. |
| `website_clicks` | `day` | Total number of taps on the website link in the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile. |