platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Overview.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/january-2021-dataset


### Issue #2 deleted custom audiences

For ads created before November 1, 2021, data might be missing from some ads where advertisers initially used a custom or lookalike audience, but later deleted that audience. Because the data is missing, data fields for custom or lookalike audience use may read as False when they should have shown as True.

This impacted less than 15% of ads within the targeting dataset released in February 2021 and impacted less than 6% of all social issue, electoral or political ads created before November 1, 2021.

In the new dataset (May 2022), if an advertiser deleted a custom or lookalike audience associated with an ad before November 1, 2021, it is indicated by a value of True in the new `include_audience_data_missing` or `exclude_audience_data_missing` columns. If you are only looking at data in the new dataset, you can choose how to treat the data in your analysis based on those columns.

You can also use those new columns to help you interpret affected data in the February 2021 dataset. Here's how:

1. As in Issue #1, compare the two datasets, but this time, looking specifically at these columns:
    
    * `include_custom_audience`
    * `exclude_custom_audience`
    * `include_data_file_custom_audience`
    * `exclude_data_file_custom_audience`
    * `include_lookalike`
    * `exclude_lookalike`
2. If a field is True in the new dataset, then even if data is marked as missing, it doesn’t affect these columns (or there were other, non-deleted audiences that allowed us to calculate this information).
    
3. If there is a difference between the two datasets, and `include_audience_data_missing` or `exclude_audience_data_missing` is True for the respective columns, the difference could be due to an audience getting deleted in the original dataset.
    
    * For the `include_data_file_custom_audience`, `exclude_data_file_custom_audience`, `include_lookalike`, and `exclude_lookalike` columns, audience deletion is definitely the reason for the discrepancy.
    * For the `include_custom_audience` and `exclude_custom_audience` columns, the discrepancy might also be due to incorrect calculation (Issue #1).
4. If all custom audience columns are the same between datasets but either of the data missing columns have a True value, there was missing data in the original dataset.
    
5. You can filter your data on `include_audience_data_missing` and `exclude_audience_data_missing`.
    
6. In the `include_data_file_custom_audience`, `exclude_data_file_custom_audience`, `include_lookalike`, and `exclude_lookalike` columns, you can safely copy True values from the old dataset to the new dataset when there is data missing in the new dataset—those audiences were deleted between the release of the February 2021 dataset and the release of the May 2022 dataset. This is something you might do if you are transferring your research from the old dataset to the new, for example.
    

This example shows how you can use `join` to compare the old and new datasets:

old\_targeting\_dataset = execute("SELECT \* FROM fbri\_prod\_atp.ad\_library\_targeting")