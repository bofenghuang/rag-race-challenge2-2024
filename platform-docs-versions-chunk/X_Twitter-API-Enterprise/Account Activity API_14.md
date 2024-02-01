platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks


### 1\. Create a Twitter app.

* Create a [Twitter app](https://developer.twitter.com/content/developer-twitter/en/docs/apps) with an approved developer account from the [developer portal](https://developer.twitter.com/content/developer-twitter/en/docs/developer-portal/overview). If you are creating the app on behalf of your company, it is recommended you create the app with a corporate Twitter account. To apply for a developer account, [click here](https://developer.twitter.com/content/developer-twitter/en/apply).
* Enable “Read, Write and Access direct messages” on the [permissions](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/overview/application-permission-model) tab of your app page.
* On the "Keys and Access Tokens" tab, take note of your app's Consumer Key (API Key) and Consumer Token (API Secret).
* On the same tab, generate your app's [Access Token and Access Token Secret](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/guides/access-tokens). You will need these Access Tokens to register your webhook URL, which is where Twitter will send account events.
* If you are unfamiliar with [Twitter Sign-in](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/sign-in-with-twitter) and how user contexts work with the Twitter API review [Obtaining Access Tokens](https://dev.twitter.com/webhooks/access-tokens). As you add accounts for which to receive events, you will subscribe them using that account's access tokens.
* Take note of your app's numeric ID, as seen in the ["Apps"](https://developer.twitter.com/content/developer-twitter/en/docs/apps) page of the [developer portal](https://developer.twitter.com/content/developer-twitter/en/docs/developer-portal/overview). When you apply for Account Activity API access, you'll need this app ID.