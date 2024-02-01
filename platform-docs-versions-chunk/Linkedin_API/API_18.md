platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin%2Fcontext&tabs=HTTPS1


## Step 3: Exchange Authorization Code for an Access Token

The next step is to get an access token for your application using the authorization code from the previous step.

    POST https://www.linkedin.com/oauth/v2/accessToken
    

To do this, make the following HTTP POST request with a `Content-Type` header of `x-www-form-urlencoded` using the following parameters:

| Parameter | Type | Description | Required |
| --- | --- | --- | --- |
| grant\_type | string | The value of this field should always be: `authorization_code` | Yes |
| code | string | The authorization code you received in Step 2. | Yes |
| client\_id | string | The Client ID value generated in Step 1. | Yes |
| client\_secret | string | The Secret Key value generated in Step 1. See the [Best Practices Guide](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/secure-applications?context=linkedin/context) for ways to keep your `client_secret` value secure. | Yes |
| redirect\_uri | url | The same `redirect_uri` value that you passed in the previous step. | Yes |

#### Sample Request

* [https](#tabpanel_1_HTTPS1)
* [curl](#tabpanel_1_cURL1)

    POST  https://www.linkedin.com/oauth/v2/accessToken
     
    Content-Type: application/x-www-form-urlencoded
    grant_type=authorization_code
    code={authorization_code_from_step2_response}
    client_id={your_client_id}
    client_secret={your_client_secret}
    redirect_uri={your_callback_url}
    

    curl --location --request POST 'https://www.linkedin.com/oauth/v2/accessToken' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=authorization_code' \
    --data-urlencode 'code={authorization_code_from_step2_response}' \
    --data-urlencode 'client_id={your_client_id}' \
    --data-urlencode 'client_secret={your_client_secret}' \
    --data-urlencode 'redirect_uri={your_callback_url}'
    

#### Response

A successful access token request returns a [JSON](http://www.json.org/) object containing the following fields:

| Parameter | Type | Description |
| --- | --- | --- |
| access\_token | string | The access token for the application. This value must be kept secure as specified in the [API Terms of Use](https://www.linkedin.com/legal/l/api-terms-of-use). The length of access tokens is ~500 characters. We recommend that you plan for your application to handle tokens with length of at least 1000 characters to accommodate any future expansion plans. This applies to both access tokens and refresh tokens. |
| expires\_in | int | The number of seconds remaining until the token expires. Currently, all access tokens are issued with a 60-day lifespan. |
| refresh\_token | string | Your refresh token for the application. This token must be kept secure. |
| refresh\_token\_expires\_in | int | The number of seconds remaining until the refresh token expires. Refresh tokens usually have a longer lifespan than access tokens. |
| scope | string | URL-encoded, space-delimited list of member permissions your application has requested on behalf of the user. |

    {  
    "access_token":"AQUvlL_DYEzvT2wz1QJiEPeLioeA",
    "expires_in":5184000,
    "scope":"r_basicprofile"
    }
    

For more error details, refer to the [API Error Details](#oauthv2accesstoken) table.

Note

**Access Token Scopes and Lifetime**  
Access tokens stay valid until the number of seconds indicated in the `expires_in` field in the API response. You can go through the OAuth flow on multiple clients (browsers or devices) and simultaneously hold multiple valid access tokens if the same scope is requested. If you request a different scope than the previously granted scope, all the previous access tokens are invalidated.