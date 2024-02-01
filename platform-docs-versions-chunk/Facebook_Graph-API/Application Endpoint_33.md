platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/activities/

### Return Type

Struct {

`success`: bool,

} Or Struct {

`applink_class`: string,

`applink_url`: string,

`applink_args`: string,

`is_fb`: bool,

`is_paid`: bool,

`account_id`: ad account id,

`ad_id`: numeric string,

`ad_objective_name`: string,

`adgroup_id`: numeric string,

`adgroup_name`: string,

`campaign_id`: numeric string,

`campaign_name`: string,

`campaign_group_id`: numeric string,

`campaign_group_name`: string,

`click_time`: timestamp,

`is_mobile_data_terms_signed`: bool,

`is_external`: bool,

`is_instagram`: bool,

`is_view_through`: bool,

`view_time`: timestamp,

`is_playable_ad`: bool,

`is_aaa_campaign`: bool,

`creative_id`: numeric string,

`engagement_type`: enum,

} Or Struct {

`success`: bool,

`drop_reason`: string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

## Updating

You can't perform this operation on this endpoint.