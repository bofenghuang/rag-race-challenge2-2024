platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/post-compliance-jobs

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `type`  <br> Required | enum (`tweets`, `users`) | Specify whether you will be uploading tweet or user IDs. You can either specify tweets or users. |
| `name`  <br> Optional | string | A name for this job, useful to identify multiple jobs using a label you define. |
| `resumable`  <br> Optional | boolean | Specifies whether to enable the upload URL with support for resumable uploads. If true, this endpoint will return a pre-signed URL with resumable uploads enabled. |