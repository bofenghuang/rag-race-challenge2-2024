platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Table Schema Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Table Schema Documentation.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/table-schema


## Ad Library data table schema

The Ad Targeting dataset (refreshed monthly) contains data about targeting selections for each ad, specified by \`archive\_id\`. We also provide the [Ad Library data](https://facebook.com/ads/library) table that contains information about ad delivery, such as what pages ran the ad, when it was created, how many users it reached, and so on. This table is refreshed daily.

To get a complete picture of the advertisement and its content, including both its targeting and its delivery, you need information from both tables. See [Joining Ad Targeting dataset data with Ad Library data](#joining-ad-library).

| Column | Type | Description |
| --- | --- | --- |
| `fbid` | string | ID for the archived ad object. |
| `ad_archive_id` | string | Same as `fbid` but an older version of the column name (prior to April 21, 2021). |
| `ad_creation_time` | string | The UTC date and time when someone created the ad. This is not the same time as when the ad ran. Includes date and time separated by T. Example: 2019-01-24T19:02:04+0000, where +0000 is the UTC offset. |
| `ad_creative_body` | list< string> | A list of the text that displays in each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards, each with its own unique text. See [Ad Creative](https://developers.facebook.com/docs/marketing-api/reference/ad-creative/) for more information. |
| `ad_creative_link_caption` | list< string> | A list of the captions that appear in the call to action section for each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards, each with its own unique text that appears in the link. |
| `ad_creative_link_description` | list< string> | A list of text descriptions that appear in the call to action section for each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards, each with its own unique text describing the link. |
| `ad_creative_link_title` | list< string> | A list of titles that appear in the call to action section for each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards, each with its own unique title text about the link. |
| `ad_delivery_start_time` | string | Date and time when an advertiser wants Facebook to start delivering an ad. Provided in UTC as in `ad_creation_time`. |
| `ad_delivery_stop_time` | string | The time when an advertiser wants to stop delivery of their ad. If this is blank, Facebook runs the ad until the advertiser stops it or they spend their entire campaign budget. Provided in UTC. |
| `ad_snapshot_url` | string | String with URL link that displays the archived ad. This displays uncompressed images and videos from the ad. Note that you cannot currently download a batch of archived ads, however you can download ad creative such as images and text for an individual ad. If you do so, it must be for analysis and you must comply with the data storage terms in [Facebook Terms of Service.](https://www.facebook.com/terms.php) |
| `funding_entity` | string | A string containing the name of the person, company, or entity that provided funding for the ad. Provided by the purchaser of the ad. |
| `currency` | string | The currency used to pay for the ad, as an [ISO currency code.](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.iso.org%2Fiso-4217-currency-codes.html%3Ffbclid%3DIwAR2dth6_P9G_7MsN9Vd_0KjbF_RfruHJjqUacKNZO-_i61kwVCQ75PVIlyQ&h=AT0s5PQ3UR_0b8Pc9qcXhDpk53wZcCxTAA0F8i-ChWQUkCNW0-ttL1xcuZ3_SnY5zS0HMvZYFZhbIAXrWvMldJ6T-upNvxMEaPZQIx1hXgkyvoR5DiIHC-nIp57kRZC2_cHHvL1Z6SDQXXGk) |
| `region_distribution` | [list< AudienceDistribution>](https://developers.facebook.com/docs/graph-api/reference/audience-distribution/) | Regional distribution of people reached by the ad. Provided as a percentage and where regions are at a sub-country level. |
| `demographic_distribution` | [list< AudienceDistribution>](https://developers.facebook.com/docs/graph-api/reference/audience-distribution/) | The demographic distribution of people reached by the ad. Provided as age ranges and gender.<br><br>* Age ranges: 18-24, 25-34, 35-44, 45-54, 55-64, 65+<br>    <br>* Gender: "Male", "Female", "Unknown" |
| `potential_reach` | [InsightsRangeValue](https://developers.facebook.com/docs/graph-api/reference/insights-range-value/) | Estimated Audience Size generally estimates how many people meet the targeting and ad placement criteria that advertisers select while creating an ad. [Learn more.](https://www.facebook.com/business/help/1665333080167380?id=176276233019487) |
| `impressions` | [InsightsRangeValue](https://developers.facebook.com/docs/graph-api/reference/insights-range-value/) | A string containing the number of times the ad created an impression. In ranges of:< 1000, 1K-5K, 5K-10K, 10K-50K, 50K-100K, 100K-200K, 200K-500K, >1M. |
| `languages` | list< string> | The list of languages contained within the ad. These are displayed in [ISO 639-1 language codes.](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.iso.org%2Fstandard%2F22109.html%3Ffbclid%3DIwAR3m8L9GO0eQRNpQ6JErJDiLs6n4U5nWZHp7ObPKwdO60O77MwULJ79rfCQ&h=AT2BE0vHPIhRk4NB0z4QkqbJHihI6-gLhLUqwU6LjhiOy1CA3bX8NDRVhfGvmd_A7z8D1sC2RviRBdKLRFhogINB5nAOtp-cCTIKIaybsvb8FxYq2PL7H-fivb6CqUuvlxXrAsGuKF0PsL1-) |
| `page_id` | numeric string | ID of the Facebook Page that ran the ad. |
| `page_name` | string | Name of the Facebook Page that ran the ad. |
| `publisher_platforms` | list< enum> | A list of platforms where the archived ad appeared, such as Facebook or Instagram. |
| `spend` | [InsightsRangeValue](https://developers.facebook.com/docs/graph-api/reference/insights-range-value/) | A string showing amount of money spent running the ad as specified in currency. This is reported in ranges; <100, 100-499, 500-999, 1K-5K, 5K-10K, 10K- 50K, 50K-100K, 100K-200K, 200K-500K, >1M. |
| `is_active` | boolean | Whether the ad is currently actively running on any platform. |
| `reached_countries` | list< string> | List of countries (as ISO country codes) that ran the ad. |
| `media_type` | list< string> | A list of media types contained within the ad. |
| `ds` | string | Table partition date stamp. |