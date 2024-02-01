platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/accounts/

### Parameters

| Parameter | Description |
| --- | --- |
| `type`<br><br>enum{test-users} | The type of user requested |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [TestAccount](https://developers.facebook.com/docs/graph-api/reference/test-account/) nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `access_token`<br><br>string | An access token that can be used to make API calls on behalf of this user<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |