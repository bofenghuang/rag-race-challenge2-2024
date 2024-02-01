platform: Facebook
topic: Graph-API
subtopic: Photo Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Photo Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/photo/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The photo ID |
| `album`<br><br>[Album](https://developers.facebook.com/docs/graph-api/reference/album/) | The album this photo is in |
| `alt_text`<br><br>string | Accessible alternative description for an image |
| `alt_text_custom`<br><br>string | User provided accessible alternative description for an image |
| `backdated_time`<br><br>datetime | A user-specified time for when this object was created |
| `backdated_time_granularity`<br><br>enum | How accurate the backdated time is |
| `can_backdate`<br><br>bool | Indicates whether the viewer can backdate the photo |
| `can_delete`<br><br>bool | Indicates whether the viewer can delete the photo |
| `can_tag`<br><br>bool | Indicates whether the viewer can tag the photo |
| `created_time`<br><br>datetime | The time this photo was published<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `event`[](#)<br><br>[Event](https://developers.facebook.com/docs/graph-api/reference/event/) | If this object has a place, the event associated with the place |
| `from`<br><br>User\|Page | The profile (user or page) that uploaded this photo |
| `height`<br><br>unsigned int32 | The height of this photo in pixels |
| `icon`<br><br>string | The icon that Facebook displays when photos are published to News Feed |
| `images`<br><br>[list<PlatformImageSource>](https://developers.facebook.com/docs/graph-api/reference/platform-image-source/) | The different stored representations of the photo. Can vary in number based upon the size of the original photo. |
| `link`<br><br>string | A link to the photo on Facebook |
| `name`<br><br>string | The user-provided caption given to this photo. Corresponds to `caption` when creating photos<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `name_tags`<br><br>[list<EntityAtTextRange>](https://developers.facebook.com/docs/graph-api/reference/entity-at-text-range/) | An array containing an array of objects mentioned in the name field which contain the id, name, and type of each object as well as the offset and length which can be used to match it up with its corresponding string in the name field |
| `page_story_id`<br><br>string | ID of the page story this corresponds to. May not be on all photos. Applies only to published photos |
| `place`<br><br>[Place](https://developers.facebook.com/docs/graph-api/reference/place/) | Place info |
| `position`<br><br>unsigned int32 | Deprecated. Returns 0<br><br>Deprecated |
| `source`<br><br>string | Deprecated. Use `images` instead<br><br>Deprecated |
| `target`<br><br>[Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) | The target this photo is published to |
| `updated_time`<br><br>datetime | The last time the photo was updated |
| `webp_images`<br><br>[list<PlatformImageSource>](https://developers.facebook.com/docs/graph-api/reference/platform-image-source/) | The different stored representations of the photo in webp format. Can vary in number based upon the size of the original photo. |
| `width`<br><br>unsigned int32 | The width of this photo in pixels |