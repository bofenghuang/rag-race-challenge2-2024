platform: X
topic: Twitter-API-Enterprise
subtopic: Usage API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Usage API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/usage-api/api-reference/get-usage

## Best Practices & Limitations [¶](#best-practices-limitations- "Permalink to this headline")

#### Data Availability

Usage data is based on deduped activities consumed through the last full time period (UTC) that data was processed. Data is generally processed and updated up to the minute, except in cases where Gnip is deploying systems.

* The Usage API allows you to access usage data since May 1, 2018.  After July 1, 2019 Usage API allows you to access usage data for the **trailing 13 calendar months**.   
    
* You have the ability to access usage data in **three month intervals** defined with a fromDate and toDate