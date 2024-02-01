platform: Facebook
topic: Graph-API
subtopic: Canvas Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Canvas Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/canvas/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | ID of the canvas |
| `background_color`<br><br>string | Background color of the canvas |
| `body_elements`[](#)<br><br>list<CanvasPhoto\|CanvasHeader\|CanvasVideo\|CanvasText\|CanvasCarousel\|CanvasButton\|CanvasFooter\|CanvasStoreLocator\|CanvasProductList\|CanvasProductSet> | Body element nodes for the canvas |
| `business_id`<br><br>numeric string | The business id for the canvas product set element |
| `canvas_link`<br><br>string | The canvas link for the canvas |
| `collection_hero_image`<br><br>[Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) | First element as photo inside canvas to use as hero media for canvas collection |
| `collection_hero_video`<br><br>[Video](https://developers.facebook.com/docs/graph-api/reference/video/) | First element as video inside canvas to use as hero media for canvas collection |
| `collection_thumbnails`<br><br>list<CanvasCollectionThumbnail> | Canvas elements that can be used as thumbnails for canvas collections |
| `element_payload`<br><br>string | Payload that contains all element |
| `elements`<br><br>list<RichMediaElement> | Body element nodes for the canvas |
| `fb_body_elements`<br><br>list<CanvasPhoto\|CanvasHeader\|CanvasVideo\|CanvasText\|CanvasCarousel\|CanvasButton\|CanvasFooter\|CanvasStoreLocator\|CanvasProductList\|CanvasProductSet\|CanvasDynamicProductSet\|CanvasTemplateVideo\|CanvasDynamicPhoto> | Body element nodes for the canvas, used by FB internal apps and includes elements who's API is not public yet |
| `is_hidden`<br><br>bool | The canvas is hidden or not |
| `is_published`<br><br>bool | Publish status of the canvas |
| `last_editor`<br><br>[User](https://developers.facebook.com/docs/graph-api/reference/user/) | User who last edited this canvas |
| `linked_documents`<br><br>[list<Canvas>](https://developers.facebook.com/docs/graph-api/reference/canvas/) | The canvas documents that are reachable via buttons/links in this document |
| `name`<br><br>string | Name used to label the canvas<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `owner`<br><br>[Page](https://developers.facebook.com/docs/graph-api/reference/page/) | Page that owns this canvas |
| `property_list`<br><br>list<string> | List of properties for this canvas |
| `store_url`<br><br>string | The associated app store URL for the canvas |
| `style_list`<br><br>list<enum> | Canvas level style attributes |
| `tags`<br><br>list<string> | Tags associated with Canvas |
| `ui_property_list`<br><br>list<string> | List of UI properties to set when viewing this canvas from creation tools |
| `unused_body_elements`<br><br>list<CanvasPhoto\|CanvasHeader\|CanvasVideo\|CanvasText\|CanvasCarousel\|CanvasButton\|CanvasFooter\|CanvasStoreLocator\|CanvasProductList\|CanvasProductSet> | Body element nodes that belong to the canvas but are not used |
| `update_time`<br><br>int32 | Last updated time of the canvas |
| `use_retailer_item_ids`<br><br>bool | HACK: Flag for whether or not the ad creative that uses this Canvas should use retailer\_item\_ids or not |