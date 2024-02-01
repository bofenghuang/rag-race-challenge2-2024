platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/business-discovery


### Getting an Account's Follower & Media Count

This sample query shows how to get the number of followers and number of published media objects on the [Blue Bottle Coffee](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fbluebottle%2F&h=AT0BNjG7hU5gOy-Tzgy0td9fc3lz87NbqE4gcwOgWCDwj4VwzmJLV5_AhO4tlfO6r6qWTLmvVG3C9tnpT6MdwGvZ55JJGrXums4vrtLU9NKrGM4qaOOAb2oSdh0TaUQYTrflmQq_g3NUyq2kVyekFQ) Instagram Business Account. Notice that business discovery queries are performed on the Instagram Business or Creator Account's ID (in this case, `17841405309211844`), not the username of the Instagram Business or Creator Account that you are attempting to get data about (`bluebottle` in this example).

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/v3.2/17841405309211844?fields=business\_discovery.username(bluebottle){followers\_count,media\_count}&access\_token={access-token}"

#### Sample Response

{
  "business\_discovery": {
    "followers\_count": 267793,
    "media\_count": 1205,
    "id": "17841401441775531" // Blue Bottle's Instagram Account ID
  },
  "id": "17841405309211844"  // ID of the Instagram account performing the query
}