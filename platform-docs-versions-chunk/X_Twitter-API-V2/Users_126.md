platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/mutes/introduction


## Introduction

Muting an account allows you to remove an account's Tweets from your timeline without unfollowing or blocking that account. Muted accounts will not know that you've muted them and you can unmute them at any time. With manage mutes endpoints, developers can create safer experiences for people on Twitter. One example of how to build with manage mutes is an application that allows you to mute accounts that might Tweet about specific topics for a specified length of time. With the mutes lookup endpoint, you can see who you or an authenticated user has muted. This can be useful to determine how you interact with the muted accounts. 

Since you are making requests for private information with mute lookup, and on behalf of a user with manage mutes, you must authenticate these endpoints with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), and use the user Access Tokens associated with a user that has authorized your App, which can be generated using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) (OAuth 1.0a) or the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).