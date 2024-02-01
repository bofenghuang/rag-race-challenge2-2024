platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/


### Parameters

| Parameter | Description |
| --- | --- |
| `allow_cycle_app_secret`<br><br>boolean | Default value: `false`<br><br>Allows for the application to cycle the secret |
| `an_platforms`<br><br>list<enum {ANDROID, DESKTOP, GALAXY, INSTANT\_ARTICLES, IOS, MOBILE\_WEB, OCULUS, UNKNOWN, XIAOMI}> | The platforms associated with the app in the AudienceNetwork product |
| `app_domains`<br><br>list<string> | Specifies a list of domains that correspond to this app. Subdomains of domains in this array are also considered to belong to this app |
| `app_name`<br><br>string | App name |
| `app_type`<br><br>boolean | App type |
| `auth_dialog_headline`<br><br>string | One line description of this app that appears in the Login Dialog |
| `auth_dialog_perms_explanation`<br><br>string | The text to explain why an app needs additional permissions. This appears in the Login Dialog |
| `auth_referral_default_activity_privacy`<br><br>string | The default privacy setting selected for Open Graph activities in the Auth Dialog |
| `auth_referral_enabled`<br><br>boolean | Enables or disables Authenticated Referrals |
| `auth_referral_extended_perms`<br><br>list<string> | Extended permissions that a person can choose to grant when Authenticated Referrals are enabled |
| `auth_referral_friend_perms`<br><br>list<string> | Basic friends permissions that a person must grant when Authenticated Referrals are enabled |
| `auth_referral_response_type`<br><br>string | The format of the authentication token this app receives from the Login Dialog |
| `auth_referral_user_perms`<br><br>list<string> | Basic permissions that a person must grant when Authenticated Referrals are enabled |
| `canvas_fluid_height`<br><br>boolean | Indicates whether this app uses fluid or settable height values for Canvas |
| `canvas_fluid_width`<br><br>boolean | Indicates whether this app uses fluid or fixed width values for Canvas |
| `canvas_url`<br><br>URL | The non-secure URL from which Canvas app content is loaded |
| `contact_email`<br><br>string | Email address users can use to contact developers |
| `deauth_callback_url`<br><br>URL | URL that is pinged whenever a person removes this app |
| `mobile_web_url`<br><br>URL | URL that mobile users will be directed to when using this app |
| `namespace`<br><br>string | The string appended to `apps.facebook.com/` to navigate to this app's Canvas page |
| `page_tab_default_name`<br><br>string | The title of this app as it appears in a Page Tab |
| `privacy_policy_url`<br><br>URL | The URL that links to a privacy policy for this app |
| `restrictions`<br><br>JSON-encoded string | Update demographic restrictions for this app. Can be one or more of the following parameters: `age`, `location`, or `type`. `age` can be one of the following values: `13+`, `16+`, `17+`, `18+`, `19+`, or `21+`. `location` can be one or more country represented by the [2 letter country code](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FISO_3166-1_alpha-2&h=AT1_YAOqq0dGg4nMWqEjjHyk1slwChUKz5CjIjr069qs_9-X75A-spaMrLXkOuVaQKpeeNPkJh1LLxsLqRWaUfpagl2x3jPPjaHLoNwqgsCb-VVNEa2POEZi60Izfb7kvfQhZ1Oaxv4LgXFi). `type` can only be `alcohol`. |
| `secure_canvas_url`<br><br>URL | The secure URL from which Canvas app content is loaded |
| `secure_page_tab_url`<br><br>URL | The secure URL from which Page Tab app content is loaded |
| `server_ip_whitelist`<br><br>list<string> | App requests must originate from this comma-separated list of IP addresses |
| `terms_of_service_url`<br><br>URL | URL to Terms of Service that appears in the Login Dialog |
| `url_scheme_suffix`<br><br>string | URL scheme suffix |
| `user_support_email`<br><br>string | Main contact email for this app where people can receive support |
| `user_support_url`<br><br>URL | URL shown in the Canvas footer that people can visit to get support for this app |
| `website_url`<br><br>URL | URL of a website that integrates with this app |