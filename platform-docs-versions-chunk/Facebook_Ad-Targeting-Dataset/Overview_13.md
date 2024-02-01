platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Overview.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/january-2021-dataset

# use the subset of old ads on which you were doing research
new\_targeting\_dataset = execute("SELECT \* FROM fbri\_prod\_atp.ad\_targeting\_dataset\_siep\_aug\_2020")
data = old\_targeting\_dataset.join(new\_targeting\_dataset.set\_index('archive\_id'), 'archive\_id', rsuffix='\_new')
data\[(data\['include\_audience\_data\_missing'\] == True) | (data\['exclude\_audience\_data\_missing'\] == True)\] # Get rows where there is missing data
data\[((data\['include\_custom\_audience'\] != data\['include\_custom\_audience\_new'\]) | (data\['include\_data\_file\_custom\_audience\_new'\] != data\['include\_data\_file\_custom\_audience'\]) | (data\['include\_lookalike'\] != data\['include\_lookalike\_new'\])) & (data\['include\_audience\_data\_missing'\] == True)\] # Find places where differences in include columns could be due to missing data