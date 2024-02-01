platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

countryOrRegion string yes

A country or region in the European Union in

which Apple-delivered advertising is available on

the App Store, expressed in ISO 3166-1 alpha-2

format. For example: ES, SE, DE.



datePreset string no

The date range of the request. Values are

LAST_90_DAYS, LAST_180_DAYS, LAST_YEAR.

The default is LAST_90_DAYS.



limit integer no The maximum number of entries to return per

page. The default is 50.



offset integer no The offset pagination that limits the number of

returned records. The default is 0.



Ad Repository API January 2024 9

Response example

The AdRepositoryAd object is returned.