platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/Post


### [](#post)Post

A post object represents a single post from any of the supported platforms (e.g., Facebook, Instagram). All posts also contain an [account object](https://github.com/CrowdTangle/API/wiki/Account). Below are the properties of a post. See examples in [/posts](https://github.com/CrowdTangle/API/wiki/Posts).

#### [](#properties)Properties

| Property | Type | Description |
| --- | --- | --- |
| account | [Account](https://github.com/CrowdTangle/API/wiki/Account) | See [account](https://github.com/CrowdTangle/API/wiki/Account). |
| brandedContentSponsor | [Account](https://github.com/CrowdTangle/API/wiki/Account) | See [account](https://github.com/CrowdTangle/API/wiki/Account). This field is only present for Facebook Page posts where there is a sponsoring Page. |
| caption | text | The caption to a photo, if available. |
| date | date ("yyyy‑mm‑dd hh:mm:ss") | The date and time the post was published. Time zone is UTC. |
| description | text | Further details, if available. Associated with links or images across different platforms. |
| expandedLinks | map of text | A map where the keys are the original links that came in the post (which are often shortened), and the values are the expanded links. |
| id  | string ("account.id\|postExternalId") | The unique identifier of the post in the CrowdTangle system. This ID is specific to CrowdTangle, not the platform from which the post originated. |
| imageText | string | The text, if it exists, within an image. |
| legacyid | int | The legacy version of the unique identifier of the post in the CrowdTangle system. This ID is specific to CrowdTangle, not the platform from which the post originated. |
| link | string | An external URL that the post links to, if available. (Facebook only) |
| media | array of [media](#media) | An array of available media for the post. |
| message | text | The user-submitted text on a post. |
| platform | enum (facebook, instagram, reddit) | The platform on which the post was posted. E.g., Facebook, Instagram, etc. |
| platformId | string | The platform's ID for the post. |
| postUrl | string | The URL to access the post on its platform. |
| score | double | The score of a post as measured by the request. E.g. it will represent the overperforming score if the request `sortBy` specifies `overperforming`, the interaction rate if the request specifies `interaction_rate`, etc. |
| statistics | [Statistics](#statistics) | Performance metrics associated with the post. |
| subscriberCount | int | The number of subscriber the account had _when the post was published_. This is in contrast to the subscriberCount found on the [account](https://github.com/CrowdTangle/API/wiki/Account), which represents the current number of subscribers an account has. |
| type | enum (album, igtv, link, live\_video, live\_video\_complete, live\_video\_scheduled, native\_video, photo, status, video, vine, youtube) | The type of the post. |
| updated | date ("yyyy‑mm‑dd hh:mm:ss") | The date and time the post was most recently updated in CrowdTangle, which is most often via getting new scores from the platform. Time zone is UTC. |
| videoLengthMS | int | The length of the video in milliseconds. |
| liveVideoStatus | string ("live", "completed", "upcoming") | The status of the live video. |