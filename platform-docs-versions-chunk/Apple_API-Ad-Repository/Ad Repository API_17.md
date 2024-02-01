platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

Ad Repository API January 2024 12

orientation string

The orientation of the ad asset that was

uploaded to App Store Connect. Values are

LANDSCAPE, PORTRAIT, UNKNOWN.



appIconVariations object The URL of the app icon on the App Store.



adLocaleVariations object The language metadata of ad variations on the

App Store.



dataStartDate string



Returned data is delayed by 7 days. For example,

If your datePreset is the LAST_90_DAYS, the

system will fetch matching ads by factoring

today (UTC) as the dataEndDate minus 7 days.

The dataStartDate is reported as the

dataEndDate minus 90 days.



dataEndDate string



Returned data is delayed by 7 days. For example,

If your datePreset is the LAST_90_DAYS, the

system will fetch matching ads by factoring

today (UTC) as the dataEndDate minus 7 days.

The dataStartDate is reported as the

dataEndDate minus 90 days.



pagination integer



Returned pagination results.



totalResults: The total number of entries that

return for the operation.