platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/severity-type

# SeverityType

A description of the dangerousness of the threat associated with a [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) object. The order of the values below are ordered from least severe to most severe.

## Values

| Name | Description |
| --- | --- |
| `UNKNOWN` | No rating of severity is available |
| `INFO` | The indicator is associated with a threat of little or no severity. |
| `WARNING` | The indicator is associated with a threat of some severity. |
| `SUSPICIOUS` | The indicator is associated with a threat that is likely severe. |
| `SEVERE` | The indicator is associated with a threat that is severe. |
| `APOCALYPSE` | The indicator is associated with a threat that is extremely severe and should be addressed immediately. |