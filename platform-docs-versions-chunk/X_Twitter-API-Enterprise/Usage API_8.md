platform: X
topic: Twitter-API-Enterprise
subtopic: Usage API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Usage API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/usage-api/api-reference/get-usage

## Data Format [¶](#data-format- "Permalink to this headline")

The following tables describe the root-level data structures for usage data returned from the Usage API. For fields with multiple levels of sub-fields, click the links provided to reveal details about the sub-fields.

If you would like to see an sample of a full Usage API payload, please visit [this page](https://developer.twitter.com/en/docs/developer-utilities/usage-api/overview).

|     |     |
| --- | --- |
| **account** | An object representing the account for which usage data was requested. |
| **bucket** | The unit of time for which usage data is provided. Can be either 'day' or 'month'. |
| **fromDate** | The earliest UTC timestamp for which you want to pull usage data (inclusive). |
| **toDate** | The latest UTC timestamp for which you want to pull usage data (exclusive). |
| **publishers** | Includes three primary objects: Used, projected, and products. |