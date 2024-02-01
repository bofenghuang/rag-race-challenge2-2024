platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/audiences/create_custom)Create custom audience

Create a custom audience and find the audiences you want your ads to reach.

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Custom audience to create.

|     |     |
| --- | --- |
| ad\_account\_id | string (ad\_account\_id) ^\\d+$<br><br>Ad account ID. |
| name<br><br>required | string (name)<br><br>Audience name. |
| rule<br><br>required | object (Rule)<br><br>JSON object defining targeted audience users. Example rule formats per audience type:  <br>CUSTOMER\_LIST: { "customer\_list\_id": "<customer list ID>"}  <br>ACTALIKE: { "seed\_id": \["<audience ID>"\], "country": "US", "percentage": "10" }  <br>(Valid countries include: "US", "CA", and "GB". Percentage should be 1-10.  <br>The targeted audience should be this % size across Pinterest.)  <br>VISITOR: { "visitor\_source\_id": \["<conversion tag ID>"\], "retention\_days": "180", "event\_source": {"=": \["web", "mobile"\]}, "ingestion\_source": {"=": \["tag"\]}}  <br>(Retention days should be 1-540. Retention applies to specific customers.)  <br>ENGAGEMENT: {"engagement\_domain": \["[www.entomi.com"\]](http://www.entomi.com/%22%5D), "engager\_type": 1}  <br>For more details on engagement audiences, see [November 2021 changelog](https://developers.pinterest.com/docs/redoc/adtech_ads_v4/#section/November-2021). |
| sharing\_type<br><br>required | string (AudienceSharingType)<br><br>Enum: "CUSTOM" "SYNDICATED"<br><br>Audience sharing type: \["CUSTOM", "SYNDICATED"\] |
| data\_party<br><br>required | string (AudienceDataParty)<br><br>Enum: "1p" "3p"<br><br>Whether the data is owned by the partner (1p) or by the data provider (3p) |
| category | string |