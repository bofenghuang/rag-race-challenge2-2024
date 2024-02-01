platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/best-practices

## Consider Privacy Rules

ThreatTags are visible based on the [PrivacyType](https://developers.facebook.com/docs/threat-exchange/reference/apis/privacy-type/) of the tagged data. For example, if the tag `public_tag` is on ANY descriptor that is publically visible (privacy type of VISIBLE), then the tag is visible to all members. Conversely, if the tag `nonpublic_tag` is ONLY on tagged objects shared to specific members (privacy types \`HAS\_WHITELIST\` or \`HAS\_PRIVACY\_GROUP\`), then the tag is only visible to those members. Tag your data accordingly. Learn more about [PrivacyType tag](https://developers.facebook.com/docs/threat-exchange/reference/apis/privacy-type/).

For more uses cases with ThreatTags, see the [ThreatTag reference](https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags/).