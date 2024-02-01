platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki


### [](#getting-started)Getting Started

Welcome to the CrowdTangle API! You can use the CrowdTangle API to access posts, the leaderboard and the link-checker. Please contact your CrowdTangle representative for access. If you have access to the API, you can locate your API token via your dashboard under Settings > API Access.

#### [](#authentication)Authentication

The CrowdTangle API expects the API token to be included either as a custom header with the name `x-api-token` or as a `token` query parameter.

    // as a custom header
    curl "https://api.crowdtangle.com/posts"
      -H "x-api-token: your-api-token"
    
    // as a query parameter 
    curl "https://api.crowdtangle.com/posts?token=your-api-token"
    

#### [](#making-a-request)Making a Request

All requests to the CrowdTangle API are made via GET to `https://api.crowdtangle.com/`. You must use https. Please visit the [API Cheat Sheet](https://help.crowdtangle.com/en/articles/3443476-api-cheat-sheet) to understand how pagination works with our API.

Below are the available endpoints:

##### [](#get-posts)[GET /posts](https://github.com/CrowdTangle/API/wiki/Posts)

##### [](#get-post)[GET /post](https://github.com/CrowdTangle/API/wiki/Posts#get-postid)

##### [](#get-postssearch)[GET /posts/search](https://github.com/CrowdTangle/API/wiki/Search)

##### [](#get-leaderboard)[GET /leaderboard](https://github.com/CrowdTangle/API/wiki/Leaderboard)

##### [](#get-links)[GET /links](https://github.com/CrowdTangle/API/wiki/Links)

##### [](#get-lists)[GET /lists](https://github.com/CrowdTangle/API/wiki/Lists)

##### [](#postman-template)Postman Template

[Postman](https://www.getpostman.com/) is a free API management software. [Click here to download a JSON file that you can import into Postman (unzip the file to access)](https://www.crowdtangle.com/assets/API-Demo.postman_collection.json.zip), and get a template for each endpoint. Please note that all parameters may not be present in the template; please view the Github API documentation to explore all parameter options.

Happy coding!