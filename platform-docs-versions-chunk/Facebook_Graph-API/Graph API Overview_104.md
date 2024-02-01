platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/secure-requests

## Encryption

When connecting to our servers your client must use TLS and be able to verify a certificate signed using [`sha256WithRSAEncryption`](http://l.facebook.com/l.php?u=http%3A%2F%2Fwww.alvestrand.no%2Fobjectid%2F1.2.840.113549.1.1.11.html&h=AT0H1HgVndsi58yMn_BbIQ5ms1nRRvjZtUrQ7aOpSOK9SjREh6iNP3009nOboMMgkIwg9aSY1n6KDNiBXHN3s4nJ9v_YCZZphY1GRqDpXgNE7OgHpBM8s_xCmRXqNoeO6cnQIoa7JQhSEj53).

Graph API supports TLS 1.2 and 1.3 and non-static RSA cipher suites. We are currently deprecating support for older TLS versions and static RSA cipher suites. Version 16.0 no longer supports TLS versions older than 1.1 or static RSA cipher suites. This change will apply to all API versions on May 3, 2023.