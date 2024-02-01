platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

### Responses

**200**

Successful ad preview creation.

**400**

Invalid Pin parameters response

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/ad\_previews

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_previews

### Request samples

* Payload

Content type

application/json

Example

AdPreviewCreateFromImage

AdPreviewCreateFromImage

AdPreviewCreateFromPin

Copy

Expand all Collapse all

`{  * "image_url": "[https://somewebsite.com/someimage.jpg](https://somewebsite.com/someimage.jpg)",      * "title": "My Preview Image"       }`

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "url": "[https://ads.pinterest.com/ad-preview/58f1a0e9ab0bd0f99462a0e4c5dd7e8297888c8a36331e88f757abe8f0295d31/](https://ads.pinterest.com/ad-preview/58f1a0e9ab0bd0f99462a0e4c5dd7e8297888c8a36331e88f757abe8f0295d31/)"       }`