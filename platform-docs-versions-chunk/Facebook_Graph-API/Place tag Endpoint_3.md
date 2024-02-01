platform: Facebook
topic: Graph-API
subtopic: Place tag Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Place tag Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/place-tag/

### Permissions

* A user access token with `user_tagged_places` permission is required to see any tags involving that person.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `id` | The ID of this place tag. | `string` |
| `created_time` | When the tag was created. | `datetime` |
| `place` | The Facebook Page representing the place. | [`Page`](https://developers.facebook.com/docs/graph-api/reference/page/) |

## Publishing

Use the [`/{user-id}/feed`](https://developers.facebook.com/docs/graph-api/reference/user/feed/) edge to create posts with place tagging.

## Deleting

You can't delete place tags, however if the original content that created the tag is removed, the place tag will also be removed.

## Updating

You can't update using this node.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)