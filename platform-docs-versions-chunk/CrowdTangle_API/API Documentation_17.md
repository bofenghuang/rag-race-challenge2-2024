platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/Account


### [](#account)Account

An Account Object represents a page, account or user on a given platform. See examples in [/posts](https://github.com/CrowdTangle/API/wiki/Posts).

#### [](#properties)Properties

| Property | Type | Descriptions |
| --- | --- | --- |
| accountType | string | For Facebook only. Options are facebook\_page, facebook\_profile, facebook\_group. |
| handle | string | The handle or vanity URL of the account. |
| id  | int | The unique identifier of the account in the CrowdTangle system. This ID is specific to CrowdTangle, not the platform on which the account exists. |
| name | string | The name of the account. |
| pageAdminTopCountry | string | The [ISO country code](https://en.m.wikipedia.org/wiki/List_of_ISO_3166_country_codes#Current_ISO_3166_country_codes) of the the country from where the plurality of page administrators operate. |
| pageCategory | string | The page category as submitted by the page. View all page categories [here](https://www.facebook.com/pages/category/). |
| pageCreatedDate | int | The date on which the page was created. |
| pageDescription | string | The description of the page as documented in Page Transparency information. |
| platform | enum (facebook, instagram, reddit) | The platform on which the account exists. |
| platformId | string | The platform's ID for the account. This is not shown for Facebook public users. |
| profileImage | string | A URL pointing at the profile image. |
| subscriberCount | int | The number of subscribers/likes/followers the account has. By default, the subscriberCount property will show page Followers (as of January 26, 2021). You can select either Page Likes or Followers in your Dashboard settings. [Learn more here.](https://help.crowdtangle.com/en/articles/4797890-faq-measuring-followers) |
| url | string | A link to the account on its platform. |
| verified | boolean | Whether or not the account is verified by the platform, if supported by the platform. If not supported, will return false. |