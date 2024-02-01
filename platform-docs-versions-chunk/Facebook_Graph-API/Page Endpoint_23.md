platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/


### Parameters

| Parameter | Description |
| --- | --- |
| `actions` | SELF\_EXPLANATORY |
| `adaptive_type`<br><br>string | adaptive\_type |
| `album_id`<br><br>numeric string | SELF\_EXPLANATORY |
| `android_key_hash`<br><br>string | SELF\_EXPLANATORY |
| `animated_effect_id`<br><br>int64 | animated\_effect\_id |
| `application_id`<br><br>non-empty string | SELF\_EXPLANATORY |
| `asked_fun_fact_prompt_id`<br><br>int64 | asked\_fun\_fact\_prompt\_id |
| `asset3d_id`<br><br>int64 | asset3d\_id |
| `associated_id`<br><br>numeric string or integer | SELF\_EXPLANATORY |
| `attach_place_suggestion`<br><br>boolean | Default value: `false`<br><br>SELF\_EXPLANATORY |
| `attached_media`<br><br>list<Object> | SELF\_EXPLANATORY |
| `media_fbid`<br><br>numeric string |     |
| `message`<br><br>UTF-8 string | Supports Emoji |
| `audience_exp`<br><br>boolean | Default value: `false`<br><br>SELF\_EXPLANATORY |
| `backdated_time`<br><br>datetime | SELF\_EXPLANATORY |
| `backdated_time_granularity`<br><br>enum{year, month, day, hour, min, none} | Default value: `none`<br><br>SELF\_EXPLANATORY |
| `breaking_news`<br><br>boolean | breaking\_news |
| `breaking_news_expiration`<br><br>int64 | breaking\_news\_expiration |
| `call_to_action`<br><br>Object | SELF\_EXPLANATORY<br><br>Supports Emoji |
| `type`<br><br>enum{BOOK\_TRAVEL, CONTACT\_US, DONATE, DONATE\_NOW, DOWNLOAD, GET\_DIRECTIONS, GO\_LIVE, INTERESTED, LEARN\_MORE, LIKE\_PAGE, MESSAGE\_PAGE, RAISE\_MONEY, SAVE, SEND\_TIP, SHOP\_NOW, SIGN\_UP, VIEW\_INSTAGRAM\_PROFILE, INSTAGRAM\_MESSAGE, LOYALTY\_LEARN\_MORE, PURCHASE\_GIFT\_CARDS, PAY\_TO\_ACCESS, SEE\_MORE, TRY\_IN\_CAMERA, WHATSAPP\_LINK, BOOK\_NOW, CHECK\_AVAILABILITY, ORDER\_NOW, WHATSAPP\_MESSAGE, GET\_MOBILE\_APP, INSTALL\_MOBILE\_APP, USE\_MOBILE\_APP, INSTALL\_APP, USE\_APP, PLAY\_GAME, WATCH\_VIDEO, WATCH\_MORE, OPEN\_LINK, NO\_BUTTON, LISTEN\_MUSIC, MOBILE\_DOWNLOAD, GET\_OFFER, GET\_OFFER\_VIEW, BUY\_NOW, BUY\_TICKETS, UPDATE\_APP, BET\_NOW, ADD\_TO\_CART, SELL\_NOW, GET\_SHOWTIMES, LISTEN\_NOW, GET\_EVENT\_TICKETS, REMIND\_ME, SEARCH\_MORE, PRE\_REGISTER, SWIPE\_UP\_PRODUCT, SWIPE\_UP\_SHOP, PLAY\_GAME\_ON\_FACEBOOK, VISIT\_WORLD, OPEN\_INSTANT\_APP, JOIN\_GROUP, GET\_PROMOTIONS, SEND\_UPDATES, INQUIRE\_NOW, VISIT\_PROFILE, CHAT\_ON\_WHATSAPP, EXPLORE\_MORE, CONFIRM, JOIN\_CHANNEL, CALL, MISSED\_CALL, CALL\_NOW, CALL\_ME, APPLY\_NOW, BUY, GET\_QUOTE, SUBSCRIBE, RECORD\_NOW, VOTE\_NOW, GIVE\_FREE\_RIDES, REGISTER\_NOW, OPEN\_MESSENGER\_EXT, EVENT\_RSVP, CIVIC\_ACTION, SEND\_INVITES, REFER\_FRIENDS, REQUEST\_TIME, SEE\_MENU, SEARCH, TRY\_IT, TRY\_ON, LINK\_CARD, DIAL\_CODE, FIND\_YOUR\_GROUPS, START\_ORDER} | The type of the action. Not all types can be used for all ads. Check [Ads Product Guide](https://www.facebook.com/business/ads-guide) to see which type can be used for based on the `objective` of your campaign.<br><br>Required |
| `value`<br><br>Object | Default value: `Vec`<br><br>JSON containing the call to action data.<br><br>Supports Emoji |
| `link`<br><br>URL |     |
| `app_link`<br><br>string |     |
| `page`<br><br>numeric string or integer |     |
| `link_format`<br><br>enum {VIDEO\_LEAD, VIDEO\_LPP, VIDEO\_NEKO, VIDEO\_NON\_LINK, VIDEO\_SHOP, WHATSAPP\_CATALOG\_ATTACHMENT} |     |
| `application`<br><br>numeric string or integer |     |
| `link_title`<br><br>string | Supports Emoji |
| `link_description`<br><br>string | Supports Emoji |
| `link_caption`<br><br>string |     |
| `product_link`<br><br>string |     |
| `get_movie_showtimes`<br><br>boolean |     |
| `sponsorship`<br><br>Object |     |
| `link`<br><br>URL |     |
| `image`<br><br>URL |     |
| `video_annotation`<br><br>Object |     |
| `annotations`<br><br>list<Object> |     |
| `start_time_in_sec`<br><br>int64 |     |
| `end_time_in_sec`<br><br>int64 |     |
| `link`<br><br>URL |     |
| `link_title`<br><br>string |     |
| `link_description`<br><br>string |     |
| `link_caption`<br><br>string |     |
| `image_url`<br><br>URL |     |
| `header_color`<br><br>string |     |
| `logo_url`<br><br>URL |     |
| `post_click_cta_title`<br><br>string |     |
| `post_click_description_title`<br><br>string |     |
| `offer_id`<br><br>numeric string or integer |     |
| `offer_view_id`<br><br>numeric string or integer |     |
| `advanced_data`<br><br>Object |     |
| `offer_id`<br><br>numeric string or integer |     |
| `lead_gen_form_id`<br><br>numeric string or integer |     |
| `referral_id`<br><br>numeric string or integer |     |
| `fundraiser_campaign_id`<br><br>numeric string or integer |     |
| `event_id`<br><br>numeric string or integer |     |
| `event_tour_id`<br><br>numeric string or integer |     |
| `app_destination`<br><br>enum {MESSENGER, MESSENGER\_EXTENSIONS, MESSENGER\_GAMES, LINK\_CARD, MARKETPLACE, WHATSAPP, INSTAGRAM\_DIRECT} |     |
| `app_destination_page_id`<br><br>numeric string or integer |     |
| `is_canvas_video_transition_enabled`<br><br>boolean |     |
| `whatsapp_number`<br><br>string |     |
| `preinput_text`<br><br>string |     |
| `customized_message_page_cta_text`<br><br>string |     |
| `external_offer_provider_id`<br><br>numeric string or integer |     |
| `origins`<br><br>enum {COMPOSER, CAMERA} |     |
| `object_store_urls`<br><br>array<string> |     |
| `facebook_login_spec`<br><br>Object |     |
| `facebook_login_app_id`<br><br>numeric string or integer |     |
| `offer_type`<br><br>enum {NO\_OFFER, PERCENTAGE\_BASED, AMOUNT\_BASED} |     |
| `offer_pct_call_to_action`<br><br>enum {TEN} |     |
| `offer_amt_call_to_action`<br><br>enum {TEN} |     |
| `product_id`<br><br>numeric string or integer |     |
| `group_id`<br><br>numeric string or integer |     |
| `caption`<br><br>string | SELF\_EXPLANATORY<br><br>Supports Emoji |
| `child_attachments`<br><br>list<Object> | SELF\_EXPLANATORY<br><br>Supports Emoji |
| `picture`<br><br>URL |     |
| `name`<br><br>string | Supports Emoji |
| `link`<br><br>URL | Required |
| `caption`<br><br>string | Supports Emoji |
| `description`<br><br>string | Supports Emoji |
| `quote`<br><br>UTF-8 string | Supports Emoji |
| `source`<br><br>URL |     |
| `properties` |     |
| `object_attachment`<br><br>numeric string or integer |     |
| `height`<br><br>int64 |     |
| `width`<br><br>int64 |     |
| `expanded_height`<br><br>int64 |     |
| `expanded_width`<br><br>int64 |     |
| `referral_id`<br><br>numeric string or integer |     |
| `thumbnail`<br><br>file |     |
| `image_crops`<br><br>dictionary { enum{191x100, 100x72, 400x150, 600x360, 100x100, 400x500, 90x160} : <list<list<int64>>> } |     |
| `call_to_action`<br><br>Object | Supports Emoji |
| `type`<br><br>enum{BOOK\_TRAVEL, CONTACT\_US, DONATE, DONATE\_NOW, DOWNLOAD, GET\_DIRECTIONS, GO\_LIVE, INTERESTED, LEARN\_MORE, LIKE\_PAGE, MESSAGE\_PAGE, RAISE\_MONEY, SAVE, SEND\_TIP, SHOP\_NOW, SIGN\_UP, VIEW\_INSTAGRAM\_PROFILE, INSTAGRAM\_MESSAGE, LOYALTY\_LEARN\_MORE, PURCHASE\_GIFT\_CARDS, PAY\_TO\_ACCESS, SEE\_MORE, TRY\_IN\_CAMERA, WHATSAPP\_LINK, BOOK\_NOW, CHECK\_AVAILABILITY, ORDER\_NOW, WHATSAPP\_MESSAGE, GET\_MOBILE\_APP, INSTALL\_MOBILE\_APP, USE\_MOBILE\_APP, INSTALL\_APP, USE\_APP, PLAY\_GAME, WATCH\_VIDEO, WATCH\_MORE, OPEN\_LINK, NO\_BUTTON, LISTEN\_MUSIC, MOBILE\_DOWNLOAD, GET\_OFFER, GET\_OFFER\_VIEW, BUY\_NOW, BUY\_TICKETS, UPDATE\_APP, BET\_NOW, ADD\_TO\_CART, SELL\_NOW, GET\_SHOWTIMES, LISTEN\_NOW, GET\_EVENT\_TICKETS, REMIND\_ME, SEARCH\_MORE, PRE\_REGISTER, SWIPE\_UP\_PRODUCT, SWIPE\_UP\_SHOP, PLAY\_GAME\_ON\_FACEBOOK, VISIT\_WORLD, OPEN\_INSTANT\_APP, JOIN\_GROUP, GET\_PROMOTIONS, SEND\_UPDATES, INQUIRE\_NOW, VISIT\_PROFILE, CHAT\_ON\_WHATSAPP, EXPLORE\_MORE, CONFIRM, JOIN\_CHANNEL, CALL, MISSED\_CALL, CALL\_NOW, CALL\_ME, APPLY\_NOW, BUY, GET\_QUOTE, SUBSCRIBE, RECORD\_NOW, VOTE\_NOW, GIVE\_FREE\_RIDES, REGISTER\_NOW, OPEN\_MESSENGER\_EXT, EVENT\_RSVP, CIVIC\_ACTION, SEND\_INVITES, REFER\_FRIENDS, REQUEST\_TIME, SEE\_MENU, SEARCH, TRY\_IT, TRY\_ON, LINK\_CARD, DIAL\_CODE, FIND\_YOUR\_GROUPS, START\_ORDER} | The type of the action. Not all types can be used for all ads. Check [Ads Product Guide](https://www.facebook.com/business/ads-guide) to see which type can be used for based on the `objective` of your campaign.<br><br>Required |
| `value`<br><br>Object | Default value: `Vec`<br><br>JSON containing the call to action data.<br><br>Supports Emoji |
| `link`<br><br>URL |     |
| `app_link`<br><br>string |     |
| `page`<br><br>numeric string or integer |     |
| `link_format`<br><br>enum {VIDEO\_LEAD, VIDEO\_LPP, VIDEO\_NEKO, VIDEO\_NON\_LINK, VIDEO\_SHOP, WHATSAPP\_CATALOG\_ATTACHMENT} |     |
| `application`<br><br>numeric string or integer |     |
| `link_title`<br><br>string | Supports Emoji |
| `link_description`<br><br>string | Supports Emoji |
| `link_caption`<br><br>string |     |
| `product_link`<br><br>string |     |
| `get_movie_showtimes`<br><br>boolean |     |
| `sponsorship`<br><br>Object |     |
| `link`<br><br>URL |     |
| `image`<br><br>URL |     |
| `video_annotation`<br><br>Object |     |
| `annotations`<br><br>list<Object> |     |
| `start_time_in_sec`<br><br>int64 |     |
| `end_time_in_sec`<br><br>int64 |     |
| `link`<br><br>URL |     |
| `link_title`<br><br>string |     |
| `link_description`<br><br>string |     |
| `link_caption`<br><br>string |     |
| `image_url`<br><br>URL |     |
| `header_color`<br><br>string |     |
| `logo_url`<br><br>URL |     |
| `post_click_cta_title`<br><br>string |     |
| `post_click_description_title`<br><br>string |     |
| `offer_id`<br><br>numeric string or integer |     |
| `offer_view_id`<br><br>numeric string or integer |     |
| `advanced_data`<br><br>Object |     |
| `offer_id`<br><br>numeric string or integer |     |
| `lead_gen_form_id`<br><br>numeric string or integer |     |
| `referral_id`<br><br>numeric string or integer |     |
| `fundraiser_campaign_id`<br><br>numeric string or integer |     |
| `event_id`<br><br>numeric string or integer |     |
| `event_tour_id`<br><br>numeric string or integer |     |
| `app_destination`<br><br>enum {MESSENGER, MESSENGER\_EXTENSIONS, MESSENGER\_GAMES, LINK\_CARD, MARKETPLACE, WHATSAPP, INSTAGRAM\_DIRECT} |     |
| `app_destination_page_id`<br><br>numeric string or integer |     |
| `is_canvas_video_transition_enabled`<br><br>boolean |     |
| `whatsapp_number`<br><br>string |     |
| `preinput_text`<br><br>string |     |
| `customized_message_page_cta_text`<br><br>string |     |
| `external_offer_provider_id`<br><br>numeric string or integer |     |
| `origins`<br><br>enum {COMPOSER, CAMERA} |     |
| `object_store_urls`<br><br>array<string> |     |
| `facebook_login_spec`<br><br>Object |     |
| `facebook_login_app_id`<br><br>numeric string or integer |     |
| `offer_type`<br><br>enum {NO\_OFFER, PERCENTAGE\_BASED, AMOUNT\_BASED} |     |
| `offer_pct_call_to_action`<br><br>enum {TEN} |     |
| `offer_amt_call_to_action`<br><br>enum {TEN} |     |
| `product_id`<br><br>numeric string or integer |     |
| `group_id`<br><br>numeric string or integer |     |
| `image_hash`<br><br>string |     |
| `static_card`<br><br>boolean |     |
| `place_data`<br><br>Object |     |
| `address_string`<br><br>string |     |
| `label`<br><br>string |     |
| `latitude` |     |
| `location_source_id`<br><br>location page/page set ID |     |
| `longitude` |     |
| `type`<br><br>enum {DYNAMIC, REALTIME, SINGLE} | Required |
| `video_id`<br><br>numeric string or integer |     |
| `caption_ids`<br><br>list<numeric string or integer> |     |
| `offer_id`<br><br>numeric string or integer |     |
| `client_mutation_id`<br><br>string | SELF\_EXPLANATORY |
| `composer_entry_picker`<br><br>string | composer\_entry\_picker |
| `composer_entry_point`<br><br>string | composer\_entry\_point |
| `composer_entry_time`<br><br>int64 | composer\_entry\_time |
| `composer_session_events_log`<br><br>JSON-encoded string | composer\_session\_events\_log |
| `composer_session_id`<br><br>string | SELF\_EXPLANATORY |
| `composer_source_surface`<br><br>string | composer\_source\_surface |
| `composer_type`<br><br>string | composer\_type |
| `connection_class`<br><br>string | SELF\_EXPLANATORY |
| `content_attachment`<br><br>numeric string | content\_attachment |
| `coordinates`<br><br>JSON-encoded coordinate list | SELF\_EXPLANATORY |
| `cta_link`<br><br>string | cta\_link |
| `cta_type`<br><br>string | cta\_type |
| `description`<br><br>string | SELF\_EXPLANATORY<br><br>Supports Emoji |
| `direct_share_status`<br><br>int64 | direct\_share\_status |
| `enforce_link_ownership`<br><br>boolean | Default value: `false`<br><br>SELF\_EXPLANATORY |
| `expanded_height`<br><br>int64 | SELF\_EXPLANATORY |
| `expanded_width`<br><br>int64 | SELF\_EXPLANATORY |
| `feed_targeting`<br><br>feed target | SELF\_EXPLANATORY |
| `geo_locations`<br><br>Object |     |
| `countries`<br><br>list<string> |     |
| `regions`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `cities`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `zips`<br><br>list<Object> |     |
| `key`<br><br>string |     |
| `locales`<br><br>list<string> | Values for targeted locales. Use `type` of `adlocale` to [find Targeting Options](https://developers.facebook.com/docs/marketing-api/targeting-search) and use the returned key to specify. |
| `age_min`<br><br>int64 | Must be `13` or higher. Default is 0. |
| `age_max`<br><br>int64 | Maximum age. |
| `genders`<br><br>list<int64> | Target specific genders. `1` targets all male viewers and `2` females. Default is to target both. |
| `college_years`<br><br>list<int64> | Array of integers. Represent graduation years from college. |
| `education_statuses`<br><br>list<int64> | Array of integers which represent current educational status. Use `1` for high school, `2` for undergraduate, and `3` for alum (or localized equivalents). |
| `interested_in`<br><br>list<int64> | Deprecated. Please see the [Graph API Changelog](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes#2-7-2018) for more information.<br><br>Deprecated |
| `relationship_statuses`<br><br>list<int64> | Array of integers for targeting based on relationship status. Use `1` for single, `2` for 'in a relationship', `3` for married, and `4` for engaged. Default is all types. |
| `interests`<br><br>list<int64> | One or more IDs of pages to target fans of pages.Use `type` of `page` to get possible IDs as [find Targeting Options](https://developers.facebook.com/docs/marketing-api/targeting-search) and use the returned id to specify. |
| `formatting`<br><br>enum {PLAINTEXT, MARKDOWN} | formatting |
| `fun_fact_prompt_id`<br><br>int64 | fun\_fact\_prompt\_id |
| `fun_fact_toastee_id`<br><br>int64 | fun\_fact\_toastee\_id |
| `has_nickname`<br><br>boolean | has\_nickname |
| `height`<br><br>int64 | SELF\_EXPLANATORY |
| `holiday_card`<br><br>JSON-encoded string | holiday\_card |
| `home_checkin_city_id`<br><br>place tag | SELF\_EXPLANATORY |
| `image_crops`<br><br>dictionary { enum{191x100, 100x72, 400x150, 600x360, 100x100, 400x500, 90x160} : <list<list<int64>>> } | SELF\_EXPLANATORY |
| `implicit_with_tags`<br><br>list<int> | SELF\_EXPLANATORY |
| `instant_game_entry_point_data`<br><br>string | instant\_game\_entry\_point\_data |
| `ios_bundle_id`<br><br>string | SELF\_EXPLANATORY |
| `is_backout_draft`<br><br>boolean | is\_backout\_draft |
| `is_boost_intended`<br><br>boolean | is\_boost\_intended |
| `is_explicit_location`<br><br>boolean | SELF\_EXPLANATORY |
| `is_explicit_share`<br><br>boolean | SELF\_EXPLANATORY |
| `is_group_linking_post`<br><br>boolean | is\_group\_linking\_post |
| `is_photo_container`<br><br>boolean | SELF\_EXPLANATORY |
| `link`<br><br>URL | SELF\_EXPLANATORY |
| `location_source_id`<br><br>numeric string or integer | location\_source\_id |
| `manual_privacy`<br><br>boolean | Default value: `false`<br><br>SELF\_EXPLANATORY |
| `message`<br><br>UTF-8 string | SELF\_EXPLANATORY<br><br>Supports Emoji |
| `multi_share_end_card`<br><br>boolean | Default value: `true`<br><br>SELF\_EXPLANATORY |
| `multi_share_optimized`<br><br>boolean | Default value: `true`<br><br>SELF\_EXPLANATORY |
| `name`<br><br>string | SELF\_EXPLANATORY<br><br>Supports Emoji |
| `nectar_module`<br><br>string | SELF\_EXPLANATORY |
| `object_attachment`<br><br>numeric string or integer | SELF\_EXPLANATORY |
| `offer_like_post_id`<br><br>int64 | offer\_like\_post\_id |
| `og_action_type_id`<br><br>numeric string or integer | SELF\_EXPLANATORY |
| `og_hide_object_attachment`<br><br>boolean | SELF\_EXPLANATORY |
| `og_icon_id`<br><br>numeric string or integer | SELF\_EXPLANATORY |
| `og_object_id`<br><br>OG object ID or URL string | SELF\_EXPLANATORY |
| `og_phrase`<br><br>UTF-8 string | SELF\_EXPLANATORY<br><br>Supports Emoji |
| `og_set_profile_badge`<br><br>boolean | Default value: `false`<br><br>og\_set\_profile\_badge |
| `og_suggestion_mechanism`<br><br>string | SELF\_EXPLANATORY |
| `page_recommendation`<br><br>JSON-encoded string | page\_recommendation |
| `picture`<br><br>URL | SELF\_EXPLANATORY |
| `place`<br><br>place tag | SELF\_EXPLANATORY |
| `place_attachment_setting`<br><br>enum {1, 2} | Default value: `2`<br><br>place\_attachment\_setting |
| `place_list`<br><br>JSON-encoded string | place\_list |
| `place_list_data`<br><br>array | place\_list\_data |
| `post_surfaces_blacklist`<br><br>list<enum {1, 2, 3, 4, 5}> | post\_surfaces\_blacklist |
| `posting_to_redspace`<br><br>enum {enabled, disabled} | Default value: `disabled`<br><br>posting\_to\_redspace |
| `privacy`<br><br>Privacy Parameter | SELF\_EXPLANATORY |
| `prompt_id`<br><br>string | prompt\_id |
| `prompt_tracking_string`<br><br>string | prompt\_tracking\_string |
| `properties` | SELF\_EXPLANATORY |
| `proxied_app_id`<br><br>numeric string or integer | SELF\_EXPLANATORY |
| `publish_event_id`<br><br>int64 | publish\_event\_id |
| `published`<br><br>boolean | Default value: `true`<br><br>SELF\_EXPLANATORY |
| `quote`<br><br>UTF-8 string | quote<br><br>Supports Emoji |
| `react_mode_metadata`<br><br>JSON-encoded string | This metadata is required for clip reacts feature |
| `ref`<br><br>list<string> | Default value: `Default`<br><br>SELF\_EXPLANATORY |
| `referenceable_image_ids`<br><br>list<numeric string or integer> | referenceable\_image\_ids |
| `referral_id`<br><br>numeric string or integer | referral\_id |
| `scheduled_publish_time`<br><br>datetime | SELF\_EXPLANATORY |
| `source`<br><br>URL | SELF\_EXPLANATORY |
| `sponsor_id`<br><br>numeric string or integer | sponsor\_id |
| `sponsor_relationship`<br><br>int64 | sponsor\_relationship |
| `suggested_place_id`<br><br>place tag | SELF\_EXPLANATORY |
| `tags`<br><br>list<int> | SELF\_EXPLANATORY |
| `target_surface`<br><br>enum {STORY, TIMELINE} | Default value: `"TIMELINE"`<br><br>target\_surface |
| `targeting`<br><br>target | SELF\_EXPLANATORY |
| `geo_locations`<br><br>Object |     |
| `countries`<br><br>list<string> |     |
| `regions`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `cities`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `zips`<br><br>list<Object> |     |
| `key`<br><br>string |     |
| `locales`<br><br>list<string> |     |
| `excluded_countries`[](#)<br><br>list<string> |     |
| `excluded_regions`[](#)<br><br>list<int64> |     |
| `excluded_cities`[](#)<br><br>list<int64> |     |
| `excluded_zipcodes`[](#)<br><br>list<string> |     |
| `timezones`[](#)<br><br>list<int64> |     |
| `age_min`<br><br>enum {13, 15, 18, 21, 25} |     |
| `text_format_metadata`<br><br>JSON-encoded string | text\_format\_metadata |
| `text_format_preset_id`<br><br>numeric string or integer | text\_format\_preset\_id |
| `text_only_place`<br><br>string | SELF\_EXPLANATORY |
| `throwback_camera_roll_media`<br><br>JSON-encoded string | throwback\_camera\_roll\_media |
| `thumbnail`<br><br>file | SELF\_EXPLANATORY |
| `time_since_original_post`<br><br>int64 | SELF\_EXPLANATORY |
| `title`<br><br>UTF-8 string | SELF\_EXPLANATORY<br><br>Supports Emoji |
| `tracking_info`<br><br>JSON-encoded string | tracking\_info |
| `unpublished_content_type`<br><br>enum {SCHEDULED, SCHEDULED\_RECURRING, DRAFT, ADS\_POST, INLINE\_CREATED, PUBLISHED, REVIEWABLE\_BRANDED\_CONTENT} | SELF\_EXPLANATORY |
| `user_selected_tags`<br><br>boolean | Default value: `false`<br><br>SELF\_EXPLANATORY |
| `video_start_time_ms`<br><br>int64 | video\_start\_time\_ms |
| `viewer_coordinates`<br><br>JSON-encoded coordinate list | SELF\_EXPLANATORY |
| `width`<br><br>int64 | SELF\_EXPLANATORY |