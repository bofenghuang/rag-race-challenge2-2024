platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/resharing

## Re-sharing options via `share_level`

The re-sharing definitions adopted by ThreatExchange are derived from those definied in the [US-CERT's Traffic Light Protocol](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.us-cert.gov%2Ftlp&h=AT2RqoQ9jVSsk_9ckBFWqeHaFLLaAo-6zyPEsPQkea4qvfmmLGIKghLv_XRNh_t5LkH7w6yGG49_h4ec4u0zUMdZam4OB7x6VOgPIC8ZDTC_T0lA3EGBYjFHIwVDhMYYTWo1j0CrSEXwWzEI). They have been adapted to accomodate the realities of re-sharing within large corporations with complex subsidiary relationships.

The exact definitions of the permitted values in the `share_level` attribute are defined in the [ShareLevelType](https://developers.facebook.com/docs/threat-exchange/reference/apis/share-level-type/).

## Setting re-sharing: examples

The following is an examples are submissions of a new malicious domain to ThreatExchange. In each example, we define which re-sharing level is permitted.

### Specifying re-sharing using the UI