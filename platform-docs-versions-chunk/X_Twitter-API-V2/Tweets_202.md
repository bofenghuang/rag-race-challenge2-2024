platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/migrate/enterprise-to-twitter-api-v2


### Similarities

#### Granularity

While the parameter for selecting granularity of the returned data is different (`bucket` for the enterprise version, `granularity` for the v2 version), the values that you can pass with that parameter are the same, as well as the default behavior:

* `day`
* `hour` (default)
* `minute`

####   
Pagination

While v2 has additional pagination features (new pagination parameters that allow you to navigate using Tweet IDs with `since_id` and `until_id`), both enterprise and v2 allow you to paginate using time (`fromDate` and `toDate` with enterprise, and `start_time` and `end_time` for v2).

If you are using the enterprise version, you will use the `next` parameter to paginate, the next token field will be called `next`, and it will be located at the root in the response.

If you are using v2, you can use either the `next_token` or `pagination_token` parameter to paginate, and your next token will be located at `meta.next_token` in the response.  
 

#### Timezone

As noted in the pagination section, you can navigate different pages of data using time for both enterprise and v2. In both cases, you will be using UTC as the timezone when using these parameters.