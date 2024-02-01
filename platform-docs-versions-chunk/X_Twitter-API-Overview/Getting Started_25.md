platform: X
topic: Twitter-API-Overview
subtopic: Getting Started
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Overview/Getting Started.md
url: https://developer.twitter.com/en/docs/twitter-api/getting-started/make-your-first-request


### Step 2. Choose a tool to make your request

While some requests can be straightforward, others can be tricky to build. That’s why the amazing community of developers have developed tools to abstract away some of the complexity. 

The following are some recommended tools and details on how to use them:

#### Postman

Postman is a visual tool that you can use to make requests to REST endpoints. We’ve created some great materials around Postman to help you get started with and explore the different endpoints available via the Twitter API. 

We recommend you read through our ["Getting started with Postman" tutorial](https://developer.twitter.com/en/docs/tutorials/postman-getting-started) to learn how to add your keys and tokens and make your first request. 

We’ve also produced a quick start guide for each of our Twitter API v2 endpoints, most of which use Postman. You can find these guides in each respective endpoint section, but here is a link to a few:

* Quick start: Post a Tweet
* Quick start: Search for Tweets
* Quick start: Lookup a user  
     

Please note that you can’t make requests to streaming endpoints using Postman. Please visit the [filtered stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/quick-start) or [1% ampled stream](https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/quick-start/sampled-stream) quick start guide to learn how to work with those endpoints.

If you prefer a more simple graphical tool, you should also consider using [Insomnia](https://insomnia.rest/).   
 

#### Sample code

If you are interested in using some simple code to make your request, we’ve put together sample code in multiple different languages for each of our Twitter API v2 endpoints. 

You can find the code samples via our Github repo, [Twitter-API-v2-sample-code](https://github.com/twitterdev/Twitter-API-v2-sample-code), which also contains a README file that you can use to learn how to set up your credentials to properly work with the requests. 

For example, here is a cURL example for the user lookup endpoint. All you have to do to use this request is replace the $ACCESS\_TOKEN and $USERNAME with your [App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) and Twitter handle. Then, copy and paste this code into your command line tool and press ‘Return’ or ‘Enter’.

      `curl "https://api.twitter.com/2/users/by/username/$USERNAME" -H "Authorization: Bearer $ACCESS_TOKEN"`
    

#### Libraries

The amazing TwitterDev community has also built libraries in a variety of different coding languages that can be used to make requests to the Twitter API.

We’ve built out a ["Tools and libraries" page](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) that lists all of the community libraries that we are aware of. Each library should have a ReadMe file that can be used to learn how to set up the repo on your machine and make your first request.

**Please note:** If you run into any problems, please read through our developer docs for the endpoint that you are making a request to, our [support section](https://developer.twitter.com/en/support), or reach out to the community on our forums for help. We’ll get you to a successful request!