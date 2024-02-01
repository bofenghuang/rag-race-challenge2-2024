platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling?context=linkedin%2Fcontext


## 401 Unauthorized

`401 Unauthorized` errors are usually caused by a problem in the request header of your API call. For example, if you don't use a valid access token when you make an API call on behalf of a LinkedIn member, a `401 Unauthorized` error is returned. Some common cases are:

| Error Type | Fix |
| --- | --- |
| Unknown authentication schema | Unrecognized authentication header schema. Make sure the authentication header follows the format `Authorization: Bearer (your access token)` |
| Empty OAuth2 access token | The authentication header is missing or empty. Make sure the authentication header follows the format `Authorization: Bearer (your access token)` |
| Invalid access token | Incorrect access token, make sure you follow the [authentication procedure](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication) to get a correct access token. |
| Expired access token | The access token has expired, see [how to refresh your access token](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) |
| The token has been revoked | The access token has been revoked by the member from their privacy settings on LinkedIn’s website. To continue using your application, the member has to re-authenticate to get a new access token for your application. |

Note

Access token downstream verification failures return a [`500 Internal Server Error`](#500-internal-server-error).