platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user

User object

## User object

The User object contains Twitter User account metadata that describes the Twitter User referenced. Users can author Tweets, Retweet, quote other Users Tweets, reply to Tweets, follow Users, be @mentioned in Tweets and can be grouped into lists.

  

The Tweet object will also contain User objects of the Users involved within a Tweet.  In case of Retweets and Quoted Tweets, the top-level `user` object represents what account took that action, and the JSON payload will include a second `user` within the `retweeted_status` for the account that created the original Tweet.  User objects can be retireved using the `id` or `screen_name`.