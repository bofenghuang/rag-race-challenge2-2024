platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/migration/introduction


## Migration introduction

**We retired the Site Streams, User Streams, and standard beta version of the Account Activity API - DM Only products in 2018. If you had been using those products, please make sure to migrate over to the premium or enterprise version of the Account Activity API.**

**We have also retired the legacy Direct Message endpoints. If you had been using those endpoints, please make sure to migrate over to either the new DM endpoints, or to the premium or enterprise version of the Account Activity API.** 

**Please review [this announcment](https://twittercommunity.com/t/details-and-what-to-expect-from-the-api-deprecations-this-week-on-august-16-2018/110746) to learn more.**

Here are the endpoints that will be affected by these changes:  

* User Streams
* Site Streams
* GET direct\_messages
* GET direct\_messages/sent
* GET direct\_messages/show
* POST direct\_messages/new
* POST direct\_messages/destroy  
     

We have new endpoints and services available that provide similar access and, for Direct Messages, some additional functionality:

* Account Activity API [enterprise](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise) and [premium](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/premium/account-activity-api/api-reference/aaa-premium)
* [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events)
* [GET direct\_messages/events/show](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-event)
* [POST direct\_messages/events/new](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/new-event)
* [POST direct\_messages/events/destroy](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/delete-message-event) 

To help you make a smooth migration to these new endpoints and services we have two migration guides:

* [Account Activity API migration guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/migration/us-ss-migration-guide) for those going from User Streams and Site Streams to our new webhooks based service
* [Direct Message migration guide](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/guides/direct-message-migration) for those migrating between Direct Message REST endpoints  
     

Additionally, we have a [series of videos](https://www.youtube.com/playlist?list=PLFKjcMIU2WshGG6Yj940XM7Z6BFs1zfBg) about the Account Activity API and how to get started.

And, finally, we have code samples to further your understanding and help you get started quickly:

* The [Account Activity Dashboard](https://github.com/twitterdev/Account-Activity-dashboard) is a sample Node.js web app with helper scripts to get started with the Account Activity API.
* [SnowBot](https://github.com/twitterdev/SnowBotDev) is a sample chatbot using the Account Activity API and REST Direct Message endpoints. It’s written in Ruby, uses the Sinatra web app framework, and is deployed on Heroku.  
     

If you are building solutions that ingest data and respond in Direct Messages we also have a [Building a Customer Engagement Application on Twitter playbook](https://developer.twitter.com/en/docs/tutorials/customer-engagement-application-playbook).