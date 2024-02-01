platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/collaborators

# Collaborators

Represents a list of users who are added as collaborators on an IG Media object.

## Creating

This operation is not supported.

## Reading

Get a list of Instagram users as collaborators and their invitation status on an IG Media object.

**`GET /{ig-media-id}`**

### Limitations

* Up to 3 Instagram accounts can be added as collaborators
* Only IG users who have enabled collaborator tagging will be returned in the response
* Collaborators tagging supports Feed image, Reels and Carousel, Stories is not supported