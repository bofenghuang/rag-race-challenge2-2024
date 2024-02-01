platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Overview.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/january-2021-dataset

## Transferring your research to the new dataset

Here we present two examples of transferring your research from the original dataset to the new dataset.

To transfer to the new dataset for the exact set of ads visible in the February 2021 dataset:

data = execute("SELECT \* FROM fbri\_prod\_atp.ad\_targeting\_dataset\_siep\_aug\_2020 WHERE archive\_id IN (SELECT archive\_id FROM fbri\_prod\_atp.ad\_library\_targeting)")

To do analysis on all ads in the new dataset from approximately the same timeframe as the original February 2021 dataset (to capture the ads with less than 100 impressions):

data = execute("SELECT b.\* FROM fbri\_prod\_atp.ad\_archive\_api AS a, fbri\_prod\_atp.ad\_targeting\_dataset\_siep\_aug\_2020 AS b WHERE a.ds = b.ds AND a.fbid = b.archive\_id AND (ad\_delivery\_start\_time BETWEEN 1596427200 AND 1604476800 OR ad\_delivery\_stop\_time BETWEEN 1596427200 AND 1604476800) AND reached\_countries LIKE '%US%'")