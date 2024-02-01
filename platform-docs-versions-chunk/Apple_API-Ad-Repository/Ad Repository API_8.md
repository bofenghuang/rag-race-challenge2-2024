platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

startIndex: Specifies the position of the first element in the

results. The default is zero.



itemsPerPage: Specifies how many items is displayed per page.



Ad Repository API January 2024 6

Get a list of countries or regions

Use this endpoint to get a list of countries or regions in the European Union in which

Apple-delivered advertising is available on the App Store. Use the country codes

returned in the response in the Get a list of ads call.

Request example

GET https://adrepository.apple.com/api/v1/countries-or-regions



Response example