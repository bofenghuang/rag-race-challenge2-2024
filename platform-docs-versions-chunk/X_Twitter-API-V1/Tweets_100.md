platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline


# GET statuses/user\_timeline

**Important notice:** On June 19, 2019, we began enforcing a limit of 100,000 requests per day to the /statuses/user\_timeline endpoint, in addition to existing user-level and app-level rate limits. This limit is applied on a per-application basis, meaning that a single developer app can make up to 100,000 calls during any single 24-hour period.

Returns a collection of the most recent [Tweets](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object) posted by the [user](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) indicated by the `screen_name` or `user_id` parameters.

User timelines belonging to protected users may only be requested when the authenticated user either "owns" the timeline or is an approved follower of the owner.

The timeline returned is the equivalent of the one seen as a user's profile on Twitter.

This method can only return up to 3,200 of a user's most recent Tweets. Native retweets of other statuses by the user is included in this total, regardless of whether `include_rts` is set to `false` when requesting this resource.

See [Working with Timelines](https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines) for instructions on traversing timelines.

See [Embedded Timelines](https://developer.twitter.com/web/embedded-timelines), [Embedded Tweets](https://developer.twitter.com/web/embedded-tweets), and [GET statuses/oembed](https://developer.twitter.com/rest/reference/get/statuses/oembed) for tools to render Tweets according to [Display Requirements](https://about.twitter.com/company/display-requirements).