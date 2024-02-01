platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/media


### Request Syntax

#### Image Containers

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
  ?image\_url={image-url}
  &is\_carousel\_item={is-carousel-item}
  &caption={caption}
  &location\_id={location-id}
  &user\_tags={user-tags}
  &product\_tags={product-tags}
  &access\_token={access-token}

#### Reel Containers

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
?media\_type=REELS
&video\_url={reel-url}
&caption={caption}
&share\_to\_feed={share-to-feed}
&collaborators={collaborator-usernames}
&cover\_url={cover-url}
&audio\_name={audio-name}
&user\_tags={user-tags}
&location\_id={location-id}
&thumb\_offset={thumb-offset}
&share\_to\_feed={share-to-feed}
&access\_token={access-token}

#### Carousel Containers

Carousel containers only. To create carousel item containers, create image or video containers instead (reels are not supported). See [Carousel Posts](https://developers.facebook.com/docs/instagram-api/guides/content-publishing#carousel-posts) for complete publishing steps.

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
?media\_type=CAROUSEL
&caption={caption}
&share\_to\_feed={share-to-feed}
&collaborators={collaborator-usernames}
&location\_id={location-id}
&product\_tags={product-tags}
&children={children}
&access\_token={access-token}