platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/custom-profiles/overview

Overview

Custom profiles allow a Direct Message author to present a different identity than that of the Twitter account being used. For example, brands may want customer service agents posting under a single Twitter account to use their own name and photo. A custom profile may also be used to attach a unique identity to a message authored by an automated application or bot so that users clearly understand they are talking to a bot.

## To use the custom profiles feature:

1. Posting accounts must be Verified and on an allowlist to use this feature.
2. Create a custom profile with a name and photo using the API.
3. Attach a custom profile ID to new Direct Message POST requests. Valid custom profiles will override the default avatar.