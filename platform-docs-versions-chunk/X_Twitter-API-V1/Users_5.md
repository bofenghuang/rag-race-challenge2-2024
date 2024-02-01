platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/get-account-verify_credentials


## Request a User's Email Address[¶](#request-a-user-s-email-address "Permalink to this headline")

The "Request email addresses from users" checkbox is available under the app permissions on [developer.twitter.com](https://developer.twitter.com/en/docs/basics/developer-portal/guides/apps). Privacy Policy URL and Terms of Service URL fields must be completed in the app settings in order for email address access to function. If enabled, users will be informed via the [oauth/authorize](https://developer.twitter.com/oauth/reference/get/oauth/authorize) dialog that your app can access their email address.

**Please note** - Your app will need to regenerate the user access tokens for previously authenticated users to access their email address.

**Please note** - You can view and edit your existing [Twitter apps](https://developer.twitter.com/en/docs/basics/developer-portal/guides/apps) via the [Twitter app dashboard](https://developer.twitter.com/en/apps) if you are logged into your Twitter account on developer.twitter.com.