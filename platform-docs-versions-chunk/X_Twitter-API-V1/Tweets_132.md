platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/basic-stream-parameters


### track

A comma-separated list of phrases which will be used to determine what Tweets will be delivered on the stream. A phrase may be one or more terms separated by spaces, and a phrase will match if all of the terms in the phrase are present in the Tweet, regardless of order and ignoring case. By this model, you can think of commas as logical ORs, while spaces are equivalent to logical ANDs (e.g. ‘the twitter’ is the AND twitter, and ‘the,twitter’ is the OR twitter).

The text of the Tweet and some entity fields are considered for matches. Specifically, the text attribute of the Tweet, expanded\_url and display\_url for links and media, text for hashtags, and screen\_name for user mentions are checked for matches.

Each phrase must be between 1 and 60 bytes, inclusive.

Exact matching of phrases (equivalent to quoted phrases in most search engines) is not supported.

Punctuation and special characters will be considered part of the term they are adjacent to. In this sense, “hello.” is a different track term than “hello”. However, matches will ignore punctuation present in the Tweet. So “hello” will match both “hello world” and “my brother says hello.” Note that punctuation is not considered to be part of a #hashtag or @mention, so a track term containing punctuation will not match either #hashtags or @mentions.

UTF-8 characters will match exactly, even in cases where an “equivalent” ASCII character exists. For example, “touché” will not match a Tweet containing “touche”.

Non-space separated languages, such as CJK are currently unsupported.

URLs are considered words for the purposes of matches which means that the entire domain and path must be included in the track query for a Tweet containing an URL to match. Note that display\_url does not contain a protocol, so this is not required to perform a match.

Twitter currently canonicalizes the domain “www.example.com” to “example.com” before the match is performed, so omit the “www” from URL track terms.

Finally, to address a common use case where you may want to track all mentions of a particular domain name (i.e., regardless of subdomain or path), you should use “example com” as the track parameter for “example.com” (notice the lack of period between “example” and “com” in the track parameter). This will be over-inclusive, so make sure to do additional pattern-matching in your code. See the table below for more examples related to this issue.

Track examples:

|     |     |     |
| --- | --- | --- |
| Parameter value | Will match... | Will not match... |
| Twitter | TWITTERtwitter “Twitter” twitter. #twitter @twitter [http://twitter.com](http://twitter.com/) | TwitterTracker#newtwitter |
| Twitter’s | I like Twitter’s new design | Someday I’d like to visit @Twitter’s office |
| twitter api,twitter streaming | The Twitter API is awesomeThe twitter streaming service is fast Twitter has a streaming API | I’m new to Twitter |
| example.com | Someday I will visit example.com | There is no example.com/foobarbaz |
| example.com/foobarbaz | example.com/foobarbazwww.example.com/foobarbaz | example.com |
| www.example.com/foobarbaz |     | www.example.com/foobarbaz |
| example com | example.comwww.example.com foo.example.com foo.example.com/bar I hope my startup isn’t merely another example of a dot com boom! |     |