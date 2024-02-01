platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin%2Fcontext&tabs=HTTPS1


## Step 2: Request an Authorization Code

To request an authorization code, you must direct the member's browser to LinkedIn's OAuth 2.0 authorization page, where the member either accepts or denies your application's permission request.

Once the request is made, one of the following occurs:

1. If it is a first-time request, the permission request timed out, or was manually revoked by the member: the browser is redirected to LinkedIn's authorization consent window.
    
2. If there is an existing permission grant from the member: the authorization screen is bypassed and the member is immediately redirected to the URL provided in the `redirect_uri` query parameter.
    

When the member completes the authorization process, the browser is redirected to the URL provided in the `redirect_uri` query parameter.

Note

If the `scope` permissions are changed in your app, your users must re-authenticate to ensure that they have explicitly granted your application all of the permissions that it is requesting on their behalf.

    GET https://www.linkedin.com/oauth/v2/authorization
    

| Parameter | Type | Description | Required |
| --- | --- | --- | --- |
| response\_type | string | The value of this field should always be: `code` | Yes |
| client\_id | string | The _API Key_ value generated when you registered your application. | Yes |
| redirect\_uri | url | The URI your users are sent back to after authorization. This value must match one of the _Redirect URLs_ defined in your [application configuration](https://www.linkedin.com/developers/). For example, `https://dev.example.com/auth/linkedin/callback`. | Yes |
| state | string | A unique string value of your choice that is hard to guess. Used to prevent [CSRF](http://en.wikipedia.org/wiki/Cross-site_request_forgery). For example, `state=DCEeFWf45A53sdfKef424`. | No  |
| scope | string | URL-encoded, space-delimited list of member permissions your application is requesting on behalf of the user. These must be explicitly requested. For example, `scope=liteprofile%20emailaddress%20w_member_social`. See [Permissions](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication) and [Best Practices for Application Development](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/application-development?context=linkedin/context) for additional information. | Yes |

The scopes available to your app depend on which Products or Partner Programs your app has access to. This information is available in the [Developer Portal](https://www.linkedin.com/developers/apps). Your app's Auth tab will show current scopes available. You can apply for new Products under the Products tab. If approved, your app will have access to new scopes.

#### Sample Request

    GET https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={your_client_id}&redirect_uri={your_callback_url}&state=foobar&scope=liteprofile%20emailaddress%20w_member_social
    

Once redirected, the member is presented with LinkedIn's authentication screen. This identifies your application and outlines the particular member permissions/scopes that your application is requesting. You can change the logo and application name in the Developer Portal under My apps > [Settings](https://www.linkedin.com/developers/apps)

#### Member Approves Request

By providing valid LinkedIn credentials and clicking **Allow**, the member approves your application's request to access their member data and interact with LinkedIn on their behalf. This approval instructs LinkedIn to redirect the member to the redirect URL that you defined in your `redirect_uri`parameter.

    https://dev.example.com/auth/linkedin/callback?state=foobar&code=AQTQmah11lalyH65DAIivsjsAQV5P-1VTVVebnLl_SCiyMXoIjDmJ4s6rO1VBGP5Hx2542KaR_eNawkrWiCiAGxIaV-TCK-mkxDISDak08tdaBzgUYfnTJL1fHRoDWCcC2L6LXBCR_z2XHzeWSuqTkR1_jO8CeV9E_WshsJBgE-PWElyvsmfuEXLQbCLfj8CHasuLafFpGb0glO4d7M
    

Attached to the `redirect_uri` are two important URL arguments that you need to read from the request:

* `code` — The OAuth 2.0 authorization code.
* `state` — A value used to test for possible [CSRF](http://en.wikipedia.org/wiki/Cross-site_request_forgery) attacks.

The `code` is a value that you exchange with LinkedIn for an OAuth 2.0 access token in the next step of the authentication process. For security reasons, the authorization code has a 30-minute lifespan and must be used immediately. If it expires, you must repeat all of the previous steps to request another authorization code.

Warning

Before you use the authorization code, your application should ensure that the value returned in the `state` parameter matches the `state` value from your original authorization code request. This ensures that you are dealing with the real member and not a malicious script. If the state values do not match, you are likely the victim of a [CSRF](http://en.wikipedia.org/wiki/Cross-site_request_forgery) attack and your application should return a `401 Unauthorized` error code in response.

#### Failed Requests

If the member chooses to cancel, or the request fails for any reason, the client is redirected to your `redirect_uri` with the following additional query parameters appended:

* `error` - A code indicating one of these errors:
    * `user_cancelled_login` - The member declined to log in to their LinkedIn account.
    * `user_cancelled_authorize` - The member refused to authorize the permissions request from your application.
* `error_description` - A URL-encoded textual description that summarizes the error.
* `state` - A value passed by your application to prevent [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) attacks.

For more error details, refer [here](#oauthv2authorization)