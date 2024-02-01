platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/post-compliance-jobs


### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | The unique identifier for this job. |
| `created_at` | date (ISO 8601) | The date and time when the job was created. |
| `type` | enum (`tweets`, `users`) | The type of the job, whether tweets or users. |
| `name` | string | The user defined job name. Only returned if specified when the job was created. |
| `upload_url` | string | A URL representing the location where to upload Tweet IDs consumed by your App. This URL is already signed with an authentication key, so you will not need to pass any additional credentials or headers to authenticate the request. |
| `upload_expires_at` | date (ISO 8601) | The date and time until which the upload URL will be available (usually 15 minutes from the request time). |
| `download_url` | string | The predefined location where to download the results from the compliance job. This URL is already signed with an authentication key, so you will not need to pass any additional credentials or headers to authenticate the request. |
| `download_expires_at` | date (ISO 8601) | The date and time until which the download URL will be available (usually seven days from the request time). |