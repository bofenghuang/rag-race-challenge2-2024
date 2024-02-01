platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/introduction

Introduction

## Introduction

### List members lookup

Members lookup group has two available endpoints. You are able to retrieve details on members of a specified List and see which Lists a user is a member of. These endpoints can be used to enable people to curate and organize new Lists based on the membership information.

There is a rate limit of 900 requests per 15 minutes when looking up member details and a limit of 75 requests per 15 minutes when looking up user memberships.

You can use [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) to authenticate your requests to this endpoint.