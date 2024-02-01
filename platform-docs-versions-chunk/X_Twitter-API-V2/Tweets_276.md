platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules


### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `add`  <br> Required | array | Specifies the operation you want to perform on the rules. |
| `add.value`  <br> Required | string | The rule text. You can learn how to build a rule by following our guide on [how to build a rule](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule).  <br>  <br>If you have Essential access, you can use basic operators to build your rule, can add up to 5 rules to your stream concurrently, and each rule can be 512 characters long.  <br>  <br>If you have Elevated access, you can use basic operators, can add up to 25 rules to your stream, and each rule can be 512 characters long  <br>  <br>If you have Academic Research access, you can use all operators, can add up to 1000 rules to your stream, and each rule can be 1024 characters long.  <br>  <br>To learn more about Twitter API access levels, please visit our [about Twitter API page](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level). |
| `delete`  <br> Required | object | Specifies the operation you want to perform on the rules. |
| `delete.ids`  <br> Required | array | Array of rule IDs, each one representing a rule already active in your stream. IDs must be submitted as strings. You can find a rule ID by using the [GET /tweets/search/stream/rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream-rules) endpoint. |
| `add.tag`  <br> Optional | string | The tag label. This is a free-form text you can use to identify the rules that matched a specific Tweet in the streaming response. Tags can be the same across rules.  <br>  <br>Learn more about tags from our [matching returned Tweets guide](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/matching-returned-tweets). |