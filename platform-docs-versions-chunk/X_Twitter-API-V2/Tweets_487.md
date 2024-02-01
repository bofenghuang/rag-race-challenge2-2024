platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/integrate/manage-replies-in-realtime

### Strive for transparency

Because Perspective is not trained on actual Tweets, certain language nuances may cause this app to hide a reply that a user wants to remain unhidden. Regardless of the technology or the approach you use when designing your app, always make the best possible effort to ensure that your users understand what your app has hidden and can make changes.

* The best option is to always trust the user and to give them full control over their decisions. This means your user experience should include controls to undo any action taken by your app on behalf of the user.
* When using an artificial intelligence, your app should use a very high confidence threshold to detect and hide Tweets.
* Not everybody uses the same words, and your app should be designed to avoid any bias. Be mindful of reclaimed words and slang that may lead to false positives.
* If you are training an artificial intelligence, consider adopting a model that closely reflects language often used on Twitter.