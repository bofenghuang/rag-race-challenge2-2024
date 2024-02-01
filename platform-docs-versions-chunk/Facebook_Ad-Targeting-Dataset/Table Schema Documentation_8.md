platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Table Schema Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Table Schema Documentation.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/table-schema

## Joining Ad Targeting dataset data with Ad Library data

If you want more information about an ad (its creative, spend, and so on) and want to map the ad with its targeting information, perform a join between the `archive_id` column of the `ad_targeting_dataset_siep_aug_2020` table (the Ad Targeting dataset) and the `fbid` column of the `ad_archive_api` table (the Ad Library dataset) as shown in this example:

data\_joined = execute("SELECT \* FROM fbri\_prod\_atp.ad\_archive\_api AS a, fbri\_prod\_atp.ad\_targeting\_dataset\_siep\_aug\_2020 AS b WHERE a.ds = b.ds AND a.fbid = b.archive\_id")

**Column name change notice**

The name of the `fbid` column of the `ad_archive_api` table was `ad_archive_id` prior to April 21, 2021. If you want to join on data before that date, use the `ad_archive_id` column name.