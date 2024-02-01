platform: Facebook
topic: Graph-API
subtopic: Event Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Event Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/event/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The event ID |
| `attending_count`[](#)<br><br>int32 | Number of people attending the event |
| `can_guests_invite`<br><br>bool | Can guests invite friends. Requires an access token of an Admin of the Event |
| `category`[](#)<br><br>enum {CLASSIC\_LITERATURE, COMEDY, CRAFTS, DANCE, DRINKS, FITNESS\_AND\_WORKOUTS, FOODS, GAMES, GARDENING, HEALTH\_AND\_MEDICAL, HEALTHY\_LIVING\_AND\_SELF\_CARE, HOME\_AND\_GARDEN, MUSIC\_AND\_AUDIO, PARTIES, PROFESSIONAL\_NETWORKING, RELIGIONS, SHOPPING\_EVENT, SOCIAL\_ISSUES, SPORTS, THEATER, TV\_AND\_MOVIES, VISUAL\_ARTS} | The category of the event |
| `cover`<br><br>[CoverPhoto](https://developers.facebook.com/docs/graph-api/reference/cover-photo/) | Cover picture |
| `created_time`<br><br>datetime | created\_time |
| `declined_count`[](#)<br><br>int32 | Number of people who declined the event |
| `description`<br><br>string | Long-form description<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `discount_code_enabled`<br><br>bool | Is discount code enabled for this event |
| `end_time`<br><br>string | End time, if one has been set<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `event_times`<br><br>list<ChildEvent> | Array of times of a multi-instance event<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `guest_list_enabled`<br><br>bool | Can see guest list. Requires an access token of an Admin of the Event |
| `interested_count`[](#)<br><br>int32 | Number of people interested in the event |
| `is_canceled`<br><br>bool | Whether or not the event has been marked as canceled |
| `is_draft`<br><br>bool | Whether the event is in draft mode or published. Requires an access token of an Admin of the Event |
| `is_online`<br><br>bool | Whether the event is online or not. Required to pass the 'address' (city name) parameter for online events. |
| `is_page_owned`<br><br>bool | Whether the event is created by page or not |
| `maybe_count`[](#)<br><br>int32 | Number of people who maybe going to the event |
| `name`<br><br>string | Event name<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `noreply_count`[](#)<br><br>int32 | Number of people who did not reply to the event |
| `online_event_format`<br><br>enum {messenger\_room, third\_party, fb\_live, other, none} | Type of online event - Live, Link or Other |
| `online_event_third_party_url`<br><br>string | Third party streaming url associated with Link events |
| `owner` | The profile that created the event |
| `place`[](#)<br><br>[Place](https://developers.facebook.com/docs/graph-api/reference/place/) | Event Place information<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `scheduled_publish_time`<br><br>string | Time when event is scheduled to be published |
| `start_time`<br><br>string | Start time<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `ticket_uri`<br><br>string | The link users can visit to buy a ticket to this event |
| `ticket_uri_start_sales_time`<br><br>string | Time when tickets go on sale |
| `ticketing_privacy_uri`<br><br>string | URI to seller's privacy policy for ticket purchases |
| `ticketing_terms_uri`<br><br>string | URI to seller's terms of service for ticket purchases |
| `timezone`<br><br>enum | Timezone |
| `type`[](#)<br><br>enum {private, public, group, community, friends, work\_company} | The type of the event |
| `updated_time`<br><br>datetime | Last update time (ISO 8601 formatted) |