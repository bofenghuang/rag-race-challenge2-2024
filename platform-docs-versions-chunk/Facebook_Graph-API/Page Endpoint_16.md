platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/


### Parameters

| Parameter | Description |
| --- | --- |
| `account_id`<br><br>int64 | ID of the account |
| `block_send_api`<br><br>boolean | Whether to block messages sent using Send API while user is in Lead Gen Experience |
| `handover_app_id`<br><br>int64 | Hand over thread to specified app after leadgen is complete |
| `handover_summary`<br><br>boolean | Opt-in to get a summary message sent to the target HOP app at the end of the automated flow |
| `privacy_url`<br><br>URI | Privacy URL for Messenger Lead Gen Experience |
| `reminder_text`<br><br>string | Reminder text that will be sent to user after inactivity |
| `step_list`<br><br>array<JSON object> | List of steps in Messenger Lead Gen Experience<br><br>Required |
| `step_id`<br><br>int64 | step\_id<br><br>Required |
| `message`<br><br>string | message<br><br>Required |
| `step_type`<br><br>enum {QUESTION, CONFIRMATION, DISCLAIMER, DISQUALIFY, INFO, INTRO, SUMMARY, POST\_LEAD\_TRANSITION} | step\_type<br><br>Required |
| `reply_type`<br><br>enum {QUICK\_REPLIES, TEXT, NONE, PREFILL, ICE\_BREAKERS, APPOINTMENT, SUBSCRIBE, CALL\_PREFERENCE} | reply\_type<br><br>Required |
| `answers`<br><br>array<string> | Default value: `[]`<br><br>answers |
| `next_step_ids`<br><br>array<int64> | Default value: `[]`<br><br>next\_step\_ids |
| `prefill_type`<br><br>enum {FULL\_ADDRESS, STREET\_ADDRESS, ZIP\_CODE, POST\_CODE, CITY, STATE, PROVINCE, COUNTRY, EMAIL, PHONE, PHONE\_OTP, JOB\_TITLE, COMPANY\_NAME, GENDER, DOB, DATE\_TIME, SLIDER, NONE, FIRST\_NAME, LAST\_NAME, FULL\_NAME, RELATIONSHIP\_STATUS, MARITAL\_STATUS, MILITARY\_STATUS, WORK\_EMAIL, WORK\_PHONE, NATIONAL\_ID\_BRAZIL, NATIONAL\_ID\_ARGENTINA, NATIONAL\_ID\_PERU, NATIONAL\_ID\_CHILE, NATIONAL\_ID\_COLOMBIA, NATIONAL\_ID\_ECUADOR, NATIONAL\_ID\_MEXICO} | Default value: `"NONE"`<br><br>prefill\_type |
| `crm_field_id`<br><br>string | crm\_field\_id |
| `answer_crm_field_ids`<br><br>array<string> | Default value: `[]`<br><br>answer\_crm\_field\_ids |
| `media_type`<br><br>enum {TEXT, IMAGE, VIDEO} | media\_type |
| `media_content`<br><br>string | media\_content |
| `options_format`<br><br>enum {TEXT, CAROUSEL} | Default value: `"TEXT"`<br><br>options\_format |
| `carousel_answers`<br><br>array<JSON object> | Default value: `[]`<br><br>carousel\_answers |
| `value`<br><br>string | value<br><br>Required |
| `media_content`<br><br>string | media\_content<br><br>Required |
| `answer_validation_enabled`<br><br>boolean | answer\_validation\_enabled |
| `invalid_reply_text`<br><br>string | invalid\_reply\_text |
| `cta`<br><br>JSON object | cta |
| `cta_type`<br><br>enum {VIEW\_WEBSITE, CALL\_BUSINESS, MESSAGE\_BUSINESS, DOWNLOAD, SCHEDULE\_APPOINTMENT, VIEW\_ON\_FACEBOOK, NONE} | cta\_type<br><br>Required |
| `cta_text`<br><br>string | cta\_text<br><br>Required |
| `cta_content`<br><br>string | cta\_content<br><br>Required |
| `allow_to_skip`<br><br>boolean | allow\_to\_skip |
| `qualifying_answers_list`<br><br>array<string> | qualifying\_answers\_list |
| `next_step_on_disqualification_id`<br><br>int64 | next\_step\_on\_disqualification\_id |
| `offer_code_file_id`<br><br>int64 | offer\_code\_file\_id |
| `offer_code`<br><br>string | offer\_code |
| `offer_code_format`<br><br>string | offer\_code\_format |
| `stop_question_message`<br><br>string | Confirmation message after user clicks on the Stop Question option in persistent menu |
| `template_name`<br><br>string | Name for the form |
| `tracking_parameters`<br><br>JSON object {string : string} | Tracking Parameters of Lead Forms |