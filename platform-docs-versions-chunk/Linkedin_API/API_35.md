platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/programmatic-refresh-tokens?context=linkedin%2Fcontext


## Introduction

Refresh tokens are used to get a new access token when your current access token expires. For more information, see the OAuth 2.0 [RFC](https://tools.ietf.org/html/rfc6749#section-1.5).

LinkedIn offers programmatic refresh tokens that are valid for a fixed length of time. By default, access tokens are valid for 60 days and programmatic refresh tokens are valid for a year. The member must reauthorize your application when refresh tokens expire.

When you use a refresh token to generate a new access token, the lifespan or Time To Live (TTL) of the refresh token remains the same as specified in the initial OAuth flow (365 days), and the new access token has a new TTL of 60 days.

For example, on:

* Day 1 - Your refresh token has a TTL of 365 days, and your access token has a TTL of 60 days.
* Day 59 - If you generate a new access token using the refresh token, the access token will have a TTL of 60 days and the refresh token will have a TTL of 306 days (365-59=306).
* Day 360- If you generate a new access token, your access token and refresh token will both expire in 5 days (365-360=5) and you must get your application reauthorized by the member using the authorization flow.

Note

Refresh Tokens are useful in minting new Access tokens and allow for seamless operations for extended periods of time. However, LinkedIn reserves the right to revoke Refresh Tokens or Access Tokens at any time due to technical or policy reasons. In such scenarios, the expectation from products leveraging Refresh Tokens is to fallback to the standard OAuth flow, and present the login screen to the end users.