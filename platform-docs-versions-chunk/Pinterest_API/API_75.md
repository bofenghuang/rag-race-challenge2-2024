platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_group_id": "2680059592705",      * "android_deep_link": "string",      * "carousel_android_deep_links": [          * "string"                   ],      * "carousel_destination_urls": [          * "string"                   ],      * "carousel_ios_deep_links": [          * "string"                   ],      * "click_tracking_url": "string",      * "creative_type": "REGULAR",      * "destination_url": "string",      * "ios_deep_link": "string",      * "is_pin_deleted": false,      * "is_removable": false,      * "name": "string",      * "status": "ACTIVE",      * "tracking_urls": {          * "impression": [                  * "URL1",                      * "URL2"                               ],              * "click": [                  * "URL1",                      * "URL2"                               ],              * "engagement": [                  * "URL1",                      * "URL2"                               ],              * "buyable_button": [                  * "URL1",                      * "URL2"                               ],              * "audience_verification": [                  * "URL1",                      * "URL2"                               ]                   },      * "view_tracking_url": "string",      * "lead_form_id": "string",      * "grid_click_type": "CLOSEUP",      * "customizable_cta_type": "LEARN_MORE",      * "quiz_pin_data": {          * "questions": [                  * {                          * "question_id": 1,                              * "question_text": "Where do you thrive?",                              * "options": [                                  * {                                          * "text": "Hangout vibes"                                                                   },                                      * {                                          * "text": "Time to party!"                                                                   },                                      * {                                          * "text": "Keeping it lowkey"                                                                   }                                                       ]                                           },                      * {                          * "question_id": 2,                              * "question_text": "Where would you nap?",                              * "options": [                                  * {                                          * "text": "Hammock in the mountains"                                                                   },                                      * {                                          * "text": "Beach towel in the sand"                                                                   },                                      * {                                          * "text": "Tent under the stars"                                                                   }                                                       ]                                           },                      * {                          * "question_id": 2,                              * "question_text": "Who are you taking?",                              * "options": [                                  * {                                          * "text": "No one—solo trip!"                                                                   },                                      * {                                          * "text": "My best friend"                                                                   },                                      * {                                          * "text": "The family"                                                                   }                                                       ]                                           }                               ],              * "results": [                  * {                          * "organicPinId": "1234",                              * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "result_id": 1                                           },                      * {                          * "organicPinId": "1234",                              * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "result_id": 2                                           },                      * {                          * "organicPinId": "1234",                              * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "result_id": 3                                           }                               ]                   },      * "pin_id": "394205773611545468",      * "ad_account_id": "549755885175",      * "campaign_id": "626735565838",      * "collection_items_destination_url_template": "string",      * "created_time": 1451431341,      * "id": "687195134316",      * "rejected_reasons": [          * "HASHTAGS"                   ],      * "rejection_labels": [          * "string"                   ],      * "review_status": "PENDING",      * "type": "pinpromotion",      * "updated_time": 1451431341,      * "summary_status": "APPROVED"       }`