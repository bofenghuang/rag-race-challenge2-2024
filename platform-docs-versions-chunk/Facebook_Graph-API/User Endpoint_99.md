platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/live_videos/

### Parameters

| Parameter | Description |
| --- | --- |
| `broadcast_status`<br><br>list<enum {UNPUBLISHED, LIVE, LIVE\_STOPPED, PROCESSING, VOD, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_EXPIRED, SCHEDULED\_CANCELED}> | Allows you to specify what kind of live videos return. No value returns all status types |
| `source`[](#)<br><br>enum{target, owner} | Default value: `target`<br><br>Specifies what the source of the videos should be. 'target' gets videos broadcasted onto the user's timeline, 'owner' gets videos made by the user |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).