platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks


## Important Notes

* When registering your webhook URL, your web app must authenticate with its consumer token and secret _and the app owner's user access token and secret_. 
* All incoming Direct Messages will be delivered via webhooks. All Direct Messages sent via [POST direct\_messages/events/new (message\_create)](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) will also be delivered via webhooks. This is so your web app can be aware of Direct Messages sent via a different client.
* Note that every webhook event includes a for\_user\_id user ID that indicates which subscription the event was delivered for.
* If you have two users using your web app for Direct Messages in the same conversation, your webhook will receive two duplicate events (one for each user). Your web app should account for this.   
    
* If you have more than one web app sharing the same webhook URL and the same user mapped to each app, the same event will be sent to your webhook multiple times (once per web app).
* In some cases, your webhook may receive duplicate events. Your webhook app should be tolerant of this and dedupe by event ID.
* Do not expect Quick Reply response to directly follow a request. A user has the ability to ignore a Quick Reply request and may respond via traditional Direct Message. The user may also provide a Quick Reply response to a request they have not replied to earlier in the message thread.