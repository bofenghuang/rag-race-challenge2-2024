platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/expansions

### Available expansions for Tweet payloads

| Expansion | Description |
| --- | --- |
| `author_id` | Returns a user object representing the Tweet’s author |
| `referenced_tweets.id` | Returns a Tweet object that this Tweet is referencing (either as a Retweet, Quoted Tweet, or reply) |
| edit\_history\_tweet\_ids | Returns Tweet objects that are part of a Tweet's edit history |
| `in_reply_to_user_id` | Returns a user object representing the Tweet author this requested Tweet is a reply of |
| `attachments.media_keys` | Returns a media object representing the images, videos, GIFs included in the Tweet |
| `attachments.poll_ids` | Returns a poll object containing metadata for the poll included in the Tweet |
| `geo.place_id` | Returns a place object containing metadata for the location tagged in the Tweet |
| `entities.mentions.username` | Returns a user object for the user mentioned in the Tweet |
| `referenced_tweets.id.author_id` | Returns a user object for the author of the referenced Tweet |