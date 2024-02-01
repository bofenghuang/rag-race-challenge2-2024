platform: X
topic: Twitter-API-V1
subtopic: Trends
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Trends.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/trends/trends-for-location/api-reference/get-trends-place

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/trends/place.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 75  |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numeric value that represents the location from where to return trending information for from. Formerly linked to the Yahoo! Where On Earth ID Global information is available by using _1_ as the _WOEID_ . |     | _1_ |
| exclude | optional | Setting this equal to _hashtags_ will remove all hashtags from the trends list. |     |     |