platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-subscribers-show


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_. |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_. |     |     |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| user\_id | required | The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name. |     |     |
| screen\_name | required | The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID. |     |     |
| include\_entities | optional | When set to either _true_, _t_ or _1_, each Tweet will include a node called "entities". This node offers a variety of metadata about the tweet in a discreet structure, including: user\_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See [Tweet Entities](https://developer.twitter.com/overview/api/tweets) for more details. |     |     |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user objects. |     |     |