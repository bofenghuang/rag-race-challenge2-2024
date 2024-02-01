platform: Facebook
topic: Graph-API
subtopic: Url Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Url Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/url

### Query String Parameters

Include the following query string parameters to augment the request.

| Parameter | Description |
| --- | --- |
| `access_token`<br><br>Required<br><br>_string_ | An [access token](#). |
| `fields`<br><br>_string_ | A comma-separated list of fields you want to request. |
| `id`<br><br>Required<br><br>_string_ | The url to be updated. The url must be [encoded](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPercent-encoding&h=AT1XU2e0WbLjs6IvHgAvgp2e7jQGStA-SbhBDzACqmt3fTNpLGtnqaskfYDaEi_SZIe7_5NW-Yv2pLUFyCuM_tYJDeybUQO477HdtrDnGWJBfhqn4kJlw2JK2WmZzTGXkrfF8sJ4gDNjLVDL) so that it does not interfere with the `scrape` parameter. |
| `scrape`<br><br>Required<br><br>_boolean_ | Value must be `true`. |

#### Example Request

POST /{version}/?id={url}&scrape=true
Host: graph.facebook.com

#### Example Response

{
  "success": true
}