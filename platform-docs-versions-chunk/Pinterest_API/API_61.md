platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/ads/create)Create ads

Create multiple new ads. Request must contain ad\_group\_id, creative\_type, and the source Pin pin\_id.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

List of ads to create, size limit \[1, 30\].

Array ()

|     |     |
| --- | --- |
| ad\_group\_id<br><br>required | string^(AG)?\\d+$<br><br>ID of the ad group that contains the ad. |
| android\_deep\_link | string Nullable<br><br>Deep link URL for Android devices. Not currently available. Using this field will generate an error. |
| carousel\_android\_deep\_links | Array of strings Nullable<br><br>Comma-separated deep links for the carousel pin on Android. |
| carousel\_destination\_urls | Array of strings Nullable<br><br>Comma-separated destination URLs for the carousel pin to promote. |
| carousel\_ios\_deep\_links | Array of strings Nullable<br><br>Comma-separated deep links for the carousel pin on iOS. |
| click\_tracking\_url | string Nullable<br><br>Tracking url for the ad clicks. |
| creative\_type<br><br>required | string (CreativeType)<br><br>Enum: "REGULAR" "VIDEO" "SHOPPING" "CAROUSEL" "MAX\_VIDEO" "SHOP\_THE\_PIN" "COLLECTION" "IDEA" "SHOWCASE" "QUIZ"<br><br>Ad creative type enum.<br><br>**Note:** SHOP\_THE\_PIN has been deprecated. Please use COLLECTION instead. |
| destination\_url | string Nullable<br><br>Destination URL. |
| ios\_deep\_link | string Nullable<br><br>Deep link URL for iOS devices. Not currently available. Using this field will generate an error. |
| is\_pin\_deleted | boolean<br><br>Is original pin deleted? |
| is\_removable | boolean<br><br>Is pin repinnable? |
| name | string Nullable<br><br>Name of the ad - 255 chars max. |
| status | string (EntityStatus)<br><br>Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>Entity status |
| tracking\_urls | object Nullable<br><br>Third-party tracking URLs. Up to three tracking URLs - with a max length of 2,000 - are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. For more information, see [Third-party and dynamic tracking](https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking). |
| view\_tracking\_url | string Nullable<br><br>Tracking URL for ad impressions. |
| lead\_form\_id | string Nullable ^(AG)?\\d+$<br><br>Lead form ID for lead ad generation. |
| grid\_click\_type | string (GridClickType) Nullable<br><br>Enum: "CLOSEUP" "DIRECT\_TO\_DESTINATION"<br><br>Where a user is taken after clicking on an ad in grid. |
| customizable\_cta\_type | string Nullable<br><br>Enum: "GET\_OFFER" "LEARN\_MORE" "ORDER\_NOW" "SHOP\_NOW" "SIGN\_UP" "SUBSCRIBE" "BUY\_NOW" "CONTACT\_US" "GET\_QUOTE" "VISIT\_WEBSITE" "APPLY\_NOW" "BOOK\_NOW" "REQUEST\_DEMO" "REGISTER\_NOW" "FIND\_A\_DEALER" "ADD\_TO\_CART" "WATCH\_NOW" "READ\_MORE" null<br><br>Select a call to action (CTA) to display below your ad. Available only for ads with direct links enabled. CTA options for consideration and conversion campaigns are LEARN\_MORE, SHOP\_NOW, BOOK\_NOW, SIGN\_UP, VISIT\_WEBSITE, BUY\_NOW, GET\_OFFER, ORDER\_NOW, ADD\_TO\_CART (for conversion campaigns with add to cart conversion events only) |
| quiz\_pin\_data | object Nullable<br><br>Before creating a quiz ad, you must create an organic Pin using POST/Create Pin for each result in the quiz. Quiz ads cannot be saved by a Pinner. Quiz ad results can be saved. |
| pin\_id<br><br>required | string^\\d+$<br><br>Pin ID. |