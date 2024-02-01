platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-details/


### TargetingInfo

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| number\_of\_users\_targeted | string | The total number of users targeted. | "20K" |
| country | list<string> | The targeted countries. | \["FR", "GB"\] |
| age | map<string,bool> | The targeted ages. | {<br><br>"female": true,<br><br>"male": false,<br><br>"unknown": true<br><br>} |
| gender | map<string,bool> | The targeted genders. | {<br><br>"13-17": false,<br><br>"18-24": false,<br><br>"25-34": false,<br><br>"35-44": true,<br><br>"35-44": true,<br><br>"55+": true,<br><br>} |
| audience\_targeting | string | A flag that indicates if the user is part of an audience list uploaded by the advertiser. | "Yes" |
| video\_interactions | string | The list of video categories that the user engaged with | "Entertainment" |
| creator\_interactions | string | The list of creator categories based on how the user followed or viewed creators | "Talent" |
| interest | string | The list of interest categories that the viewers of this ad were grouped into | "News & Entertainment, Business Services" |