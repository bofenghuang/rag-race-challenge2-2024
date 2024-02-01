platform: Facebook
topic: Graph-API
subtopic: Milestone Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Milestone Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/milestone

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `id` | The ID of a milestone event | `string` |
| `title` | The title of the milestone | `string` |
| `from` | The Page that posted the milestone. | [`Page`](https://developers.facebook.com/docs/graph-api/reference/page/) |
| `description` | The description of the milestone | `string` |
| `created_time` | The creation time of the milestone | `datetime` |
| `updated_time` | The update time of the milestone | `datetime` |
| `start_time` | The start time of the milestone | `datetime` |
| `end_time` | The end time of the milestone. Page milestones have the same start and end time | `datetime` |

## Creating

You can't perform this operation on this endpoint.

Use the [`/{page-id}/milestones`](https://developers.facebook.com/docs/graph-api/reference/page/milestones/) endpoint to create new milestones for a Page.

## Deleting