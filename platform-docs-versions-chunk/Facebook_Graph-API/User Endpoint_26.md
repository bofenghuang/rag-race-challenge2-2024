platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/accounts/


### Parameters

| Parameter | Description |
| --- | --- |
| `about`<br><br>UTF-8 encoded string | Short description |
| `address`<br><br>UTF-8 encoded string | Address |
| `category_enum`<br><br>string | Page category (enum). See [Pages Categories API](https://developers.facebook.com/docs/graph-api/reference/page-category/) docs. |
| `category_list`<br><br>list<numeric string> | List of categories |
| `city_id`<br><br>city id | City ID |
| `coordinates`<br><br>JSON-encoded coordinate list | Coordinates |
| `cover_photo`<br><br>Object | Cover photo |
| `url`<br><br>URL | Required |
| `offset_y`<br><br>integer | Default value: `50` |
| `offset_x`<br><br>integer | Default value: `50` |
| `focus_y`<br><br>float |     |
| `focus_x`<br><br>float |     |
| `zoom_scale_x`<br><br>float |     |
| `zoom_scale_y`<br><br>float |     |
| `no_feed_story`<br><br>boolean | Default value: `false` |
| `no_notification`<br><br>boolean | Default value: `false` |
| `description`<br><br>UTF-8 encoded string | Description |
| `ignore_coordinate_warnings`<br><br>boolean | If ignore warnings generated in coordination validation (bool) |
| `location`<br><br>Object | This defines the location for this page. This is required if `location_page_id` is not specified, or if the Page referenced by the `location_page_id` doesn't have a valid value for the field. The dictionary must include the keys either `city_id` or all of `city`, `state`, and `country` (but `state` is optional if the address is not in the U.S.). |
| `city`<br><br>string |     |
| `state`<br><br>string |     |
| `country`<br><br>string |     |
| `name`<br><br>UTF-8 encoded string | Page name<br><br>Required |
| `phone`<br><br>UTF-8 encoded string | Phone |
| `picture`<br><br>URL | Profile picture |
| `website`<br><br>URL | Website |
| `zip`<br><br>string | Zipcode |