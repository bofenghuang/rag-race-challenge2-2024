platform: X
topic: Twitter-API-V2
subtopic: Usage
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Usage.md
url: https://developer.twitter.com/en/docs/twitter-api/usage/tweets/introduction


### Getting started

To use this endpoint, you need a [bearer token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) from the [developer portal](https://developer.twitter.com/en/portal/dashboard). Once you have the bearer token,  you can call the usage API as shown below:

      `curl 'https://api.twitter.com/2/usage/tweets' --header 'Authorization: Bearer XXXXX'`
    

If the request is successful, you should see the JSON response as shown below:

      `{     "data": {         "cap_reset_day": 10,         "project_cap": "5000000000",         "project_id": "1369785403853424",         "project_usage": "43435"     } }`
    

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)