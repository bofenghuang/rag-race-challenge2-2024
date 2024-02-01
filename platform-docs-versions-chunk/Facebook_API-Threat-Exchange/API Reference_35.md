platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type

# StatusType

StatusType is an important field in ThreatExchange, as it corresponds to whether the upload is referring to malicious or harmful content. This help you determine what the original uploader's intent was in uploading signals, and therefore what you should do when you find matching or corresponding data on your platform.

## Values

| Name | Cybersecurity Description | Content Safety Description |
| --- | --- | --- |
| `MALICIOUS` | The object is consistently malicious | Corresponds to harmful content or behavior. |
| `SUSPICIOUS` | The object can be malicious, dependent on the context in which it is found | Helps discover harmful content or requires additional investigation to discover harmful content. |
| `NON_MALICIOUS` | The object is not known to be malicious | Informational or trend information that does not lead to the discovery of harmful content. |
| `UNKNOWN` | No maliciousness information available | Do not use this StatusType for content safety. |