platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor


## Fields

| Parameter | Description | Type |
| --- | --- | --- |
| `id` | Unique identifier of the threat descriptor. Automatically assigned at create time, and non-editable. | `number` |
| `added_on` | The datetime this descriptor was first uploaded. Automatically computed; not directly editable. | `string` |
| `confidence` | A rating, from 0-100, on how confident the publisher is of the threat indicator's status. 0 is meant to be least confident, with 100 being most confident. | `number` |
| `description` | A short summary of the indicator and threat. | `string` |
| `expired_on` | Datetime the indicator is no longer considered a threat, as subjectively determined by the owner of the descriptor. | `number` |
| `first_active` | The datetime when this opinion first became valid, as subjectively determined by the owner of the descriptor. | `string` |
| `last_active` | The datetime when this opinion stopped being valid, as subjectively determined by the owner of the descriptor. | `string` |
| `indicator` | The [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) described by the descriptor: for example, a URL or a hash string. Non-editable after the descriptor is created. | [`ThreatIndicator`](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) |
| `last_updated` | Datetime the threat descriptor was last updated. Automatically computed; not directly editable. | `string` |
| `my_reactions` | A list of reactions that you have added to this descriptor. | [`ReactionType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/reaction-type) |
| `owner` | The [ThreatExchangeMember](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) that submitted the descriptor. Non-editable. | [`ThreatExchangeMember`](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) |
| `precision` | The degree of accuracy of the descriptor. | [`PrecisionType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/precision-type) |
| `privacy_type` | The level of privacy applied to the descriptor. Also known as "visibility". | [`PrivacyType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/privacy-type) |
| `raw_indicator` | A raw, unsanitized string of the indicator being described. | `string` |
| `reactions` | A list of reactions to reacting application. | [`ReactionType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/reaction-type) |
| `review_status` | Describes how the indicator was vetted. | [`ReviewStatusType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type) |
| `severity` | Dangerousness of threat associated with the indicator. | [`SeverityType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/severity-type) |
| `share_level` | A designation of how the indicator may be shared, based on the [US-CERT's Traffic Light Protocol](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.us-cert.gov%2Ftlp%2F&h=AT1Lb6l0qN6j4mzPRKvbGVul11UnpqHVYAjrw6qXi5huQP8k7K4gJ5eVak1mLG73RwNRU_81SKPCyPRKgxV1wR0p2dE0OlNOeTezxNE7FENmpTcT8ug_aR9vmlfZZWsohiXpElR8jtPsrtTN). | [`ShareLevelType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/share-level-type) |
| `source_uri` | A publicly accessible URL containing further context or details about the descriptor. | `string` |
| `status` | If the indicator is known to be malicious or not. | [`StatusType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type) |
| `type` | The type of indicator. | [`IndicatorType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type) |