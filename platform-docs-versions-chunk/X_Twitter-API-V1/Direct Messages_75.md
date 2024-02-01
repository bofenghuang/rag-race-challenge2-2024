platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/buttons/api-reference/buttons

## CTAs Object[¶](#ctas-object "Permalink to this headline")

Buttons can be added to a Direct Message by defining a `ctas` array of 1-3 objects.

|     |     |
| --- | --- |
| **type** (required) | Defines the type of button to display. Currently must be set to `web_url`. |
| **label** (required) | The text that will be displayed to the user on each button. Max string length of 36 characters. |
| **url** (required) | A valid http or https target URL of the button. |
| **tco\_url** (read only) | The t.co version of the URL will be returned in a POST response and on the read path (GET requests) only. |