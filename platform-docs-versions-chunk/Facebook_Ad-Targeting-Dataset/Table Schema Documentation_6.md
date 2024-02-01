platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Table Schema Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Table Schema Documentation.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/table-schema

## Tracking ad change history

An ad's `archive_id` in the Ad Targeting dataset maps to the ad's ID in the Ad Library product, where researchers can access the ad creative, the Page associated with the ad, who paid for the ad ("Paid for by" disclaimer), a range of how much they spent, and the reach of the ad across multiple demographics.

If an advertiser makes changes to an ad after it has been created, (such as editing the creative, targeting logic, or spend limits), then our system stores the updated version of the ad as a new distinct ID. This means that distinct `archive_id` values in the dataset could relate to a similar creative, such as if the only modification was to change the targeting of the ad.