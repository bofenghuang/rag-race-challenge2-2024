platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/edit-tweets


## Introduction

The Twitter API v2 endpoints provide edited Tweet metadata. The _Edit Tweets_ feature was first introduced for testing among Twitter employees on September 1, 2022. Starting on that date, eligible Tweets are editable for 30 minutes and up to 5 times. _All objects for Tweets created since September 29, 2022_ include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history can be described by chaining these IDs together, starting with the original ID.  Additionally, if any Tweet in the edit chain is deleted, all Tweets in that chain are deleted as well.

Using the Twitter API v2, a developer can find out:

* If a Tweet was edit eligible at the time of creation. Some Tweets, such as those with polls or scheduled Tweets, can not be edited.
* Tweets are editable for 30 minutes, and can be edited up to 5 times. For editable Tweets you can see if time for editing remains and how many more edits are possible.
* If you are viewing an edited version of a Tweet (in most cases the API will return the most recent version of a Tweet, unless a specific past version is requested by Tweet ID).
* The entire edit history of the Tweet.
* The engagement attributed to each version of the Tweet.

There are three components to a Tweet’s edit history:

1. By default, the Tweet payload will contain an array of Tweet IDs that are part of a Tweet’s edit history. This information is specified by the edit\_history\_tweet\_ids, which is a default field in the Tweet payload. This array will contain at least one ID, the ID of the original, unedited Tweet. When there is only one ID that means the Tweet has no edit history. 
2. You can get information such as whether a Tweet was editable at the time it was created, how much time, if any, is remaining for a Tweet to be edited, and how many edits remain by specifying edit\_controls in your [tweet.fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter.
3. Finally, you can get the Tweet objects for each Tweet in a Tweet’s edit history, by specifying the edit\_history\_tweet\_ids using the [expansion](https://developer.twitter.com/en/docs/twitter-api/expansions) parameter

Most Tweets are eligible for editing. However, the following types of Tweets are not:   

* Tweet is promoted
* Tweet has a poll
* Tweet is a non-self-thread reply
* Tweet is a Retweet (note that Quote Tweets are eligible for edit)
* Tweet is nullcast
* Community Tweet
* Superfollow Tweet
* Collaborative Tweet

Examples