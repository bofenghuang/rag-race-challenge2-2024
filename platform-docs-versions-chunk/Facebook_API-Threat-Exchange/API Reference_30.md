platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type

# ReviewStatusType

Indicates if the data was reviewed and, if via automation or a human.

## Values

| Name | Description |
| --- | --- |
| `UNKNOWN` | No review data available. |
| `UNREVIEWED` | The data has not been reviewed. |
| `PENDING` | The data is currently under review. |
| `REVIEWED_MANUALLY` | The data was reviewed manually. |
| `REVIEWED_AUTOMATICALLY` | The data was reviewed by an automated system. Note that you cannot set this value if the current value is REVIEWED\_MANUALLY. This restriction was added to prevent automated systems from clobbering the work of human reviewers. To get around this, you must first change the review status to another value, e.g. PENDING, and then change it to REVIEWED\_AUTOMATICALLY. |