platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/guides/dev-getting-started-engagement-api


### Authenticating with OAuth

OAuth is an authentication standard that is very common in the technology industry.  If you are already using OAuth (perhaps with other Twitter APIs) then you are likely using a language-specific OAuth package that abstracts away all the gnarly details. If you are new to OAuth, please visit our [Oauth with the Twitter API](https://developer.twitter.com/en/docs/basics/authentication/overview/oauth.html) page or head directly to the [https://oauth.net](https://oauth.net/) to learn more. Then we recommend that you find an OAuth package for your integration language of choice and start there. With these packages, the path to authenticating typically means configuring your keys and tokens, creating some sort of HTTP object, then making requests with that object.  

For example, in the Ruby world, the following pseudo-code represents a recipe to build an OAuth-enabled app using the Ruby gem ‘oauth’ and making a POST request:  

      `require 'oauth'  #Assemble JSON request (as above). request = make_json_request()   #Build an app consumer object with my app consumer key and secret. consumer = OAuth::Consumer.new(keys['consumer_key'], keys['consumer_secret'], {:site => ‘https://data-api.twitter.com’}) #Build a user token with tokens provided by account providing permission. If making app-only #request (checking Tweets that do not require permission with /totals endpoint), this step can be #skipped.  token = {:oauth_token => keys['access_token'], :oauth_token_secret => keys['access_token_secret']}  #Create oauth-enabled app object.  app = OAuth::AccessToken.from_hash(consumer, token) #Make POST request. result = app.post(“/insights/engagement/totals", request, {"content-type" => "application/json", "Accept-Encoding" => "gzip"})`
    

The Engagement API supports both application-only and user-context authentication. If you are collecting engagement metrics for unowned public Tweets with the /totals endpoint then no user permission is required and you can use application-only authentication. In this case, you’ll use only your app key and secret to authenticate.

OAuth also allows an app to make an API request “on behalf of another user”, using tokens that relate to the user. If you are generating Engagement metrics for owned Tweets, ie Tweets that were published by a user whom you have user tokens for, you will be making requests with a user context, meaning authenticating with both your app keys and user-specific access tokens. These user access tokens are typically supplied with the '[Sign-in with Twitter](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-for-websites/log-in-with-twitter/login-in-with-twitter)' process or acquired directly from the user (please note that you must use [twurl](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/using-twurl) if you acquire the tokens directly from the user). Once the user provides their tokens, they do not expire and can be used with the Engagement API to make requests on their behalf,  as long as the user doesn't reset their tokens or change their password, in which case they will have to provide you the new tokens.

You can review which metrics require which authentication via [this table](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/overview#EngagementTypes).