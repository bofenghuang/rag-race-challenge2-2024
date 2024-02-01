platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The app user's App-Scoped User ID. This ID is unique to the app and cannot be used by other apps.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `about`<br><br>string | _Returns no data as of April 4, 2018._ |
| `age_range`<br><br>[AgeRange](https://developers.facebook.com/docs/graph-api/reference/age-range/) | The age segment for this person expressed as a minimum and maximum age. For example, more than 18, less than 21.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `birthday`<br><br>string | The person's birthday. This is a fixed format string, like `MM/DD/YYYY`. However, people can control who can see the year they were born separately from the month and day so this string can be only the year (YYYY) or the month + day (MM/DD)<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `education`<br><br>[list<EducationExperience>](https://developers.facebook.com/docs/graph-api/reference/education-experience/) | _Returns no data as of April 4, 2018._ |
| `email`<br><br>string | The User's primary email address listed on their profile. This field will not be returned if no valid email address is available.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `favorite_athletes`<br><br>[list<Experience>](https://developers.facebook.com/docs/graph-api/reference/experience/) | Athletes the User likes. |
| `favorite_teams`<br><br>[list<Experience>](https://developers.facebook.com/docs/graph-api/reference/experience/) | Sports teams the User likes. |
| `first_name`<br><br>string | The person's first name<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `gender`<br><br>string | The gender selected by this person, `male` or `female`. If the gender is set to a custom value, this value will be based off of the selected pronoun; it will be omitted if the pronoun is neutral.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `hometown`<br><br>[Page](https://developers.facebook.com/docs/graph-api/reference/page/) | The person's hometown |
| `id_for_avatars`<br><br>numeric string | A profile based app scoped ID. It is used to query avatars |
| `inspirational_people`<br><br>[list<Experience>](https://developers.facebook.com/docs/graph-api/reference/experience/) | The person's inspirational people |
| `installed`<br><br>bool | Is the app making the request installed |
| `is_guest_user`<br><br>bool | if the current user is a guest user. should always return false. |
| `languages`<br><br>[list<Experience>](https://developers.facebook.com/docs/graph-api/reference/experience/) | Facebook Pages representing the languages this person knows |
| `last_name`<br><br>string | The person's last name<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `link`<br><br>string | A link to the person's Timeline. The link will only resolve if the person clicking the link is logged into Facebook and is a friend of the person whose profile is being viewed.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `local_news_megaphone_dismiss_status`<br><br>bool | Display megaphone for local news bookmark<br><br>Deprecated |
| `local_news_subscription_status`<br><br>bool | Daily local news notification<br><br>Deprecated |
| `locale`<br><br>string | The person's locale<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)Deprecated |
| `location`<br><br>[Page](https://developers.facebook.com/docs/graph-api/reference/page/) | The person's current location as entered by them on their profile. This field requires the `user_location` permission.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `meeting_for`<br><br>list<string> | What the person is interested in meeting for |
| `middle_name`<br><br>string | The person's middle name<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `name`<br><br>string | The person's full name<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `name_format`<br><br>string | The person's name formatted to correctly handle Chinese, Japanese, or Korean ordering |
| `political`<br><br>string | _Returns no data as of April 4, 2018._ |
| `quotes`<br><br>string | The person's favorite quotes |
| `relationship_status`<br><br>string | _Returns no data as of April 4, 2018._ |
| `shared_login_upgrade_required_by`[](#)<br><br>timestamp | The time that the shared login needs to be upgraded to Business Manager by |
| `significant_other`<br><br>[User](https://developers.facebook.com/docs/graph-api/reference/user/) | The person's significant other |
| `sports`<br><br>[list<Experience>](https://developers.facebook.com/docs/graph-api/reference/experience/) | Sports played by the person |
| `supports_donate_button_in_live_video`<br><br>bool | Whether the user can add a Donate Button to their Live Videos |
| `third_party_id`<br><br>string | A string containing an anonymous, unique identifier for the User, for use with third-parties. Deprecated for versions 3.0+. Apps using older versions of the API can get this field until January 8, 2019. Apps installed by the User on or after May 1st, 2018, cannot get this field.<br><br>Deprecated |
| `timezone`<br><br>float (min: -24) (max: 24) | The person's current timezone offset from UTC<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)Deprecated |
| `token_for_business`<br><br>string | A token that is the same across a business's apps. Access to this token requires that the person be logged into your app or have a role on your app. This token will change if the business owning the app changes |
| `updated_time`<br><br>datetime | Updated time<br><br>Deprecated |
| `verified`<br><br>bool | Indicates whether the account has been verified. This is distinct from the `is_verified` field. Someone is considered verified if they take any of the following actions:<br><br>                                                                                                                                                                        * Register for mobile<br>                                                                                                                                                                        * Confirm their account via SMS<br>                                                                                                                                                                        * Enter a valid credit card<br>    <br><br>Deprecated |
| `video_upload_limits`<br><br>[VideoUploadLimits](https://developers.facebook.com/docs/graph-api/reference/video-upload-limits/) | Video upload limits |
| `website`<br><br>string | _Returns no data as of April 4, 2018._ |