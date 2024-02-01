platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication?context=linkedin%2Fcontext

# Overview

The LinkedIn API uses [OAuth 2.0](http://oauth.net/2/) for member (user) authorization and API authentication. Applications must be authorized and authenticated before they can fetch data from LinkedIn or get access to LinkedIn member data.

There are two types of Authorization Flows available:

* [**Member Authorization (3-legged OAuth)**](#member-authorization-3-legged-oauth-flow)
* [**Application Authorization (2-legged OAuth)**](#application-authorization-2-legged-oauth-client-credential-flow)

Depending on the type of permissions your integration will require, follow one of the authorization flows to get started.

Note

* There are several third-party libraries in the open source community which abstract the OAuth 2.0 authentication process in every major programming language.
* LinkedIn does not support TLS 1.0.