platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/programmatic-refresh-tokens?context=linkedin%2Fcontext


### Step 1: Getting a Refresh Token

Use the [Authorization Code Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin/context) to get both a refresh token and access token. If your application is authorized for programmatic refresh tokens, the following fields are returned when you exchange the authorization code for an access token:

* `refresh_token` — Your refresh token for the application. This token must be kept secure.
* `refresh_token_expires_in` — The number of seconds remaining until the refresh token expires. Refresh tokens usually have a longer lifespan than access tokens.
* `scope` — URL-encoded, space-delimited list of member permissions your application has requested on behalf of the user.|

#### Sample Response

    {
      "access_token": "AQXNnd2kXITHELmWblJigbHEuoFdfRhOwGA0QNnumBI8XOVSs0HtOHEU-wvaKrkMLfxxaB1O4poRg2svCWWgwhebQhqrETYlLikJJMgRAvH1ostjXd3DP3BtwzCGeTQ7K9vvAqfQK5iG_eyS-q-y8WNt2SnZKZumGaeUw_zKqtgCQavfEVCddKHcHLaLPGVUvjCH_KW0DJIdUMXd90kWqwuw3UKH27ki5raFDPuMyQXLYxkqq4mYU-IUuZRwq1pcrYp1Vv-ltbA_svUxGt_xeWeSxKkmgivY_DlT3jQylL44q36ybGBSbaFn-UU7zzio4EmOzdmm2tlGwG7dDeivdPDsGbj5ig",
      "expires_in": 86400,
      "refresh_token": "AQWAft_WjYZKwuWXLC5hQlghgTam-tuT8CvFej9-XxGyqeER_7jTr8HmjiGjqil13i7gMFjyDxh1g7C_G1gyTZmfcD0Bo2oEHofNAkr_76mSk84sppsGbygwW-5oLsb_OH_EXADPIFo0kppznrK55VMIBv_d7SINunt-7DtXCRAv0YnET5KroQOlmAhc1_HwW68EZniFw1YnB2dgDSxCkXnrfHYq7h63w0hjFXmgrdxeeAuOHBHnFFYHOWWjI8sLLenPy_EBrgYIitXsAkLUGvZXlCjAWl-W459feNjHZ0SIsyTVwzAQtl5lmw1ht08z5Du-RiQahQE0sv89eimHVg9VSNOaTvw",
      "refresh_token_expires_in": 525600,
      "scope":"r_basicprofile"
    
    }
    

Note

Refresh tokens are approximately 500 characters long. We recommend that your application stack be made to handle tokens of at least 1000 characters to accommodate future expansion plans. This applies to access tokens as well as refresh tokens.