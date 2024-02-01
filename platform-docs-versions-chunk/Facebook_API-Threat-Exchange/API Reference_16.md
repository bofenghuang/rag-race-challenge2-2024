platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags

# ThreatTag

A label which groups [Malware](https://developers.facebook.com/docs/threat-exchange/reference/apis/malware), [ThreatDescriptor](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor), and/or [MalwareFamily](https://developers.facebook.com/docs/threat-exchange/reference/apis/malware-family) objects. Once objects are tagged, you can use tags to narrow your search queries in TE.

## Fields

| Parameter | Description | Type |
| --- | --- | --- |
| `id` | Unique identifier of the threat tag | `number` |
| `text` | The text for this tag | `string` |

### Legal Tags

The text of tags is case insensitive, restricted to letters, numbers, underscores, and colons, and must be UTF-8 friendly. So "שלום" is a valid text, but "#example-tag" is not.