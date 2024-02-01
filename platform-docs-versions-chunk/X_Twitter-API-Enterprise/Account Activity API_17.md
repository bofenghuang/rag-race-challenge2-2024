platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks

### 4\. Validate setup

* To validate your app and webhook are configured correctly, favorite a Tweet posted by one of the Twitter accounts your app is subscribed to. You should receive a `favorite_events` via a POST request to your webhook URL for each Favorite your subscribers receive.
* Note that it may take up to 10 seconds for events to start being delivered after a subscription has been added.