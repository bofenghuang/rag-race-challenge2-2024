platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/introduction

Introduction

## Introduction

Bookmarks are a core feature of the Twitter app that allows you to “save” Tweets and easily access them later. With these endpoints, you can retrieve, create, delete or build solutions to manage your Bookmarks via the API.  

### Manage Bookmarks

We have two available methods for manage Bookmarks, POST and DELETE. The POST method lets you create Bookmarks. Likewise, the DELETE method allows you to delete a specific Bookmark. 

There is a per-user rate limit of 50 requests per 15 minutes for the POST and DELETE methods.

Since you are making requests on behalf of a user with the manage Bookmarks endpoints, you must authenticate by generating a user Access Token with OAuth 2.0. You can use the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) to do so. To use this endpoint you must pass in the scopes `tweet.read`, `users.read`, and  `bookmark.write`.