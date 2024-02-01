platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

startIndex: Specifies the position of the first

element in the results. The default is zero.



itemsPerPage: Specifies how many items is

displayed per page.



Ad Repository API January 2024 13

Get ad variations

Use this endpoint to return ad variations by date range. Use the adId returned in

the Get a list of ads call as a resource identifier in the URI.



GET https://adrepository.apple.com/api/v1/ad-repository-ads/{adId}?

datePreset=LAST_90_DAYS



Request parameters



Parameter Type Required Description



adId string yes A unique resource ad identifier.



datePreset string no

The date range of the request. Values are

LAST_90_DAYS, LAST_180_DAYS, LAST_YEAR.

The default is LAST_90_DAYS.



Ad Repository API January 2024 14

Response example

The AdRepositoryAd object is returned.