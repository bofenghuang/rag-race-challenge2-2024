platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/audiences/update)Update audience

Update (edit or remove) an existing targeting audience.

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| audience\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an audience |

##### Request Body schema: application/json

The audience to be updated.

|     |     |
| --- | --- |
| ad\_account\_id | string (ad\_account\_id) ^\\d+$<br><br>Ad account ID. |
| name | string (name)<br><br>Audience name. |
| rule | object (Rule)<br><br>JSON object defining targeted audience users. Example rule formats per audience type:  <br>CUSTOMER\_LIST: { "customer\_list\_id": "<customer list ID>"}  <br>ACTALIKE: { "seed\_id": \["<audience ID>"\], "country": "US", "percentage": "10" }  <br>(Valid countries include: "US", "CA", and "GB". Percentage should be 1-10.  <br>The targeted audience should be this % size across Pinterest.)  <br>VISITOR: { "visitor\_source\_id": \["<conversion tag ID>"\], "retention\_days": "180", "event\_source": {"=": \["web", "mobile"\]}, "ingestion\_source": {"=": \["tag"\]}}  <br>(Retention days should be 1-540. Retention applies to specific customers.)  <br>ENGAGEMENT: {"engagement\_domain": \["[www.entomi.com"\]](http://www.entomi.com/%22%5D), "engager\_type": 1}  <br>For more details on engagement audiences, see [November 2021 changelog](https://developers.pinterest.com/docs/redoc/adtech_ads_v4/#section/November-2021). |
| description | string (description)<br><br>Audience description. |
| operation\_type | string (operation\_type)<br><br>Default: "UPDATE"<br><br>Enum: "UPDATE" "REMOVE"<br><br>Audience operation type (update or remove). |