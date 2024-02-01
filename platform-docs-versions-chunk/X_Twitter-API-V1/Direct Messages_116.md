platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/customer-feedback/api-reference/create


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **type** (required) | The Feedback type. Possible values: csat, nps (case sensitive) |
| **to\_user\_id** (required) | The ID of the user who should receive the Feedback prompt in a direct message. |
| **message** (required) | The Direct Message text used to introduce the Feedback prompt. |
| **privacy\_url** (required) | The URL to the sender’s hosted privacy policy. The sender is the business owner of the @username. |
| **external\_id** (optional) | An open field to track case IDs, conversation IDs, etc with a max length of 256 characters. |
| **question\_variant\_id** (optional) | The ID of the relative question variant text that will override the default text. See NPS Question Variants and CSAT Question Variants sections. Default value is 0 if not provided. |
| **display\_name** (optional) | Overrides the display name in the question text only (i.e. "How likely are you to recommend <display\_name> to a friend?" Max length of 20 characters.)<br><br>Confirmation messaging uses the default Twitter display name from the business’ profile. |
| **test** (optional) | Boolean value. Default is false. If true, we will exclude this feedback from analytics / aggregations.<br><br>This value should be used for any testing activity. |