platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/disconnections-explained


## Disconnections explained

Disconnects from your PowerTrack stream can happen for a handful of reasons - whether they proactively planned or unplanned. Regardless of whether or not they were planned, any sort of disconnect can be surprising cause for data loss, but they don’t have to be. A basic understanding of the types of disconnects that you might encounter and how to quickly reconnect can mean the difference between a major issue and something that can be incorporated into your application design by reconnecting, or using Backfill or [Recovery](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#replay). Please note that for any disconnect, forced or client-side, your [console.gnip.com dashboard](https://console.gnip.com/) will have a message that displays the kind of disconnect that you experienced and a timestamp for the disconnect.  

This article will go over the types of disconnects you might encounter, how to minimize their effects, and how to troubleshoot issues related to disconnects.