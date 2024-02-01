platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Overview.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/january-2021-dataset


## How to manage issues found in the datasets

There are two issues having to do with the inclusion or exclusion of custom and lookalike audiences that we found in the datasets.

**These issues only affected data related to custom and lookalike audiences.**

Your research was not impacted if it did not involve custom or lookalike audiences.

Here's what we have done to address these issues:

* We are providing this updated documentation explaining the issues and describing ways to interpret the data in light of them.
    
* We have corrected the issues in the May 2022 targeting dataset.
    
* We have included two new columns in the May 2022 targeting dataset called `include_audience_data_missing` and `exclude_audience_data_missing`. These columns are marked True where we know we are missing data. A value of True (data is missing) indicates that a custom or lookalike audience was used, but we’re unable to identify or report the specifics of that audience.
    

Here are the two issues and strategies for interpreting any data affected by them:

* Issue #1: [incorrect calculations](#incorrect-calculations)
    
* Issue #2: [deleted custom audiences](#deleted-CA)