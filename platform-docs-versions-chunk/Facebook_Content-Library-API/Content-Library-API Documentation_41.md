platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-events

## Recurring events

Recurring events have a parent event to which all instances of the recurring event are associated by way of the `parent_event_id`. The set of fields returned for an event search differs depending on whether the event returned is a parent or an instance (child) of the recurring event. Start and end times, for example, are specific to instances of the recurring event. The following table summarizes the differences:

| Event type | Fields returned | Fields not returned |
| --- | --- | --- |
| Recurring event (the "parent" event) (event\_type=`recurring`) | `recurring_event_ids` | `attending_count`<br><br>`declined_count`<br><br>`interested_count`<br><br>`event_start_time`<br><br>`event_end_time`<br><br>`parent_event_id` |
| Instance of recurring (the "child" event) (event\_type=`instance_of_recurring`) | `attending_count`<br><br>`declined_count`<br><br>`interested_count`<br><br>`event_start_time`<br><br>`event_end_time`<br><br>`parent_event_id` | `recurring_event_ids` |