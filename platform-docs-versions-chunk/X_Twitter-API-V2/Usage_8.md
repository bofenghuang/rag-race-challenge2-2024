platform: X
topic: Twitter-API-V2
subtopic: Usage
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Usage.md
url: https://developer.twitter.com/en/docs/twitter-api/usage/tweets/api-reference/get-usage-tweets

### Example responses

* [Default Fields](#tab0)
* [Optional Fields](#tab1)

Default Fields

Optional Fields

      `{   "data": {     "cap_reset_day": 10,     "project_cap": "2000000",     "project_id": "1281043626347900822499",     "project_usage": "2007"   } }`
    

      `{   "data": {     "daily_client_app_usage": [       {         "usage": [           {             "date": "2023-11-01T00:00:00.000Z",             "usage": "200"           }         ],         "client_app_id": "101111140",         "usage_result_count": 1       }     ],     "project_cap": "2000000",     "daily_project_usage": {       "project_id": "1281043626347900822499",       "usage": [         {           "date": "2023-11-01T00:00:00.000Z",           "usage": "200"         }       ]     },     "project_usage": "200",     "cap_reset_day": 5,     "project_id": "1281043626347900822499"   } }`