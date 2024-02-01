platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet


## Tweet Object

Tweets are the basic atomic building block of all things Twitter. Tweets are also known as “status updates.” The Tweet object has a long list of ‘root-level’ attributes, including fundamental attributes such as `id`, `created_at`, and `text`. Tweet objects are also the ‘parent’ object to several child objects. Tweet child objects include `user`, `entities`, and `extended_entities`. Tweets that are geo-tagged will have a `place` child object.

When the following Tweet is rendered in JSON:

> 1/ To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm
> 
> — TwitterAPI (@TwitterAPI) [Oct 10, 2018](https://twitter.com/TwitterDev/status/1050118621198921728)

The JSON will be a mix of ‘root-level’ attributes (here we are highlighting some of the most fundamental attributes), and child objects (which are represented here with the `{}` notation):

{
 "created\_at": "Wed Oct 10 20:19:24 +0000 2018",
 "id": 1050118621198921728,
 "id\_str": "1050118621198921728",
 "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
 "user": {},  
 "entities": {}
}