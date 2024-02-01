platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/introduction


## Introduction

Twitter is committed to our community of developers who build with the Twitter API. As part of this commitment, we aim to make our API open and fair to developers, safe for people on Twitter, and beneficial for the Twitter platform as a whole. It is crucial that any developer who stores Twitter content offline, ensures the data reflects user intent and the current state of content on Twitter. For example, when someone on Twitter deletes a Tweet or their account, protects their Tweets, edits a Tweet, or scrubs the geo information from their Tweets, it is critical for both Twitter and our developers to honor that person’s expectations and intent.

Real-time streams of compliance events provide developers the tools to maintain Twitter data in compliance with the [Twitter Developer Agreement and Policy](https://developer.twitter.com/en/developer-terms/policy). 

There are two c_ompliance event_ streams, one for _Tweet compliance_ events, and one for _User compliance_ events. These streams are available with Enterprise access and are designed to help partners that ingest high volumes of data 'listen' for compliance events such as Tweet edit events.

These streams provide the following events: 

**Tweet compliance stream:** 

* delete - indicates that the Tweet was deleted.
    
* tweet\_edit \- indicates a Tweet has been edited and provides the ID of the updated Tweet. 
    
* withheld - indicates that the Tweet has been withheld from one or more countries. 
    
* drop \- indicates that the Tweet should be removed from public view.  
    
* undrop - indicates that the Tweet may be displayed again and treated as public.
    

**User compliance stream:**   

* user\_delete - indicates that the User account was deleted
    
* user\_undelete - indicates that the User account was undeleted
    
* user\_protect - indicates that the User account became private
    
* user\_unprotect - indicates that the User account became public
    
* user\_withheld - indicates that the User account has been withheld from one or more countries. 
    
* user\_suspend - indicates that the User account was suspended
* user\_unsuspend - indicates that the User account was unsuspended
* user\_profile\_modification - indicates that the User profile has been updated. This includes an updated description, name, location, and URL. 

* ****scrub\_geo**** - indicates that the location information associated with the User was removed
    

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance1/quick-start.html)

[Jump to example requests](https://github.com/twitterdev/Twitter-API-v2-sample-code/tree/main/Batch-Compliance)

[Python client](https://github.com/twitterdev/compliant-client)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/compliance/jobs)