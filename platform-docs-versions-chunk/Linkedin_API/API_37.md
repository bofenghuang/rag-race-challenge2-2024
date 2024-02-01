platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/programmatic-refresh-tokens?context=linkedin%2Fcontext


### Step 2: Exchanging a Refresh Token for a New Access Token

You can exchange the refresh token for a new access token by making the following HTTP POST request with a `Content-Type` header of `x-www-form-urlencoded` and the following parameters in the request body:

    https://www.linkedin.com/oauth/v2/accessToken
    

| Parameter | Description | Required |
| --- | --- | --- |
| grant\_type | The value of this field should always be refresh\_token. | Yes |
| refresh\_token | The refresh token from Step 1. | Yes |
| client\_id | The Client ID value generated when you registered your application. | Yes |
| client\_secret | The Client Secret value generated when you registered your application. | Yes |

#### Sample Request

    POST https://www.linkedin.com/oauth/v2/accessToken
    
    Content-Type: application/x-www-form-urlencoded
    grant_type=refresh_token&refresh_token=AQQOMeCIQMa6-zjU-02w8EJW67wPVk3hjJE5x1lZhU013LihKD8i1DpvaAl2jnuP8F1uXMgkm8nzjPfnaJR_kQNOxsLRLZWnAMzHMm81S0yQlkBYicw&client_id=861hhm46p48to2&client_secret=gPecS7yqHkyyShvR
    

A successful request returns a new access token with a new expiration time and the refresh token.

    {
      "access_token": "BBBB2kXITHELmWblJigbHEuoFdfRhOwGA0QNnumBI8XOVSs0HtOHEU-wvaKrkMLfxxaB1O4poRg2svCWWgwhebQhqrETYlLikJJMgRAvH1ostjXd3DP3BtwzCGeTQ7K9vvAqfQK5iG_eyS-q-y8WNt2SnZKZumGaeUw_zKqtgCQavfEVCddKHcHLaLPGVUvjCH_KW0DJIdUMXd90kWqwuw3UKH27ki5raFDPuMyQXLYxkqq4mYU-IUuZRwq1pcrYp1Vv-ltbA_svUxGt_xeWeSxKkmgivY_DlT3jQylL44q36ybGBSbaFn-UU7zzio4EmOzdmm2tlGwG7dDeivdPDsGbj5ig",
      "expires_in": 86400,
      "refresh_token": "AQWAft_WjYZKwuWXLC5hQlghgTam-tuT8CvFej9-XxGyqeER_7jTr8HmjiGjqil13i7gMFjyDxh1g7C_G1gyTZmfcD0Bo2oEHofNAkr_76mSk84sppsGbygwW-5oLsb_OH_EXADPIFo0kppznrK55VMIBv_d7SINunt-7DtXCRAv0YnET5KroQOlmAhc1_HwW68EZniFw1YnB2dgDSxCkXnrfHYq7h63w0hjFXmgrdxeeAuOHBHnFFYHOWWjI8sLenPy_EBrgYIitXsAkLUGvZXlCjAWl-W459feNjHZ0SIsyTVwzAQtl5lmw1ht08z5Du-RiQahQE0sv89eimHVg9VSNOaTvw",
      "refresh_token_expires_in": 439200,
      "scope":"r_basicprofile"
    }
    

#### API Error Details

| HTTP STATUS CODE | ERROR MESSAGE | ERROR DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- |
| 400 | invalid\_request "The provided authorization grant or refresh token is invalid, expired or revoked" | Invalid or expired or revoked refresh token is sent as part of the request. | Refresh Token expired or revoked or invalid, hence reauthenticate the member to generate the new refresh token. |
| 400 | invalid\_request "A required parameter "redirect\_uri" is missing" | Redirect\_URI in the request is missing. It is mandatory parameter. | Pass the Redirect\_URI in the request to route user back to correct landing page. |
| 400 | invalid\_request "A required parameter "grant\_type" is missing" | Grant type in the request is missing. It is mandatory parameter. | Add grant\_type as "refresh\_token" in the request. |
| 400 | invalid\_request "A required parameter "client\_id" is missing" | Client ID in the request is missing. It is mandatory parameter. | Pass the client id of the app in request. |
| 400 | invalid\_request "A required parameter "refresh\_token" is missing" | Refresh Token in the request is missing. It is mandatory parameter. | Pass the stored Refresh Token received as part of initial access token call. |