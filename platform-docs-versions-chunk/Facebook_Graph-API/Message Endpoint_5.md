platform: Facebook
topic: Graph-API
subtopic: Message Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Message Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/message


### Fields

If a field has no data, it will not be returned in the JSON response.

NameDescription

`attachments.data`

_array_

`file_url`

`generic_template`

`id`

`image_data`

`name`

`video_data`

Media, such as an image, video, or file CDN URL, attached to the message.

  

The URL for the file attached to the message

The URL for the image attached to the message. Can include the following key:value pairs:

|     |     |
| --- | --- |
| * `cta`: object with `title`, `type`, `url`<br>* `medial_url`: string, URL for the image | * `subtitle`: string, in pixels<br>* `title`: string, |

The ID for the attachment

The URL for the image attached to the message. Can include the following key:value pairs:

|     |     |
| --- | --- |
| * `animated_gif_preview_url`: string, URL for preview for the GIF<br>* `animated_gif_url`: string, URL for the GIF<br>* `height`: int, in pixels<br>* `max_height`: int, in pixels<br>* `max_width`: int, in pixels | * `preview_url`: string, Preview for the URL<br>* `render_as_sticker`: bool, true or false<br>* `url`: string, URL for the image<br>* `width`: int, in pixels |

The name for the attachement

The URL for the video attached to the message

`created_time`

_datetime_

The time the message was created

`from`

_object_

`id`

`email`

`name`

`username`

Information about who sent the message. Can be a person, Page, or Instagram Professional account

The ID can be an Instagram-scoped ID or Page-scoped ID for a person or Page ID or Instagram Professional account ID for your business.

The email for a person or Facebook Page. _Page messaging only_

The name for a person or Facebook Page. _Page messaging only_

The username for a person on Instagram or your Instagram Professional account. _Instagram Messaging only_

"from": {
    "username": "INSTAGRAM-USERNAME",
    "id": "ID"
  }

`id`

_string_

The ID for a message

`is_unsupported`

_boolean_

Only returned when `true`; a message contains unsupported content.

`message`

_string_

Text content for the message. If no text is part of the message, this will be empty.

`reactions`

_array_

`data` _array_

`reaction` _emoji_

`users` _array of objects_

`id`

  

`username`

The types of reactions the message has received with a list of all the people who reacted with that reaction type.

An array of reaction objects

The reaction emoji type

A list of people who have reacted to the message

  

The ID can be an Instagram-scoped ID for a person on Instagram or Instagram Professional account ID for your business.

The username for a person on Instagram or your Instagram Professional account. _Instagram Messaging only_

"reactions":
  {
    "reaction": "❤️",
    "users" : \[
      {
        "username": "INSTAGRAM-USERNAME",
        "id": "ID", 
      },
    \]
  }

`shares`

_array_

Media shares, such as a post or product template, included in the message. Please note, for the shares object you need to request the sub-fields also in order to retrieve the data.

"shares": {
  "data": \[{
    "template": {
      "payload":{
        "product": {
           "elements":{     //Can contain multiple products if applicable
             "data": \[
              {
                "id" : "PRODUCT-ID",    // 0 if business can't see this product
                "retailer\_id": "ID-ASSIGNED-BY-THE-RETAILER", 
                "image\_url" : "IMAGE-URL", 
                "name" : "PRODUCT-NAME",
                "price" : "$10"
              },
            \],
          }
        }
      }
    }
  }\]
}   

`story`

_array_

The link and ID for a story. Only mentions and replyies are supported.

StoryReply: 
{
    "link": "CDN-URL",
    "id": "STORY-ID"
}

StoryMention: 
{
    "link": "CDN-URL",
    "id": "STORY-ID"
}

`tags`

_object_

A `data` array containing names for tags indicating the message folder and source of the message.

* For Facebook Pages, `name` can be `inbox`, `read`, `source:chat`,

`to`

_object_

`data` _array_

`id`

`email`

`name`

`username`

Information about who received the message

  
  

The ID can be an Instagram-scoped ID or Page-scoped ID for a person or Page ID or Instagram Professional account ID for your business.

The email for a person or Facebook Page. _Page messaging only_

The name for a person or Facebook Page. _Page messaging only_

The username for a person on Instagram or your Instagram Professional account. _Instagram Messaging only_

"to": {
  "data": \[
    { 
      "username": "INSTAGRAM-USERNAME", 
      "id": "ID" 
    }
  \]
}