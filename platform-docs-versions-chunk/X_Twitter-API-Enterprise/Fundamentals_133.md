platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets


## Introduction

Enterprise endpoints have been updated to provide edited Tweet metadata. The _Edit Tweets_ feature was first introduced for testing among Twitter employees on September 1, 2022. Starting on that date, eligible Tweets were editable for 30 minutes and up to 5 times. _All objects for Tweets created since September 29, 2022_ include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history can be described by chaining these IDs together, starting with the original ID. Additionally, if any Tweet in the edit chain is deleted, all Tweets in that chain are deleted as well. 

These metadata details are included automatically. No request parameters are needed to include available edit history as part of the Tweet object. 

With these new metadata, a developer can find out:

* If a Tweet was edit eligible at the time of creation. Some Tweets, such as those with polls or scheduled Tweets, cannot be edited.
* Tweets are editable for 30 minutes, and can be edited up to 5 times. For editable Tweets, you can see if time for editing remains and how many more edits are possible.
* If you are viewing an edited version of a Tweet. In most cases, the API will return the most recent version of a Tweet, unless a specific past version is requested by Tweet ID.

Three new Tweet attributes have been added at the root level:

* **edit\_history**  - Provides all Tweet IDs associated with the edit history of the Tweet. The "initial\_tweet\_id" attribute indicates the original Tweet and the "edit\_tweet\_ids" attribute is an array that provides all IDs associated with its edit history. If the Tweet has not been edited, this array will contain a single ID.

"edit\_history": {
    "initial\_tweet\_id": "1283764123"
    "edit\_tweet\_ids": \["1283764123"\]
  }

* **edit\_controls** - Provides attributes that indicate when the 30-minute edit window ends and how many potential edits remain. 

"edit\_controls": {  
     "editable\_until\_ms": 1660155761384
     "edits\_remaining": 3   
  }

* **editable** - Indicates whether a Tweet was eligible for editing when created. 

"editable": true

Most Tweets are eligible. However, the following types of Tweets are not: 

* Tweet is promoted
* Tweet has a poll
* Tweet is a non-self-thread reply
* Tweet is a Retweet (note that Quote Tweets are eligible for edit)
* Tweet is nullcast
* Community Tweet
* Superfollow Tweet
* Collaborative Tweet

Example attributes for unedited Tweet