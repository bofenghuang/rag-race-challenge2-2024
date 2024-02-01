platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The app ID<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `aam_rules`<br><br>string | Rules of Auto Advanced Matching in FB SDKs |
| `an_ad_space_limit`<br><br>unsigned int32 | The maximum number of Ad Spaces allowed for each Audience Network supported platform |
| `an_platforms`<br><br>list<enum> | The platforms associated with the app in the Audience Network product. Not enforced, but when present, it can be used to provide the user with platform specific information for the app and its placements |
| `app_domains`<br><br>list<string> | Domains and subdomains this app can use |
| `app_events_config`<br><br>ApplicationAppEventsConfig | Configuration for app events |
| `app_install_tracked`<br><br>bool | Whether the app install is trackable or not |
| `app_name`<br><br>string | App name |
| `app_signals_binding_ios`<br><br>list<Binding> | List of app event bindings for iOS app |
| `app_type`<br><br>unsigned int32 | App type |
| `auth_dialog_data_help_url`<br><br>string | The URL of a special landing page that helps people who are using an app begin publishing Open Graph activity |
| `auth_dialog_headline`<br><br>string | One line description of an app that appears in the Login Dialog |
| `auth_dialog_perms_explanation`<br><br>string | The text to explain why an app needs additional permissions. This appears in the Login Dialog |
| `auth_referral_default_activity_privacy`<br><br>string | The default privacy setting selected for Open Graph activities in the Auth Dialog |
| `auth_referral_enabled`<br><br>unsigned int32 | Indicates whether Authenticated Referrals are enabled |
| `auth_referral_extended_perms`<br><br>list<string> | Extended permissions that a person can choose to grant when Authenticated Referrals are enabled |
| `auth_referral_friend_perms`<br><br>list<string> | Basic friends permissions that a user must grant when Authenticated Referrals are enabled |
| `auth_referral_response_type`<br><br>string | The format that an app receives for the authentication token from the Login Dialog |
| `auth_referral_user_perms`<br><br>list<string> | Basic user permissions that a user must grant when Authenticated Referrals are enabled |
| `canvas_fluid_height`<br><br>bool | Indicates whether the app uses fluid or settable height values for Canvas |
| `canvas_fluid_width`<br><br>unsigned int32 | Indicates whether the app uses fluid or fixed width values for Canvas |
| `canvas_url`<br><br>string | The non-secure URL from which Canvas app content is loaded |
| `category`<br><br>string | The category of the app<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `client_config`<br><br>map | Config data for the client |
| `company`<br><br>string | The company the app belongs to |
| `configured_ios_sso`<br><br>bool | True if the app has configured Single Sign On on iOS |
| `contact_email`<br><br>string | Email address listed for people using the app to contact developers |
| `created_time`<br><br>datetime | Timestamp that indicates when the app was created |
| `creator_uid`<br><br>id | User ID of the creator of this app |
| `daily_active_users`<br><br>numeric string | The number of daily active users the app has |
| `daily_active_users_rank`<br><br>unsigned int32 | Ranking of this app vs other apps comparing daily active users |
| `deauth_callback_url`<br><br>string | URL that is pinged whenever a person removes the app |
| `default_share_mode`<br><br>string | The platform that should be used to share content |
| `description`<br><br>string | The description of the app, as provided by the developer<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `financial_id`<br><br>string | The ID for the corresponding audience network financial entity. |
| `hosting_url`<br><br>string | Webspace created with one of our hosting partners for this app |
| `icon_url`<br><br>string | The URL of this app's icon |
| `ios_bundle_id`<br><br>list<string> | Bundle ID of the associated iOS app |
| `ios_supports_native_proxy_auth_flow`<br><br>bool | Whether to support the native proxy login flow |
| `ios_supports_system_auth`<br><br>bool | Whether to support the iOS integrated Login Dialog |
| `ipad_app_store_id`<br><br>string | ID of the app in the iPad App Store |
| `iphone_app_store_id`<br><br>string | ID of the app in the iPhone App Store |
| `latest_sdk_version`<br><br>ApplicationSDKInfo | App latest sdk version |
| `link`<br><br>string | A link to the app on Facebook<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `logging_token`<br><br>string | To use for logging purposes |
| `logo_url`<br><br>string | The URL of the app's logo |
| `migrations`<br><br>map<string, bool> | Status of migrations for this app |
| `mobile_profile_section_url`<br><br>string | Mobile URL of the app section on a person's profile |
| `mobile_web_url`<br><br>string | URL to which Mobile users will be directed when using the app |
| `monthly_active_users`<br><br>numeric string | The number of monthly active users the app has |
| `monthly_active_users_rank`<br><br>unsigned int32 | Ranking of this app vs other apps comparing monthly active users |
| `name`<br><br>string | The name of the app<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `namespace`<br><br>string | The string appended to `apps.facebook.com/` to navigate to the app's canvas page<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `object_store_urls`<br><br>[ApplicationObjectStoreURLs](https://developers.facebook.com/docs/graph-api/reference/application-object-store-urls/) | Mobile store URLs for the app |
| `page_tab_default_name`<br><br>string | The title of the app when used in a Page Tab |
| `page_tab_url`<br><br>string | The non-secure URL from which Page Tab app content is loaded |
| `photo_url`<br><br>string | The URL of the app photo |
| `privacy_policy_url`<br><br>string | The URL that links to a Privacy Policy for the app |
| `profile_section_url`<br><br>string | URL of the app section on a user's profile for the desktop site |
| `property_id`<br><br>string | The monetization property which owns this app |
| `protected_mode_rules`<br><br>ApplicationProtectedModeRules | protected\_mode\_rules |
| `real_time_mode_devices`<br><br>list<string> | List of real time hashed device |
| `restrictions`<br><br>[ApplicationRestrictionInfo](https://developers.facebook.com/docs/graph-api/reference/application-restriction-info/) | Demographic restrictions for the app |
| `restrictive_data_filter_params`<br><br>string | Params used to filter out restrictive data |
| `secure_canvas_url`<br><br>string | The secure URL from which Canvas app content is loaded |
| `secure_page_tab_url`<br><br>string | The secure URL from which Page Tab app content is loaded |
| `server_ip_whitelist`<br><br>string | App requests must originate from this comma-separated list of IP addresses |
| `social_discovery`<br><br>unsigned int32 | Indicates whether app usage stories show up in the Ticker or Feed |
| `subcategory`<br><br>string | The subcategory the app can be found under |
| `suggested_events_setting`<br><br>string | Settings for suggested events |
| `supported_platforms`<br><br>list<enum {WEB, CANVAS, MOBILE\_WEB, IPHONE, IPAD, ANDROID, WINDOWS, AMAZON, SUPPLEMENTARY\_IMAGES, GAMEROOM, INSTANT\_GAME, OCULUS, SAMSUNG, XIAOMI}> | All the platform the app supports |
| `terms_of_service_url`<br><br>string | URL to Terms of Service that appears in the Login Dialog |
| `url_scheme_suffix`<br><br>string | URL scheme suffix |
| `user_support_email`<br><br>string | Main contact email for this app where people can receive support |
| `user_support_url`<br><br>string | URL shown in the Canvas footer that people can visit to get support for the app |
| `website_url`<br><br>string | URL of a website that integrates with this app |
| `weekly_active_users`<br><br>numeric string | The number of weekly active users the app has |