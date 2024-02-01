platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Overview.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/january-2021-dataset


## Understanding the differences between the two datasets

Since you might be using one or both datasets in your research, and since you might want to transfer your research from the old dataset to the new one, it is important to understand the differences:

| Feature | February 2021 dataset | May 2022 dataset |
| --- | --- | --- |
| Table name | `ad_targeting_dataset` | `ad_targeting_dataset_siep_aug_2020`<br><br>  <br><br>There are three additional columns in this table: `exclude_audience_data_missing`, `include_audience_data_missing`, and `language`.<br><br>  <br><br>See [Table schema](https://developers.facebook.com/docs/fort-ads-targeting-dataset/table-schema) for details. |
| Coverage area | USA data only. | All countries in which we currently have our ad authorizations and disclaimer tools available.<br><br>  <br><br>More information about the countries this includes is available [here.](https://www.facebook.com/business/help/2150157295276323?id=288762101909005) |
| Minimum number of impressions for the ad to be included | 100 | 1   |
| Ongoing data collected and published | No  | Yes<br><br>  <br><br>On the 1st of each month beginning June 2022, an update to the table is published so that it includes all data through the 21st of the previous month. A delta table is also published, listing ads that were reclassified as non-political (and therefore removed) since the previous publication. |
| Indicates where custom audience data is known to be missing.<br><br>  <br><br>See [How to manage issues found in the datasets](#manage-issues) for more information. | No  | Yes<br><br>  <br><br>`include_audience_data_missing` and `exclude_audience_data_missing` columns are new in this dataset. |
| Preserves custom audience information for audiences that were removed.<br><br>  <br><br>See [How to manage issues found in the datasets](#manage-issues) for more information. | No  | Yes, after November 1, 2021. |