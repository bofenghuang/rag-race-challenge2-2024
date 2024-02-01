platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/integrate/compliance-data-objects

Compliance Data Objects

Possible types of compliance events will include Tweet events and User events, for which there are multiple types described below.    

Please note:

* Read more about Tweet visibility [here](https://support.twitter.com/articles/14016) and our developer policy around deleted Tweets [here](https://dev.twitter.com/overview/terms/policy#3.Update_Respect_Users_Control_and_Privacy).
* The Tweet Compliance stream includes events triggered by Tweets getting edited. See the 'tweet\_edit' example event below.  
* Several User delete, protect and suspend events are not necessarily permanent and can toggle between states infinitely. These include: user\_delete, user\_undelete, user\_protect, user\_unprotect and user\_suspend, user\_unsuspend.
* User\_deletes are followed by Tweet deletes 30 days later only if the user has not selected to user\_undelete their account. It is possible that a user\_delete is reversed by the user and deletes for all of their Tweets 30 days later do not occur.
* User\_suspend is an action that remains true unless the user is subject to an user\_unsuspend event. These are not subject to any changes on a 30 day time period.

Refer to the ‘Recommended Action’ column to understand how to process each type of event in order to respect the privacy and intent of the end user.