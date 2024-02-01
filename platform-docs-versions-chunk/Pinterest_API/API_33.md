platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/ad_groups/create)Create ad groups

Create multiple new ad groups. All ads in a given ad group will have the same budget, bid, run dates, targeting, and placement (search, browse, other). For more information, [click here](https://help.pinterest.com/en/business/article/campaign-structure).

**Note:**

* 'bid\_in\_micro\_currency' and 'budget\_in\_micro\_currency' should be expressed in microcurrency amounts based on the currency field set in the advertiser's profile.
    
    Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.
    
    A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’s profile.
    
    **Equivalency equations**, using dollars as an example currency:
    
    * $1 = 1,000,000 microdollars
    * 1 microdollar = $0.000001
    
    **To convert between currency and microcurrency**, using dollars as an example currency:
    
    * To convert dollars to microdollars, mutiply dollars by 1,000,000
    * To convert microdollars to dollars, divide microdollars by 1,000,000
* Ad groups belong to ad campaigns. Some types of campaigns (e.g. budget optimization) have limits on the number of ad groups they can hold. If you exceed those limits, you will get an error message.
* Start and end time cannot be set for ad groups that belong to CBO campaigns. Currently, campaigns with the following objective types: TRAFFIC, AWARENESS, WEB\_CONVERSIONS, and CATALOG\_SALES will default to CBO.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

List of ad groups to create, size limit \[1, 30\].

Array ()

|     |     |
| --- | --- |
| name<br><br>required | string<br><br>Ad group name. |
| status | string<br><br>Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>Ad group/entity status. |
| budget\_in\_micro\_currency | integer Nullable<br><br>Budget in micro currency. This field is **REQUIRED** for non-CBO (campaign budget optimization) campaigns. A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. A CBO campaign is limited to 70 or less ad groups. |
| bid\_in\_micro\_currency | integer Nullable<br><br>Bid price in micro currency. This field is **REQUIRED** for the following campaign objective\_type/billable\_event combinations: AWARENESS/IMPRESSION, CONSIDERATION/CLICKTHROUGH, CATALOG\_SALES/CLICKTHROUGH, VIDEO\_VIEW/VIDEO\_V\_50\_MRC. |
| optimization\_goal\_metadata | object Nullable<br><br>Optimization goals for objective-based performance campaigns. **REQUIRED** when campaign's `objective_type` is set to `"WEB_CONVERSION"`. |
| budget\_type | string<br><br>Default: "DAILY"<br><br>Enum: "DAILY" "LIFETIME" "CBO\_ADGROUP"<br><br>Budget type. If DAILY, an ad group's daily spend will not exceed the budget parameter value. If LIFETIME, the end\_time parameter is **REQUIRED**, and the ad group spend is spread evenly between the ad group `start_time` and `end_time` range. A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. For CBO campaigns, only "CBO\_ADGROUP" is allowed. For WEB\_SESSIONS campaigns, only "LIFETIME" is allowed. |
| start\_time | integer Nullable<br><br>Ad group start time. Unix timestamp in seconds. Defaults to current time. |
| end\_time | integer Nullable<br><br>Ad group end time. Unix timestamp in seconds. |
| targeting\_spec | object (TargetingSpec)<br><br>Ad group targeting specification defining the ad group target audience. For example, {"APPTYPE":\["iphone"\], "GENDER":\["male"\], "LOCALE":\["en-US"\], "LOCATION":\["501"\], "AGE\_BUCKET":\["25-34"\]} |
| lifetime\_frequency\_cap | integer<br><br>Set a limit to the number of times a promoted pin from this campaign can be impressed by a pinner within the past rolling 30 days. Only available for CPM (cost per mille (1000 impressions)) ad groups. A CPM ad group has an IMPRESSION [billable\_event](https://developers.pinterest.com/docs/redoc/#section/Billable-event) value. This field **REQUIRES** the `end_time` field. |
| tracking\_urls | object Nullable<br><br>Third-party tracking URLs.  <br>JSON object with the format: {"[Tracking event enum](https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event)":\[URL string array\],...}  <br>For example: {"impression": \["URL1", "URL2"\], "click": \["URL1", "URL2", "URL3"\]}.  <br>Up to three tracking URLs are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. May be null. Pass in an empty object - {} - to remove tracking URLs.  <br>  <br>For more information, see [Third-party and dynamic tracking](https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking). |
| auto\_targeting\_enabled | boolean Nullable<br><br>Enable auto-targeting for ad group. Also known as ["expanded targeting"](https://help.pinterest.com/en/business/article/expanded-targeting). |
| placement\_group | string<br><br>Enum: "ALL" "SEARCH" "BROWSE" "OTHER"<br><br>[Placement group](https://developers.pinterest.com/docs/redoc/#section/Placement-group). |
| pacing\_delivery\_type | string<br><br>Default: "STANDARD"<br><br>Enum: "STANDARD" "ACCELERATED"<br><br>Ad group pacing delivery type. With ACCELERATED, an ad group budget is spent as fast as possible. With STANDARD, an ad group budget is spent smoothly over a day. When using CBO, only the STANDARD pacing delivery type is allowed. |
| campaign\_id<br><br>required | string^\[C\]?\\d+$<br><br>Campaign ID of the ad group. |
| billable\_event<br><br>required | string (ActionType)<br><br>Enum: "CLICKTHROUGH" "IMPRESSION" "VIDEO\_V\_50\_MRC"<br><br>Ad group billable event type. |
| bid\_strategy\_type | string (BidStrategyType) Nullable<br><br>Enum: "AUTOMATIC\_BID" "MAX\_BID" "TARGET\_AVG" null<br><br>Bid strategy type |