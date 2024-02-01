platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate/enterprise-to-twitter-api-v2

### Similarities

#### Pagination

While v2 has additional pagination features (new pagination parameters that allow you to navigate using Tweet IDs with `since_id` and `until_id`), both enterprise and v2 allow you to paginate using time (`fromDate` and `toDate` with enterprise, and `start_time` and `end_time` for v2).  
 

#### Timezone

As noted in the pagination section, you can navigate different pages of data using time for both enterprise and v2. In both cases, you will be using UTC as the timezone when using these parameters.

**Support for Tweet edit history and metadata**

Both versions provide metadata that describes any edit history. Check out the [search API References](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference) and the [Tweet edits fundamentals page](https://developer.twitter.com/en/docs/twitter-api/tweet-edits) for more details.