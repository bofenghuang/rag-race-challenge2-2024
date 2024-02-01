platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

previewDevice string The device displaying the ad.



adAssets string The resolved URL for an ad assset.



videoUrl string The resolved URL for a video asset.



pictureUrl string The resolved URL for the screenshot or a

screenshot of the image asset.



order integer The order of the ad asset that was uploaded to

App Store Connect.



height integer The height of the ad asset that was uploaded to

App Store Connect.



width integer The width of the ad asset that was uploaded to

App Store Connect.



orientation string

The orientation of the ad asset that was

uploaded to App Store Connect. Values are

LANDSCAPE, PORTRAIT, UNKNOWN



Ad Repository API January 2024 19

Get advertising-restrictions

Use this endpoint to return details of advertising-restrictions applied during a date

range. Ads must have at least one advertising impression to be included in the

response.



GET https://adrepository.apple.com/api/v1/restrictions