platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

Response properties..................................................................................................................................22



Changelog......................................................................................................................................................24



Ad Repository API January 2024 2



Contents

Getting Started

Use the Ad Repository API to look up Apple-delivered advertising on the App Store in

select European countries and regions as well as information about qualifying

advertising restrictions. You can manage API calls programmatically using API tools and

programs of your choice.

Versioning

The current version of the API is v1.

Usability

• Communication with the web service must use HTTPS.

• RSQL query patterns are supported in some endpoints.

• The API doesn’t accept headers with \*/\*. Disallow Accept \*/\* in your cURL

commands.

• API responses will have a header Content-Type: application/json.