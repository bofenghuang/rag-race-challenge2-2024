platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/hashtag-search


### Getting Media Tagged With A Hashtag

To get all of the photos and videos that have a specific hashtag, first use the `/ig_hashtag_search` endpoint and include the hashtag and ID of the Instagram Business or Creator Account making the query. For example, if the query is being made on behalf of the Instagram Business Account with the ID `17841405309211844`, you could get the ID for the "#coke" hashtag by performing the following query:

GET graph.facebook.com/ig\_hashtag\_search
  ?user\_id\=17841405309211844
  &q\=coke

This will return the ID for the “#Coke” hashtag node:

{
  "id" : "17873440459141021"
}

Now that you have the hashtag ID (`17873440459141021`), you can query its `/top_media` or `/recent_media` edge and include the Business Account ID to get a collection of media objects that have the “#coke” hashtag. For example:

GET graph.facebook.com/17873440459141021/recent\_media
  ?user\_id\=17841405309211844

This would return a response that looks like this:

{
  "data": \[
    {
      "id": "17880997618081620"
    },
    {
      "id": "17871527143187462"
    },
    {       
      "id": "17896450804038745"     
    }
  \]
}

[](#)

[](#)