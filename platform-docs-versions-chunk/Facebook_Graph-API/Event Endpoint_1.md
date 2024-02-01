platform: Facebook
topic: Graph-API
subtopic: Event Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Event Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/event/

# Event

Represents an [Event](https://www.facebook.com/help/572885262883136/).

### Limitations

Access to Events on [Users](https://developers.facebook.com/docs/graph-api/reference/user) and [Pages](https://developers.facebook.com/docs/graph-api/reference/page) is only available to Facebook Marketing Partners.

## Reading

Get fields and edges on an Event.

### Requirements

For Events on an [App](https://developers.facebook.com/docs/graph-api/reference/application):

* An App access token of an App that created the Event.

For Events on a [Group](https://developers.facebook.com/docs/graph-api/reference/group):

* A User access token of an Admin of the Event.
* The [Groups API](https://developers.facebook.com/docs/apps/review/feature#reference-GROUPS_ACCESS) feature.