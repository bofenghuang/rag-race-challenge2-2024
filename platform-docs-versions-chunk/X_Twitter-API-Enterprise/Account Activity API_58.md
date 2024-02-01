platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/guides/direct-message-migration.html


## Direct Message migration guide

**On September 17th, 2018 we retired the legacy Direct Message endpoints.  
If you had been using those endpoints, please make sure to migrate over to the new Direct Message endpoints or the Account Activity API.**

**Please review [this announcment](https://twittercommunity.com/t/details-and-what-to-expect-from-the-api-deprecations-this-week-on-august-16-2018/110746) to learn more.**

This guide is designed to help you migrate from legacy Direct Message REST APIs to their enhanced replacements which have graduated from beta. Below you will find a summary of the changes, a new features list, and key differences and considerations to help with the transition. The new Direct Message endpoints are available now to all developers. For guidance in migrating from User Streams or Site Streams, see the [migration guide to Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/subscribe-account-activity/migration/us-ss-migration-guide).

* [Summary of changes](#summary)
* [New features](#features)
* [Sending Direct Messages](#sending)
* [Receiving Direct Messages](#receiving)
* [Deleting Direct Messages](#deleting)