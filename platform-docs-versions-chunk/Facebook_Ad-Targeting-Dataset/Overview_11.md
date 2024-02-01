platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Overview.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/january-2021-dataset


### **Issue #1 incorrect calculations**

Due to an error in the source code for the February 2021 dataset, when calculating the `include_custom_audience` and `exclude_custom_audience` data fields, we calculated the inclusion and exclusion of custom audiences where custom audiences may not actually have been used. For less than 12% of ads within the targeting dataset, this resulted in custom audience inclusion or exclusion incorrectly reading as True.

This has been corrected in the new dataset released in 2022, so if you are only using the new dataset, this problem will not affect your research.

If you are using the 2021 dataset, comparing ads from the 2021 and 2022 datasets can help you to interpret the data. Here's how:

1. For the three months of overlap, compare the two datasets, looking specifically at these custom audience columns:
    
    * `include_custom_audience`
    * `exclude_custom_audience`
2. If there is a difference between the two datasets in the `include_custom_audience` column, and `include_audience_data_missing` (in the new dataset) is True, the discrepancy could be the result of either incorrect calculation (Issue #1) or custom audience deletion (Issue #2), and there is no way to know which. If `include_audience_data_missing` is False (no missing data), the discrepancy is the result of incorrect calculation (Issue #1).
    
3. If there is a difference between the two datasets in the `exclude_custom_audience` column, and `exclude_audience_data_missing` (in the new dataset) is True, the discrepancy could be the result of either incorrect calculation (Issue #1) or custom audience deletion (Issue #2), and there is no way to know which. If `exclude_audience_data_missing` is False (no missing data), the discrepancy is the result of incorrect calculation (Issue #1).
    

This example shows how you can use `join` to compare the old and new datasets:

old\_targeting\_dataset = execute("SELECT \* FROM fbri\_prod\_atp.ad\_library\_targeting")
new\_targeting\_dataset = execute("SELECT \* FROM fbri\_prod\_atp.ad\_targeting\_dataset\_siep\_aug\_2020")
data = old\_targeting\_dataset.join(new\_targeting\_dataset.set\_index('archive\_id'), 'archive\_id', rsuffix='\_new')

data\[(data\['include\_custom\_audience'\] != data\['include\_custom\_audience\_new'\])\] # Checking the new data against the old data

data\[(data\['include\_custom\_audience'\] != data\['include\_custom\_audience\_new'\]) and (data\['include\_audience\_data\_missing'\] == False)\] # Checking the new data against the old data where there are no instances of missing data