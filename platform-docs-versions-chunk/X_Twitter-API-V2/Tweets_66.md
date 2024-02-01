platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/introduction

Introduction

## Introduction

The Twitter API v2 has three timelines endpoints - reverse chronological home timeline, user Tweet timeline, and user mention timeline. See below for more details.

These three timelines endpoints support edited Tweets. These endpoints will always return the most recent edit, along with the edit history. Any Tweet collected after its 30-minute edit window will represent its final version. Edit metadata includes an array of IDs for all Tweets in its history. For Tweets with no edit history, this array will hold a single ID. For Tweets that have been edited, this array contains multiple IDs, arranged in ascending order reflecting the order of edits, with the most recent version in the last position of the array. To learn more about how Tweet edits work, see the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/edit-tweets) page.