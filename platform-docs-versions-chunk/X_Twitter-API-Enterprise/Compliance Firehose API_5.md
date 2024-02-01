platform: X
topic: Twitter-API-Enterprise
subtopic: Compliance Firehose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Compliance Firehose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/guides/compliance-data-objects

Compliance Data Objects

Possible types of compliance events will include Tweet (or “status”) events and User events, for which there are multiple types described below.    

Please note:

* Read more about User statuses [here](https://support.twitter.com/articles/14016) and our developer policy around deleted Tweets [here](https://dev.twitter.com/overview/terms/policy#3.Update_Respect_Users_Control_and_Privacy).
* The Compliance Firehose has been updated to provide 'tweet\_edit' events. 
* Several User delete, protect and suspend events are not necessarily permanent and can toggle between states infinitely. These include: user\_delete,user\_undelete, user\_protect, user\_unprotect and user\_suspend, user\_unsuspend.
* User\_deletes are followed by status\_deletes 30 days later only if the user has not selected to user\_undelete their account. It is possible that a user\_delete is reversed by the user and deletes for all of their tweets 30 days later do not occur.
* User\_suspend is an action that remains true unless the user is subject to an user\_unsuspend event. These are not subject to any changes on a 30 day time period.

Refer to the ‘Recommended Action’ column to understand how to process each type of event in order to respect the privacy and intent of the end user.  
  

| Original Message Type | Object | Permanent (Yes/No) | Recommended Action |
| --- | --- | --- | --- |
| delete | Status | Yes | Delete associated Tweet. |
| status\_withheld | Status | Yes | Suppress associated Tweet in specific countries listed in the status\_withheld message. |
| drop | Status | No  | Remove the Tweet from public view. |
| undrop | Status | No  | Status may be displayed again and treated as public. |
| tweet\_edit | Status | Yes | Honor and, where relevant, display the new edit. |
| user\_delete | User | No  | Suppress or delete all Tweets by associated user. |
| user\_undelete | User | No  | All Tweets by associated user may be displayed again and treated as public. |
| user\_protect | User | No  | Suppress or delete all Tweets by associated user. |
| user\_unprotect | User | No  | All Tweets by associated user may be displayed again and treated as public. |
| user\_suspend | User | No  | Suppress or delete all Tweets by associated user. |
| user\_unsuspend | User | No  | All Tweets by associated user may be displayed again and treated as public. |
| scrub\_geo | User | Yes | Delete all geodata provided by Twitter for all Tweets by the user prior to the specified Tweet in the scrub\_geomessage. Note that subsequent Tweets by a user may contain geodata that may be used. |
| user\_withheld | User | Yes | Suppress Tweets by associated user in specific countries listed in the user\_withheld message. |
| delete | Favorite | Yes | Delete associated like/favorite. |