platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/best-practices

## Tag Your Data

By [tagging your data](https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags/), it makes it easier for yourself and others to find the indicators they care most about. For example, by tagging descriptors with `evil`, this allows others to filter descriptors searches by data with that tag. Another option is that you can then search the `threat_tags` endpoint by that tag and see all the tagged objects visible to you. The tagging endpoint also supports partial matches on tags, so a query for `evil` will surface any tags visible to you which are like `evil*`.

## Be Descriptive with Your Tags

ThreatTags (also known as "subjective tags") contain metadata fields describing what they are. If you create the tag `foo`, others can inspect the metadata to see what means or why the data was tagged. But it's helpful to be more descriptive instead; for example, `campaign_zeusbotnet` or `malicious_ssl_cert`.