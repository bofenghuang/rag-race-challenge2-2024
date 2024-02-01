platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/connecting

## Connection churn

Repeatedly opening and closing a connection (churn) wastes server resources. Keep your connections as stable and long-lived as possible.

Avoid mobile (cellular network) connections from mobile devices. WiFi is generally OK.

Delay opening a streaming connection in cases where the user may quit the application quickly.

If your client works in an environment where the connection quality changes over time, attempt to detect flaky connections. When detected, fall back to REST polling until the connection quality improves.