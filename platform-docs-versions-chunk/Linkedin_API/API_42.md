platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/token-introspection?context=linkedin%2Fcontext&tabs=http


### API Details

    POST https://www.linkedin.com/oauth/v2/introspectToken
    
    Content-Type: application/x-www-form-urlencoded
    

#### Sample Request

* [http](#tabpanel_1_http)
* [curl](#tabpanel_1_curl)

    POST https://www.linkedin.com/oauth/v2/introspectToken
    

    curl --location --request POST 'https://www.linkedin.com/oauth/v2/introspectToken' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'client_id=<Application Client ID>' \
    --data-urlencode 'client_secret=<Application Client Secret>' \
    --data-urlencode 'token=<Token Value>'
    

#### Request Body

| Field | Type | Description |
| --- | --- | --- |
| client\_id | string | Required. Application client id |
| client\_secret | string | Required. Application client secret |
| token | string | Required. The string value of the token returned using [Client Credential Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow) (2-legged OAuth), [Authorization Code Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) (3-legged OAuth), or `Enterprise_User` (Enterprise OAuth Flow). |

#### Sample Response

    {
        "active": true,
        "client_id": "xxxxxxxx",
        "authorized_at": 1493055596,
        "created_at": 1493055596,
        "status": "active",
        "expires_at": 1497497620,
        "scope": "r_liteprofile,r_emailaddress,w_member_social",
        "auth_type": "_see note below_" 
    }
    

Note

Possible `auth-type` values returned are:  
"auth\_type": "2L"  
"auth\_type": "3L"  
"auth\_type": "Enterprise\_User"

#### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| active | boolean | Required. Boolean indicator of whether or not the returned token is currently active |
| status | string | Optional. An enum string with values:  <br>`revoked` - Token has been revoked  <br>`expired` - Token has expired due to the "expires\_at" TTL  <br>`active` - Token is active |
| scope | string | Optional. A string containing a comma-separated list of scopes associated with this token.  <br>Returned only for token obtained via [Authorization Code Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) (3-legged OAuth) |
| client\_id | string | Optional. Optional. Application Client ID |
| created\_at | long | Optional. Epoch time in seconds, indicating when this token was originally issued |
| expires\_at | long | Optional. Epoch time in seconds, indicating when this token will expire |
| authorized\_at | long | Optional. Epoch time in seconds, indicating when the token was authorized |
| auth\_type | string | Optional. String with values:  <br>`3L` - 3-legged member token  <br>`2L` - 2-legged application token  <br>`Enterprise_User` - Enterprise member token |

##### HTTP Response Status Codes

The response will vary depending on the status of the token and its authenticity.

| Status Code | Description |
| --- | --- |
| 200 | Success |
| 400 | Invalid `client id` or `token` |
| 401 | Invalid `client secret` |

Note

If the credentials are valid but do not match the client information in the token, you will receive a successful response (status 200 OK), however with `"active": false,` in the response body.