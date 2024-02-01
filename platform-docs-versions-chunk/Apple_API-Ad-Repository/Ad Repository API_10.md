platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

code string

The ISO 3166-1 alpha-2 two-letter country code of the country or

region in the European Union in which Apple-delivered advertising

is available on the App Store. For example: ES, SE, DE.



Ad Repository API January 2024 8

Get a list of ads



Use this endpoint to return ad metadata and an adId to use in the Get Ad Variations call.



GET https://adrepository.apple.com/api/v1/ad-repository-ads



Request example

• Use ql= URL encoded RSQL filter to allow special characters.

• You can have both id or countryOrRegion or either in a request. If id is used

then type must also be present.

GET ~/api/v1/ad-repository-ads

?ql=

type==APP;

id==1582276305;

countryOrRegion=in=(FR,DE);

datePreset==LAST_90_DAYS;

\&offset=0

\&limit=50



Request parameters



Parameter Type Required Description



type string yes Values are APP , DEVELOPER.



id string yes

A unique identifier. If the type is APP , the id is an

appId . If the type is DEVELOPER, the id is a

developerId.