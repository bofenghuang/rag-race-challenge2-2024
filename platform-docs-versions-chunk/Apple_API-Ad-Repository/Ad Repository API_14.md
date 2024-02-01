platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

placement string

The placement of the ad on the App Store.

Values are APPSTORE_SEARCH_RESULTS,

APPSTORE_TODAY_TAB, APPSTORE_SEARCH_TAB



format string The format of the ad. Values are Icon Ad, Icon

+ Asset Ad.



countryOrRegion string

A country or region in the European Union in

which Apple-delivered advertising is available on

the App Store, expressed in ISO 3166-1 alpha-2

format. For example: ES, SE, DE.



audienceRefinement object Audience refinement criteria used in an ad

campaign.



ageTarget boolean Indicates if age parameters are used in an ad

campaign.



genderTarget boolean Indicates if gender parameters are used in an ad

campaign.



locationTarget boolean Indicates if country or region parameters are

used in an ad campaign.



customerTypeTarget boolean



Indicates app downloader type. Values are:

ALL_USERS

NEW_USERS

RETURNING_USERS

USERS_OF_MY_OTHER_APPS