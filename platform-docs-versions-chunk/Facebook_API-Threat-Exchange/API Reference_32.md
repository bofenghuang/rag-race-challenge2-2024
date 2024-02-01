platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/signature-type

# SignatureType

The kind or format of signature described by a [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) object with [ThreatType](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-type) of `SIGNATURE`.

## Values

| Name | Description |
| --- | --- |
| `BRO` | A signature string compatible with a Bro sensor |
| `REGEX_URL` | A PCRE compatible regular expression |
| `SNORT` | A signature string compatible with the Snort format |
| `SURICATA` | A signature string compatible with the Suricata format |
| `UNKNOWN` | An unknown signature type |
| `YARA` | A signature string compatible with the Yara format |