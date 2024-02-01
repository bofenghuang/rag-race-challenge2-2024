platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/


### Parameters

| Parameter | Description |
| --- | --- |
| `allow_organic_lead_retrieval`<br><br>boolean | Default value: `true`<br><br>Previously, this flag controlled whether any leads submitted in a non-Ad context were retrievable. Now this flag will not be considered and it will be deprecated entirely. To control visibility of Lead Forms in a non-Ad context you should use 'block\_display\_for\_non\_targeted\_viewer' |
| `block_display_for_non_targeted_viewer`<br><br>boolean | Whether to make the organic post invisible to viewers in non-Ad context |
| `context_card`<br><br>Object | Optional context card shown as the intro page<br><br>Supports Emoji |
| `title`<br><br>string |     |
| `style`<br><br>enum {LIST\_STYLE, PARAGRAPH\_STYLE} |     |
| `content`<br><br>array<string> |     |
| `button_text`<br><br>string |     |
| `cover_photo_id`<br><br>photo ID |     |
| `cover_photo`<br><br>file | Custom cover photo for context card |
| `custom_disclaimer`<br><br>Object | Customized disclaimer including title, body content with inline links, and consent checkboxes |
| `title`<br><br>string |     |
| `body`<br><br>Object |     |
| `text`<br><br>string | Required |
| `url_entities`<br><br>list<JSON object> |     |
| `checkboxes`<br><br>list<Object> |     |
| `is_required`<br><br>boolean | Default value: `true` |
| `is_checked_by_default`<br><br>boolean | Default value: `false` |
| `text`<br><br>string | Required |
| `key`<br><br>string |     |
| `follow_up_action_url`<br><br>URI | The final destination URL that user will go to when clicking view website button |
| `is_for_canvas`<br><br>boolean | Default value: `false`<br><br>Flag to indicate that the form is going to be used under a canvas |
| `is_optimized_for_quality`<br><br>boolean | Default value: `false`<br><br>Flag to indicate whether the form will be optimized for quality |
| `locale`<br><br>enum {AR\_AR, CS\_CZ, DA\_DK, DE\_DE, EL\_GR, EN\_GB, EN\_US, ES\_ES, ES\_LA, FI\_FI, FR\_FR, HE\_IL, HI\_IN, HU\_HU, ID\_ID, IT\_IT, JA\_JP, KO\_KR, NB\_NO, NL\_NL, PL\_PL, PT\_BR, PT\_PT, RO\_RO, RU\_RU, SV\_SE, TH\_TH, TR\_TR, VI\_VN, ZH\_CN, ZH\_HK, ZH\_TW} | The locale of the form. Pre-defined questions renders in this locale |
| `name`<br><br>string | The name that will help identity the form<br><br>Required |
| `privacy_policy`<br><br>Object | The url and link\_text of the privacy policy of advertiser. link\_text is limited to a maximum of 70 characters. |
| `url`<br><br>string |     |
| `link_text`<br><br>string |     |
| `question_page_custom_headline`<br><br>string | The custom headline for the question page within the form |
| `questions`<br><br>list<Object> | An array of questions of the form<br><br>Required |
| `key`<br><br>string |     |
| `label`<br><br>string |     |
| `type`<br><br>enum {CUSTOM, CITY, COMPANY\_NAME, COUNTRY, DOB, EMAIL, GENDER, FIRST\_NAME, FULL\_NAME, JOB\_TITLE, LAST\_NAME, MARITIAL\_STATUS, PHONE, PHONE\_OTP, POST\_CODE, PROVINCE, RELATIONSHIP\_STATUS, STATE, STREET\_ADDRESS, ZIP, WORK\_EMAIL, MILITARY\_STATUS, WORK\_PHONE\_NUMBER, SLIDER, STORE\_LOOKUP, STORE\_LOOKUP\_WITH\_TYPEAHEAD, DATE\_TIME, ID\_CPF, ID\_AR\_DNI, ID\_CL\_RUT, ID\_CO\_CC, ID\_EC\_CI, ID\_PE\_DNI, ID\_MX\_RFC, JOIN\_CODE, USER\_PROVIDED\_PHONE\_NUMBER, FACEBOOK\_LEAD\_ID, EMAIL\_ALIAS, MESSENGER} | Required |
| `inline_context`<br><br>string |     |
| `options`<br><br>list<JSON object> |     |
| `dependent_conditional_questions`<br><br>list<JSON object> |     |
| `conditional_questions_group_id`<br><br>LeadGen Conditional Questions Group ID |     |
| `thank_you_page`<br><br>Object | Optional customized thank you page displayed post submission |
| `title`<br><br>string | Required |
| `body`<br><br>string | Required |
| `short_message`<br><br>string |     |
| `button_text`<br><br>string |     |
| `button_description`<br><br>string |     |
| `business_phone_number`<br><br>phone number string |     |
| `enable_messenger`<br><br>boolean | Default value: `false` |
| `website_url`<br><br>string |     |
| `button_type`<br><br>enum {VIEW\_WEBSITE, CALL\_BUSINESS, MESSAGE\_BUSINESS, DOWNLOAD, SCHEDULE\_APPOINTMENT, VIEW\_ON\_FACEBOOK, NONE} | Required |
| `country_code`<br><br>string |     |
| `tracking_parameters`<br><br>JSON object {string : string} | Map for additional tracking parameters to include with the form's field data |