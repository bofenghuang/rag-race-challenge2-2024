platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/faq

###   
Error troubleshooting guide

**I am having problems authenticating**

Please make sure to review our [guidelines on authenticating](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Authentication) with the Engagement API.  
 

**I have passed the correct consumer key and secret, as well as access token and access token secret, but the following error is being returned. What can I do?**

    [
        Your account could not be authenticated. Reason: Unknown Authorization Type;
    ]

  
Make sure not to use any access tokens or secrets when you try and authenticate with the /totals endpoint. This is because if you do include these tokens, and are attempting to pull content from a Tweet not associated with these tokens, you will likely receive an error such as:

    [
        Forbidden to access tweets: 1054424731825229824;
    ]