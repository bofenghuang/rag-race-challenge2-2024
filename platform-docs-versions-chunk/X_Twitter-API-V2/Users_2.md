platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction


## Introduction

The RESTful endpoint uses the GET method to return information about a user or group of users, specified by a user ID or a username. The response includes one or many [user objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user), which deliver fields such as the Follower count, location, pinned Tweet ID, and profile bio. Responses can also optionally include expansions to return the full Tweet object for a user’s pinned Tweet, including the Tweet text, author, and other Tweet fields. 

You can authenticate your request to all users lookup endpoints other than the authenticated user lookup with [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), or [OAuth 2.0 Authorization code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). However, if you would like to access private metrics or data from private users, you will need to utilize OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and pass the authenticated users' Access Token with your request.    

This endpoint is commonly used to receive up-to-date details on a user, to verify that a user exists, or to update your stored details following a compliance event.