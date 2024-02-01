platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Table Schema Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Table Schema Documentation.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/table-schema

### **Inconsistencies between the Ad Targeting dataset table and the Ad Library data table**

If you perform a join between the two tables, you will see that there are ads in the Ad Targeting dataset table that do not have a corresponding entry in the Ad Library data table (or vice versa). This happens because ads initially classified as political can be reclassified as non-political after they have been run.

When a reclassification occurs, the Ad Library data table reflects the change before the Ad Targeting dataset because the Ad Library data table is updated daily and the Ad Targeting dataset is updated monthly.

Beginning with the second monthly update, there is an [Ad Targeting dataset delta table](#delta-schema) that describes ads that were reclassified as non-political (and therefore, removed from the dataset) since the previous monthly update.