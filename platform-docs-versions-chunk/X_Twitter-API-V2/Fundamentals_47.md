platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/expansions


## Overview

With expansions, developers can expand objects referenced in the payload. Objects available for expansion are referenced by ID. For example, the `referenced_tweets.id` and `author_id` fields returned in the [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html) payload can be expanded into complete objects. If you would like to request fields related to the user that posted that Tweet, or the media, poll, or place that was included in that Tweet, you will need to pass the related expansion query parameter in your request to receive that data in your response. Currently, v2 endpoints that return Tweets, Users, Lists, Spaces, and Direct Message event objects all support expansions (see examples below). 

When including an expansion in your request, we will include that expanded object’s default fields within the same response. It helps return additional data in the same response without the need for separate requests. If you would like to request additional [fields](https://developer.twitter.com/en/docs/twitter-api/fields.html) related to the expanded object, you can include the field parameter associated with that expanded object, along with a comma-separated list of fields that you would like to receive in your response. Please note fields are not always returned in the same order they were requested in the query.

The Tweet payload below contains reference IDs for complementary objects we can expand on, including the author\_id of who posted the Tweet, the id of a _referenced_ Tweet, and a media\_key for a media attachment. 

      `{     "data": {         "attachments": {             "media_keys": [                 "16_1211797899316740096"             ]         },         "author_id": "2244994945",         "id": "1212092628029698048",         "referenced_tweets": [             {                 "type": "replied_to",                 "id": "1212092627178287104"             }         ],         "text": "We believe the best future version of our API will come from building it with YOU. Here’s to another great year with everyone who builds on the Twitter platform. We can’t wait to continue working with you in the new year. https://t.co/yvxdK6aOo2"     } }`
    

We can expand on `attachments.media_keys` to view the media object, `author_id` to view the user object, and `referenced_tweets.id` to view the Tweet object the originally requested Tweet was referencing. Expanded objects will be nested in the `"includes"` object, as can be seen in the sample response below.