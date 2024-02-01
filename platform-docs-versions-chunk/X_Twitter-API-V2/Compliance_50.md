platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/api-reference/get-users-compliance-stream

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `user_delete` | string | A delete user event. |
| `user_undelete` | string | A undelete user event. |
| `user_withheld` | string | A withheld user event. |
| `user_protect` | string | A protect user event. |
| `user_unprotect` | string | A unprotect user event. |
| `user_suspend` | string | A suspend user event. |
| `user_unsuspend` | string | A unsuspend user event. |
| `scrub_geo` | string | A geo scrub user event. |
| `user_profile_modification` | string | A modified user profile event. |
| `id` | string | The ID of the user triggering a compliance event. |
| `event_at` | date (ISO 8601) | Time of when event happended. |
| `withheld_in_countries` | string | Country where user is withheld. |
| `up_to_tweet_id` | string | Provided when a user removes their geo metadata. |
| `profile_field` | string | Indicates what Profile attribute was updated. |