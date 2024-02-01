platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets


## Introduction

Non-streaming standard endpoints have been updated to provide edited Tweet metadata. The statuses/filter and statuses/sample streaming endpoints have not been updated, while other endpoints that provide Tweet objects have been updated. The _Edit Tweets_ feature was first introduced for testing among Twitter employees on September 1, 2022. Starting on that date, eligible Tweets are editable for 30 minutes and up to 5 times. _All objects for Tweets created since September 29, 2022_ include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history can be described by chaining these IDs together, starting with the original ID. Additionally, if any Tweet in the edit chain is deleted, all Tweets in that chain are deleted as well. 

These edit metadata details are included when the include\_ext\_edit\_control request parameter is set to true: 

include\_ext\_edit\_control=true

With these new metadata, a developer can find out:  

* If a Tweet was edit eligible at the time of creation. Some Tweets, such as those with polls or scheduled Tweets, cannot be edited.
* Tweets are editable for 30 minutes, and can be edited up to 5 times. For editable Tweets, you can see if time for editing remains and how many more edits are possible.
* If you are viewing an edited version of a Tweet. In most cases, the API will return the most recent version of a Tweet, unless a specific past version is requested by Tweet

One new Tweet attribute has been added at the root level:

* **ext\_edit\_control**  - Provides all Tweet IDs associated with the edit history of the Tweet. The "edit\_tweet\_ids" attribute is an array that provides all IDs associated with its edit history. If the Tweet has not been edited, this array will contain a single ID.

      `"ext_edit_control": { 	"initial": { 	  "edit_tweet_ids":["1550220531252678656"],  	  "editable_until_msecs": "123", 	  "edits_remaining": "5", 	  "is_edit_eligible": true 	} }`
    

Most Tweets are eligible. However, the following types of Tweets are not: