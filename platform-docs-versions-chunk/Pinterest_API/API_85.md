platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/audiences/create)Create audience

Create an audience you can use in targeting for specific ad groups. Targeting combines customer information with the ways users interact with Pinterest to help you reach specific groups of users; you can include or exclude specific audience\_ids when you create an ad group.

For more, see [Audience targeting](https://help.pinterest.com/en/business/article/audience-targeting).

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

List of ads to create, size limit \[1, 30\]

|     |     |
| --- | --- |
| ad\_account\_id | string (ad\_account\_id) ^\\d+$<br><br>Ad account ID. |
| name<br><br>required | string (name)<br><br>Audience name. |
| rule<br><br>required | object (Rule)<br><br>JSON object defining targeted audience users. Example rule formats per audience type:  <br>CUSTOMER\_LIST: { "customer\_list\_id": "<customer list ID>"}  <br>ACTALIKE: { "seed\_id": \["<audience ID>"\], "country": "US", "percentage": "10" }  <br>(Valid countries include: "US", "CA", and "GB". Percentage should be 1-10.  <br>The targeted audience should be this % size across Pinterest.)  <br>VISITOR: { "visitor\_source\_id": \["<conversion tag ID>"\], "retention\_days": "180", "event\_source": {"=": \["web", "mobile"\]}, "ingestion\_source": {"=": \["tag"\]}}  <br>(Retention days should be 1-540. Retention applies to specific customers.)  <br>ENGAGEMENT: {"engagement\_domain": \["[www.entomi.com"\]](http://www.entomi.com/%22%5D), "engager\_type": 1}  <br>For more details on engagement audiences, see [November 2021 changelog](https://developers.pinterest.com/docs/redoc/adtech_ads_v4/#section/November-2021). |
| description | string (description)<br><br>Audience description. |
| audience\_type<br><br>required | string<br><br>Enum: "CUSTOMER\_LIST" "VISITOR" "ENGAGEMENT" "ACTALIKE" "PERSONA"<br><br>Audience type |