platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/expansions

### Available expansion for User payloads

| Expansion | Description |
| --- | --- |
| `pinned_tweet_id` | Returns a Tweet object representing the Tweet pinned to the top of the user’s profile |

### Available expansions for Direct Message event payloads

| Expansion | Description |
| --- | --- |
| `attachments.media_keys` | Returns a Media object that was attached to a Direct Message |
| `referenced_tweets.id` | Returns a Tweet object that was referenced in a Direct Message |
| `sender_id` | Returns a User object representing the author of a Direct Message and who invited a participant to join a conversation |
| `participant_ids` | Returns a User object representing a participant that joined or left a conversation |