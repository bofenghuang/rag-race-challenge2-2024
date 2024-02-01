platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator

# ThreatIndicator

An indicator of compromise.

## Fields

| Parameter | Description | Type |
| --- | --- | --- |
| `id` | Unique identifier of the threat indicator. Automatically assigned at create time, and non-editable. | `number` |
| `indicator` | The value of the indicator. Non-editable after initial creation of the indicator. | `string` |
| `type` | The type of indicator. Non-editable after initial creation of the indicator. | List of [`IndicatorType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type) |

### Sample Usage

Example query for a specific indicator: 788497497903212:

https://graph.facebook.com/`v19.0`/788497497903212/?access\_token=555|aSdF123GhK

Data returned:

{
   "indicator": "facebook.com",
   "type": "DOMAIN",
   "id": "788497497903212"
}