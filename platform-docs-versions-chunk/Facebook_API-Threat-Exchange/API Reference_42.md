platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates


## What changes constitute an Update

`/threat_updates` will generate an update to changes to [ThreatDescriptor objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor/) that have been shared to the PrivacyGroup. Changes to the fields or connected data will generate an update.

At a minimum, this is:

1. If a [ThreatDescriptor objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor/) is added to the PrivacyGroup, removed from the PrivacyGroup, or deleted.
2. Changes to fields directly stored on the [ThreatDescriptor objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor/)
3. Changes in which [ThreatTags](https://developers.facebook.com/docs/threat-exchange/reference/apis/docs/threat-exchange/reference/apis/threattags/) are on those ThreatDescriptors
4. Changes in which [Reactions](https://developers.facebook.com/docs/threat-exchange/reference/apis/docs/threat-exchange/reference/apis/threattags/) are on those ThreatDescriptors

Note that not every update will appear to have changed data - `/threat_updates` only stores the last update to an object, and so changes that are rapidly undone may not appear to change your copy of the data. Additionally, if you select only some fields, you will see updates that don't change the fields you selected.