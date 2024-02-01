platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/quick-replies/api-reference/options

## Option Object[¶](#option-object "Permalink to this headline")

|     |     |
| --- | --- |
| **label** (required) | The text label displayed on the button face. Label text is returned as the user's message response. String, max length of 36 characters including spaces. Values with URLs are not allowed and will return an error. |
| **description** (optional) | Optional description text displayed under label text. All options must have this property defined if property is present in any option. Text is auto-wrapped and will display on a max of two lines and supports `n` for controlling line breaks. Description text is not include in the user's message response. String, max length of 72 characters including spaces. |
| **metadata** (optional) | Metadata that will be sent back in the webhook request. String, max length of 1,000 characters including spaces. |