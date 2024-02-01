platform: Bing
topic: Ad-Library-API
subtopic: Ad Library API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Bing_Ad-Library-API/Ad Library API.md
url: https://learn.microsoft.com/en-us/advertising/guides/ad-library-api?view=bingads-13


### Templates

To create the endpoints used to query the Ad Library, append the appropriate template to the base URL:

| Template | HTTP Verb | Description | Resource |
| --- | --- | --- | --- |
| Advertisers | Get | Get Advertisers by Name  <br>  <br>Parameters:  <br>\- top (int32, default 3)  <br>\- skip (int32, default 0)  <br>\- searchText (string, default “”) | Array<Advertiser> |
| Advertisers({AdvertiserId})  <br>or  <br>Advertisers/{AdvertiserId} | Get | Get Advertiser by Id  <br>  <br>Parameters: none  <br>  <br>_Note_: AdvertiserId may be an AccountId or VerifiedAdvertiserId. Multiple accounts may be verified under the same identity. If a verified AccountId is requested the parent VerifiedAdvertiserId will be returned instead. | Advertiser |
| Ads | Get | Get Ads by Advertiser/Content  <br>  <br>Parameters:  <br>• top (int32, default 12)  <br>• skip (int64, default 0)  <br>• startDate (string)  <br>• endDate (string)  <br>• Dates in format ‘yyyy-MM-dd’  <br>• countryCodes (string)  <br>  <br>Comma separated values, i.e. ’10,26,53’  <br>• advertiserId (int64)  <br>• searchText (string) | Array<Ad> |
| Ads({AdId})  <br>or  <br>Ads/{AdId} | Get | Get Ad by Id  <br>  <br>Parameters: none | Ad  |