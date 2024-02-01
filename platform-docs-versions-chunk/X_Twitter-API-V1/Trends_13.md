platform: X
topic: Twitter-API-V1
subtopic: Trends
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Trends.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/trends/locations-with-trending-topics/api-reference/get-trends-closest

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| lat | required | If provided with a _long_ parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive. |     | _37.781157_ |
| long | required | If provided with a _lat_ parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive. |     | _\-122.400612831116_ |

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/trends/closest.json?lat=37.781157&long=-122.400612831116`