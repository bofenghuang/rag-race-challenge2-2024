platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-statuses


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since\_id, the since\_id will be forced to the oldest ID available. |     |     |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal to the specified ID. |     |     |
| count | optional | Specifies the number of results to retrieve per "page." |     |     |
| include\_entities | optional | Entities are ON by default in API 1.1, each tweet includes a node called "entities". This node offers a variety of metadata about the tweet in a discreet structure, including: user\_mentions, urls, and hashtags. You can omit entities from the result by using _include\_entities=false_ |     |     |
| include\_rts | optional | When set to either _true_ , _t_ or _1_ , the list timeline will contain native retweets (if they exist) in addition to the standard stream of tweets. The output format of retweeted tweets is identical to the representation you see in home\_timeline. |     |     |