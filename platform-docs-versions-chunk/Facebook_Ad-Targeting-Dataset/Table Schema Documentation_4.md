platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Table Schema Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Table Schema Documentation.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/table-schema


## Ad Targeting dataset columns for indicating missing data

As of November 1, 2021, we started tracking information about custom audiences that were deleted sometime after the ads were initially run. For data prior to that date, the Ad Targeting dataset might be missing information about whether custom audiences, datafile custom audiences, or lookalike audiences were used or not. By "missing information", we mean that one of the affected columns could read False when it should actually be True. If it already reads True, we know for sure that it is True.

We have added two columns to the table schema where we indicate whether data is missing. The following table lists the two new columns, indicates the columns of data to which they pertain, and provides the meaning of the possible values:

|     | include\_audience\_data\_missing column | exclude\_audience\_data\_missing column |
| --- | --- | --- |
| **Columns tracked** | `include_custom_audience`<br><br>  <br><br>`include_data_file_custom_audience`<br><br>  <br><br>`include_lookalike` | `exclude_custom_audience`<br><br>  <br><br>`exclude_data_file_custom_audience`<br><br>  <br><br>`exclude_lookalike` |
| **Value of True means...** | Information is missing. At least one of the columns above could read False when it should actually be True. | Information is missing. At least one of the columns above could read False when it should actually be True. |
| **Value of False means...** | No data is missing. | No data is missing. |