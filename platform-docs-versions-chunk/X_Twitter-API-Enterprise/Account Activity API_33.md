platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries


### What are retries?

The Account Activity API provides a retry feature when the client's web app does not return a 'success' 200 response for an account activity webhook event. When the client-side does not confirm the successful receipt of an event, Twitter assumes the event was not received. If a non-200 response is received, a response isn't received within three seconds, or we don't receive a response at all, we retry the request and leave that open for three seconds. This means that you have roughly five seconds over two attempts to respond to receive the activity that we are trying to send to your webhook URL. In the event that your server doesn't response or returns a transient error, we will retry for five minutes. There will be a total of three retry attempts to confirm validation. This allows redundancy and insurance that you receive all webhook events. Note that subscriptions with retries will get retried events for any/all activities for all subscribed users on their webhook.

If you do not confirm validation within these eight attempts, the activity will no longer be available via the Account Activity API.