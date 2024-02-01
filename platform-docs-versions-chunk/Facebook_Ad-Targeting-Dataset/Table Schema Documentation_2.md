platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Table Schema Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Table Schema Documentation.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/table-schema


## Ad Targeting table schema

In this table, the Type (data type) can be:

* _String_: Sequence of characters, representing either a constant or a variable.
    
* _Boolean_: One of two possible values (usually denoted true and false).
    
* _BigInt_: Integer (numerical) value.
    
* _List_: Series of values. Angle brackets indicate the data type of the values in the list.
    
* _Map_: Series of key/value pairs. Angle brackets indicate the data type of the key and the data type of the value, separated by a comma.
    

| Column name | Type | Description | Sample value |
| --- | --- | --- | --- |
| `age` | string | Age group targeted by the ad. | `25` - `65+` |
| `archive_id` | BigInt | Ad dataset ID. | `2681789712070426` |
| `ds` | string | Table partition date stamp. | `2020-12-06` |
| `exclude` | map<string, string> | Ad excludes people who are categorized by ANY of the items listed, which can include behavior, field of study, education level, school, job title, and many more. | `{"Civil service":"Interests","Government Employees (Global)":"Industry","Servidor público no Brasil":"Job title"}` |
| `exclude_audience_data_missing`<br><br>  <br><br>This column is new in the May 2022 dataset. See [Columns for Indicating Missing Data](#missing-data) for more information. | Boolean | Indicates whether information is missing from the exclude\_custom\_audience, exclude\_data\_file\_custom\_audience, or exclude\_lookalike column. | `True` (data is missing)<br><br>  <br><br>`False` (data is not missing) |
| `exclude_connection` | Boolean | Ad excludes (`True`) or does not exclude (`False`) people who have liked a Page owned by the advertiser, responded to an event created by the advertiser, or used an app owned by the advertiser. | `True` |
| `exclude_custom_audience` | Boolean | Ad excludes (\`True\`) or does not exclude (\`False\`) a [custom audience](https://www.facebook.com/business/help/744354708981227) created by the advertiser. | `True` |
| `exclude_data_file_custom_audience` | Boolean | Ad excludes (\`True\`) or does not exclude (\`False\`) people in a [custom audience](https://www.facebook.com/business/help/744354708981227) created by the advertiser from a [customer list.](https://www.facebook.com/business/help/606443329504150) | `True` |
| `exclude_location` | map<string, map<string, mixed>> | Locations (cities, countries, zip codes) excluded by the ad, plus an optional radius in miles.<br><br>  <br><br>See [Location data](#location-data) for additional information. | `{"United States":{"Nevada":{}}}` |
| `exclude_lookalike` | Boolean | Ad excludes (\`True\`) or does not exclude (\`False\`) a [lookalike audience](https://www.facebook.com/business/help/164749007013531) created by the advertiser. | `True` |
| `gender` | string | Gender targeted by the ad. | `Female` |
| `include` | list<map<string, string>> | Ad targets people who are categorized by ANY of the items listed, with at least one item in each group. Items can include behavior, field of study, education level, school, job title, and many more. | The following example shows two groups, each enclosed in curly braces. Ad targets people with at least one item in each group.<br><br>\[<br>  {<br>    "College grad": "Education level"<br>  },<br>  {<br>    "Wine": "Interests",<br>    "Golf": "Interests",<br>    "Organic food": "Interests",<br>    "Skiing": "Interests",<br>    "Security (finance)": "Interests",<br>    "Frequent Travelers": "Behaviors",<br>    "Sustainable development": "Interests",<br>    "Business and industry": "Interests",<br>    "Natural environment": "Interests",<br>    "Sailing": "Interests",<br>    "Running": "Interests",<br>    "SVT Play": "Interests",<br>    "Politics": "Interests"<br>  }<br>\] |
| `include_audience_data_missing`<br><br>  <br><br>This column is new in the May 2022 dataset. See [Columns for indicating missing data](#missing-data) for more information. | Boolean | Indicates whether information is missing from the include\_custom\_audience, include\_data\_file\_custom\_audience, or include\_lookalike column. | `True` (data is missing)<br><br>  <br><br>`False` (data is not missing) |
| `include_connection` | Boolean | Ad targets (`True`) or does not target (`False`) people who have liked a Page owned by the advertiser, responded to an event created by the advertiser, or used an app owned by the advertiser. | `True` |
| `include_custom_audience` | Boolean | Ad targets (\`True\`) or does not target (\`False\`) a [custom audience](https://www.facebook.com/business/help/744354708981227?id=2469097953376494) created by the advertiser. | `True` |
| `include_data_file_custom_audience` | Boolean | Ad targets (\`True\`) or does not target (\`False\`) people in a [custom audience](https://www.facebook.com/business/help/744354708981227) created by the advertiser from a [customer list](https://www.facebook.com/business/help/606443329504150). | `True` |
| `include_friend_connections` | Boolean | Ad targets (`True`) or does not target (`False`) friends of people who have liked a Page owned by the advertiser or who have used an app owned by the advertiser. | `True` |
| `include_location` | map<string, map<string, mixed>> | Locations targeted by the ad. Radius in miles included if specified by the advertiser. Can be cities, countries, or zip codes, plus an optional radius in miles.<br><br>  <br><br>See [Location data](#location-data) for additional information. | `{"Brazil":{"Minas Gerais":{"Santa Maria do Suaçuí":["< place>, Santa Maria do Suaçuí (+1 km)"]},"Glucínio Minas Gerais, Poaia Minas Gerais":{}}}` |
| `include_lookalike` | Boolean | Ad targets (\`True\`) or does not target (\`False\`) a [lookalike audience](https://www.facebook.com/business/help/164749007013531) created by the advertiser. | `True` |
| `language`<br><br>  <br><br>This column is new in the May 2022 dataset. | string | Languages targeted by the ad. | `English (UK), Greek, English (US)` |
| `location_type` | string | Ad targets people by their relationship to a location. The location is the area selected by the advertiser upon ad creation and is identified by the `include_location` column.<br><br>  <br><br>Possible values:<br><br>  <br><br>* `Location`—The ad targets people whose home or most recent location is within the selected area<br>* `Location - Living In`—The ad targets people whose home is within the selected area<br>* `Location - Recently In`—The ad targets people whose most recent location is within the selected area<br>* `Location - Traveling In`—The ad targets people whose most recent location is within the selected area but whose home is more than 125mi/200km away<br><br>See [Location data](#location-data) for additional information. | `Location - Living In` |