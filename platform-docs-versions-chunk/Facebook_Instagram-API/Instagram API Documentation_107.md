platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/changelog


## September 12, 2023

#### Deprecation of Media and User Insights

_Applies to v18.0+. Will apply to all versions on December 11, 2023._

Duplicative and legacy Instagram insight metrics are being deprecated. Please see documentation for the endpoints and [Instagram Insights](https://developers.facebook.com/docs/instagram-api/guides/insights) for more information on which metrics to use in their place.

The following endpoints and metrics are affected:

* [`GET /{ig-user-id}/insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights)
    * `AUDIENCE_GENDER_AGE`
    * `AUDIENCE_LOCALE`
    * `AUDIENCE_COUNTRY`
    * `AUDIENCE_CITY`
* [`GET /{ig-media-id}/insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights)
    * `CAROUSEL_ALBUM_IMPRESSIONS`
    * `CAROUSEL_ALBUM_REACH`
    * `CAROUSEL_ALBUM_ENGAGEMENT`
    * `CAROUSEL_ALBUM_SAVED`
    * `CAROUSEL_ALBUM_VIDEO_VIEWS`
    * `TAPS_FORWARD`
    * `TAPS_BACK`
    * `EXITS`
    * `ENGAGEMENT`

**Note:** `total_interactions`, which is listed as an alternative for some of the deprecated metrics, is currently only available using version 18.0 and does not work with older versions. When querying older versions before Dec 11, 2023, please use the `engagement` metric.`total_interactions`, which is listed as an alternative for some of the deprecated metrics, is currently only available using version 18.0 and does not work with older versions. When querying older versions before Dec 11, 2023, please use the `engagement` metric.

[](#)

[](#)