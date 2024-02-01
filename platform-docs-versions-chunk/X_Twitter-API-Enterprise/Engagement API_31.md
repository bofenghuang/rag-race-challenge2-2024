platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/faq


### Engagement API

**How can I access the Engagement API?**

Access to the Engagement API is provisioned through an enterprise subscription.  Please fill out [this form](https://developer.twitter.com/content/developer-twitter/en/enterprise-application) to get in touch with our sales team.  
 

**How is my usage tracked by '@handle'?**

If your contract includes a limit for the number of unique handles that can be used with Engagement API.  The internal Twitter system will keep track of the number of Authenticated users owning Tweets that are queried with the Engagement API.  Customers should also keep track of this unique number on the client side.  Currently, there is no usage API or UI to check the @handle usage for the Engagement API.  The system will not block overages if there are more @handles requested than what is contracted.  At the end of the billing month, the number of unique @handles queried is compared to the contracted amount and an overage will be charged in accordance with the contract terms.

**Can I check my @handle usage for Engagement API?**

Currently, there is no usage API or UI to check the @handle usage for the Engagement API.  The system will not block overages if there are more @handles requested than what is contracted.  At the end of the billing month, the number of unique @handles queried is compared to the contracted amount and an overage will be charged in accordance with the contract terms.

**The `engagements` metadata field returned in the payload is not equal to the sum of all the various engagement metric totals. Why is this the case?**

This is to be expected. The `engagements` metadata field may not always correlate with the sum of all individual engagement metrics returned by the API. This is because the `engagements` metadata field may include additional engagements that do not have specific metrics broken out in the payload. Said another way, adding all of the various engagement metric totals together may not equal the value you are seeing in the `engagements` metric field that is returned to you in the payload.

You can think of the `engagements` metadata field as any click or interaction made on the Tweet.  
 

**The `url_clicks` field in the payload response is returning a number, when in fact the Tweet does not have a URL. How is this possible?**

This may be because a Tweet that contains something like a hashtag (that creates a link to another page) will count as a URL click if it is clicked on by a user.  
 

**Why can I not receive engagement data for a specific Tweet?**

There are various reasons why you might not be able to retrieve engagement data for a specific Tweet, including:

* The Tweet ID or IDs you have requested are not available based on the authentication token you are using to retrieve data on behalf of a third party.
* The Tweet ID or IDs you have requested specific to the /totals endpoint are not 90 days or newer and are thus not available for returning the impressions or engagement metrics.
* The Tweet ID or IDs you have requested are no longer available, usually indicating that they have been deleted or are no longer publicly available for another reason.

Please review the different [error messages](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#ErrorMessages) that you will likely receive in any of the above cases.  
 

**How can I handle rate limiting with the Engagement API?**

You can use the `x-per-minute-limit` and `x-per-minute-remaining` information returned by the response header when you make a request to the Engagement API to monitor your consumption.  
  
`x-per-minute-limit` tells you what your allowance is and `x-per-minute-remaining` tells you how many calls you have left.