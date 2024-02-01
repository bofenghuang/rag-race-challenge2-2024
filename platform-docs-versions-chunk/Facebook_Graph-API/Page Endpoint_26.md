platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/


### Parameters

| Parameter | Description |
| --- | --- |
| `about`<br><br>UTF-8 string | Update the `about` field. Note that this value is mapped to the **Description** setting in the **Edit Page Info** user interface.<br><br>Supports Emoji |
| `accept_crossposting_handshake`<br><br>array<JSON object> | Accepts a pending crossposting request initiated by another Page |
| `partner_page_id`<br><br>page ID | partner\_page\_id<br><br>Required |
| `allow_live`<br><br>boolean | allow\_live<br><br>Required |
| `allow_spherical_photo`<br><br>boolean | Default value: `false`<br><br>Indicates that we should allow this photo to be treated as a spherical photo. This param will only be used when uploading a new image file. This will not change the behavior unless the server is able to interpret the photo as spherical, such as via Photosphere XMP metadata. Regular non-spherical photos will still be treated as regular photos even if this parameter is true. |
| `attire`[](#)<br><br>enum{Unspecified, Casual, Dressy} | Update the `attire` field |
| `begin_crossposting_handshake`<br><br>array<JSON object> | Begins the video crossposting handshake with another page |
| `partner_page_id`<br><br>page ID | partner\_page\_id<br><br>Required |
| `allow_live`<br><br>boolean | allow\_live<br><br>Required |
| `bio`<br><br>string | Update the `bio` field |
| `category_list`<br><br>list<numeric string> | Update the `category_list` field |
| `company_overview`<br><br>string | Update the `company_overview` field |
| `contact_address`[](#)<br><br>Object | Update the `contact_address` field |
| `city_id`<br><br>city id |     |
| `street1`<br><br>string |     |
| `street2`<br><br>string |     |
| `zip`<br><br>string |     |
| `cover`<br><br>numeric string or integer | Update the `cover` field. This field can only be updated by the Page Admin or Page Editor with `EDIT_PROFILE` and [`business_management` permissions](https://developers.facebook.com/docs/apps/review/login-permissions#business-management). |
| `culinary_team`[](#)<br><br>string | Update the `culinary_team` field |
| `delivery_and_pickup_option_info`<br><br>array<string> | delivery\_and\_pickup\_option\_info. Each String represent the url link to a delivery and pick up option webpage. The API filters out duplicated urls as well as invalidated urls. If empty array is input, `delivery_and_pickup_option_info` field of the page will be cleared. |
| `description`<br><br>string | Update the `description` field. Note that this value is mapped to the **Additional Information** setting in the **Edit Page Info** user interface. |
| `differently_open_offerings`<br><br>JSON object {enum {ONLINE\_SERVICES, DELIVERY, PICKUP, OTHER} : boolean} | Indication of services currently offered by this business. Specify "true" for all that apply. Intended to be used when `temporary_status` = 'differently\_open'.<br><br>Note to restaurants: See `restaurant_services` for how to indicate longer term or permanent aspects of your business. |
| `directed_by`[](#)<br><br>string | Update the `directed_by` field |
| `displayed_message_response_time`[](#)<br><br>string | Page estimated message response time displayed to user |
| `emails`[](#)<br><br>list<string> | Update the `emails` field |
| `focus_x`<br><br>float | Cover photo focus x |
| `focus_y`<br><br>float | Cover photo focus y |
| `food_styles`[](#)<br><br>list<enum{Afghani, American (New), American (Traditional), Asian fusion, Barbeque, Brazilian, Breakfast, British, Brunch, Buffets, Burgers, Burmese, Cajun/Creole, Caribbean, Chinese, Creperies, Cuban, Delis, Diners, Ethiopian, Fast food, Filipino, Fondue, Food stands, French, German, Greek and Mediterranean, Hawaiian, Himalayan/Nepalese, Hot dogs, Indian/Pakistani, Irish, Italian, Japanese, Korean, Latin American, Mexican, Middle Eastern, Moroccan, Pizza, Russian, Sandwiches, Seafood, Singaporean, Soul food, Southern, Spanish/Basque, Steakhouses, Sushi bars, Taiwanese, Tapas bars, Tex-Mex, Thai, Turkish, Vegan, Vegetarian, Vietnamese}> | Update the `food_styles` field |
| `general_info`<br><br>string | Update the `general_info` field |
| `general_manager`[](#)<br><br>string | Update the `general_manager` field |
| `genre`[](#)<br><br>string | Update the `genre` field |
| `hours`<br><br>dictionary { string : <> } | Update the `hours` field |
| `ignore_coordinate_warnings`<br><br>boolean | Ignore coordinate warnings when updating this Page's location |
| `impressum`[](#)<br><br>string | Update the `impressum` field |
| `is_always_open`[](#)<br><br>boolean | Is this location always open? |
| `is_permanently_closed`<br><br>boolean | Update the `is_permanently_closed` field |
| `is_published`[](#)<br><br>boolean | Update the `is_published` field |
| `is_webhooks_subscribed`[](#)<br><br>boolean | Is the application subscribed for real time updates from this page? |
| `location`<br><br>Object | Update the `location` field |
| `city`<br><br>string |     |
| `city_id`<br><br>city id |     |
| `state`[](#)<br><br>string |     |
| `country`[](#)<br><br>string |     |
| `street`<br><br>string |     |
| `zip`<br><br>string |     |
| `latitude`[](#)<br><br>float |     |
| `longitude`[](#)<br><br>float |     |
| `mission`<br><br>string | Update the `mission` field |
| `no_feed_story`<br><br>boolean | Default value: `false`<br><br>Don't generate a feed story for the cover photo |
| `no_notification`<br><br>boolean | Default value: `false`<br><br>Don't generate a notification for the cover photo |
| `offset_x`<br><br>integer | Default value: `50`<br><br>Cover photo offset x |
| `offset_y`<br><br>integer | Default value: `50`<br><br>Cover photo offset y |
| `parking`<br><br>dictionary { enum{street, lot, valet} : <boolean> } | Update the `parking` field |
| `payment_options`[](#)<br><br>dictionary { enum{visa, amex, mastercard, discover, cash\_only} : <boolean> } | Update the `payment_options` field |
| `phone`<br><br>string | Update the `phone` field |
| `pickup_options`<br><br>array<enum {CURBSIDE, IN\_STORE, OTHER}> | List of pickup option types available at this Page's business location |
| `plot_outline`[](#)<br><br>string | Update the `plot_outline` field |
| `price_range`[](#)<br><br>string | Update the `price_range` field |
| `public_transit`[](#)<br><br>string | Update the `public_transit` field |
| `restaurant_services`[](#)<br><br>dictionary { enum{reserve, walkins, groups, kids, takeout, delivery, catering, waiter, outdoor} : <boolean> } | Update the `restaurant_services` field |
| `restaurant_specialties`[](#)<br><br>dictionary { enum{breakfast, lunch, dinner, coffee, drinks} : <boolean> } | Update the `restaurant_specialties` field |
| `scrape`<br><br>boolean | Re-scrape the website associated with this Page |
| `spherical_metadata`<br><br>JSON object | A set of params describing an uploaded spherical photo. This param will only be used when uploading a new image file. This field is not required; if it is not present we will try to generate spherical metadata from the metadata embedded in the image. If it is present, it takes precedence over any embedded metadata. Please click to the left to expand this list and see more information on each parameter. See also the Google Photo Sphere spec for more info on the meaning of the params: https://developers.google.com/streetview/spherical-metadata |
| `ProjectionType`<br><br>string | Accepted values include equirectangular (full spherical photo), cylindrical (panorama), and cubestrip (also known as cubemap, e.g. for synthetic or rendered content; stacked vertically with 6 faces).<br><br>Required |
| `CroppedAreaImageWidthPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: Very similar to equirectangular. This value should be equal to the actual width of the image, and together with FullPanoWidthPixels, it describes the horizontal FOV of content of the image: HorizontalFOV = 360 \* CroppedAreaImageWidthPixels / FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This has no relationship to the pixel dimensions of the image. It is simply a representation of the horizontal FOV of the content of the image. HorizontalFOV = CroppedAreaImageWidthPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>Required |
| `CroppedAreaImageHeightPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value will NOT be equal to the actual height of the image. Instead, together with FullPanoHeightPixels, it describes the vertical FOV of the image: VerticalFOV = 180 \* CroppedAreaImageHeightPixels / FullPanoHeightPixels. In other words, this value is equal to the CroppedAreaImageHeightPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This has no relationship to the pixel dimensions of the image. It is simply a representation of the vertical FOV of the content of the image. VerticalFOV = CroppedAreaImageHeightPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>Required |
| `FullPanoWidthPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: Very similar to equirectangular. This value defines a ratio of horizontal pixels to degrees in the space of the image, and in general the pixel to degree ratio in the scope of the metadata object. Concretely, PixelsPerDegree = FullPanoWidthPixels / 360. This is also equivalent to the circumference of the cylinder used to model this projection.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It only defines the pixel to degree ratio in the scope of the metadata object. It represents the number of pixels in 360 degrees, so pixels per degree is then given by: PixelsPerDegree = FullPanoWidthPixels / 360. As an example, if FullPanoWidthPixels were chosen to be 3600, we would have PixelsPerDegree = 3600 / 360 = 10. An image with a vertical field of view of 65 degrees would then have a CroppedAreaImageHeightPixels value of 65 \* 10 = 650.<br><br>Required |
| `FullPanoHeightPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the FullPanoHeightPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is always equal to FullPanoWidthPixels / 2.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is a second, redundant representation of PixelsPerDegree. FullPanoHeightPixels = 180 \* PixelsPerDegree. It must be consistent with FullPanoWidthPixels: FullPanoHeightPixels = FullPanoWidthPixels / 2.<br><br>Required |
| `CroppedAreaLeftPixels`<br><br>int64 | Default value: `0`<br><br>\--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the CroppedAreaLeftPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. Concretely, AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels. |
| `CroppedAreaTopPixels`<br><br>int64 | Default value: `0`<br><br>\--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the CroppedAreaTopPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. Concretely, AngularOffsetFromTopDegrees = CroppedAreaTopPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. AngularOffsetFromTopDegrees = CroppedAreaTopPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels. |
| `PoseHeadingDegrees`<br><br>float |     |
| `PosePitchDegrees`<br><br>float |     |
| `PoseRollDegrees`<br><br>float |     |
| `InitialViewHeadingDegrees`<br><br>float |     |
| `InitialViewPitchDegrees`<br><br>float |     |
| `InitialViewRollDegrees`<br><br>float | This is not currently supported |
| `InitialViewVerticalFOVDegrees`<br><br>float | This is deprecated. Please use InitialVerticalFOVDegrees. |
| `InitialVerticalFOVDegrees`<br><br>float | You can set the intial vertical FOV of the image. You can set either this field or InitialHorizontalFOVDegrees. |
| `InitialHorizontalFOVDegrees`<br><br>float | You can set the intial horizontal FOV of the image. You can set either this field or InitialVerticalFOVDegrees. |
| `PreProcessCropLeftPixels`<br><br>int64 |     |
| `PreProcessCropRightPixels`<br><br>int64 |     |
| `start_info`[](#)<br><br>Object | Update the `start_info` field |
| `type`<br><br>enum{Unspecified, Born, Founded, Started, Opened, Created, Launched} | Required |
| `date`<br><br>Object |     |
| `year`<br><br>integer |     |
| `month`<br><br>integer |     |
| `day`<br><br>integer |     |
| `store_location_descriptor`[](#)<br><br>string | Update the `store_location_descriptor` field |
| `temporary_status`<br><br>enum {DIFFERENTLY\_OPEN, TEMPORARILY\_CLOSED, OPERATING\_AS\_USUAL, NO\_DATA} | Update the `temporary_status` field |
| `website`<br><br>URL | Update the `website` field |
| `zoom_scale_x`<br><br>float | Cover photo zoom scale x |
| `zoom_scale_y`<br><br>float | Cover photo zoom scale y |