platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

Returned data is delayed by 7 days. For example, If

your datePreset is the LAST_90_DAYS, the system will

fetch matching ads by factoring today (UTC) as the

dataEndDate minus 7 days. The dataStartDate is

reported as the dataEndDate minus 90 days.



pagination integer



Returned pagination results.



totalResults: The total number of entries that return

for the operation.



startIndex: Specifies the position of the first element

in the results. The default is zero.



itemsPerPage: Specifies how many items is displayed

per page.



Ad Repository API January 2024 23

Changelog



Date Notes



January, 2024 Added joecolor to AdRepositoryAd object response.



November, 2023 Added short description field. See Get a list of ads Response properties

and Get ad variations Response properties.



August, 2023 Initial version.



Ad Repository API January 2024 24

Apple Inc.

Copyright © 2024 Apple Inc.

All rights reserved.