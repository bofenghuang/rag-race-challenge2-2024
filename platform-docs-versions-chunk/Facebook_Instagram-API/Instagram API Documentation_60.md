platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/hashtag-search

# Hashtag Search

Find public IG Media that has been tagged with specific hashtags.

## Limitations

* You can query a maximum of 30 unique hashtags on behalf of an Instagram Business or Creator Account within a rolling, 7 day period. Once you query a hashtag, it will [count against this limit](https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags) for 7 days. Subsequent queries on the same hashtag within this time frame will not count against your limit, and will not reset its initial query 7 day timer.
* You cannot comment on hashtagged media objects discovered through the API.
* Hashtags on Stories are not supported.
* Emojis in hashtag queries are not supported.
* The API will return a generic error for any requests that include hashtags that we have deemed sensitive or offensive.

[](#)