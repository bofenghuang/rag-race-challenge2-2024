platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

audienceRefinement object

array

Audience refinement criteria used in an ad campaign.



ageTarget boolean Indicates if age parameters are used in the ad

campaign.



genderTarget boolean Indicates if gender parameters are used in the ad

campaign.



locationTarget boolean Indicates if country or region parameters are used in

the ad campaign.



customerTypeTarget boolean



Indicates app downloader type. Values are:

ALL_USERS

NEW_USERS

RETURNING_USERS

USERS_OF_MY_OTHER_APPS



dataStartDate string



Returned data is delayed by 7 days. For example, if

your datePreset is the LAST_90_DAYS, the system will

fetch matching ads by factoring today (UTC) as the

dataEndDate minus 7 days. The dataStartDate is

reported as the dataEndDate minus 90 days.



Ad Repository API January 2024 22

dataEndDate string