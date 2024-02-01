platform: Facebook
topic: Graph-API
subtopic: Group message Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Group message Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/group-message/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>token with structure: Post ID | id  |
| `actions`<br><br>list | actions |
| `admin_creator`<br><br>BusinessUser\|User\|Application | admin\_creator |
| `allowed_advertising_objectives`<br><br>list<string> | allowed\_advertising\_objectives |
| `application`<br><br>[Application](https://developers.facebook.com/docs/graph-api/reference/application/) | application |
| `backdated_time`<br><br>datetime | backdated\_time |
| `call_to_action`<br><br>struct with keys: type, value | call\_to\_action |
| `can_reply_privately`<br><br>bool | can\_reply\_privately |
| `caption`<br><br>string | caption |
| `child_attachments`<br><br>list | child\_attachments |
| `comments_mirroring_domain`<br><br>string | comments\_mirroring\_domain |
| `coordinates`<br><br>struct with keys: checkin\_id, author\_uid, page\_id, target\_id, target\_href, coords, tagged\_uids, timestamp, message, target\_type | coordinates |
| `created_time`<br><br>datetime | created\_time<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `description`<br><br>string | description |
| `event`[](#)<br><br>[Event](https://developers.facebook.com/docs/graph-api/reference/event/) | event |
| `expanded_height`<br><br>unsigned int32 | expanded\_height |
| `expanded_width`<br><br>unsigned int32 | expanded\_width |
| `feed_targeting`<br><br>struct with keys: country, cities, regions, genders, age\_min, age\_max, education\_statuses, college\_years, relationship\_statuses, interests, interested\_in, user\_adclusters, locales, countries, geo\_locations, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, industries, politics, ethnic\_affinity, generation, fan\_of, relevant\_until\_ts | feed\_targeting |
| `from`<br><br>User\|Page | from |
| `full_picture`<br><br>string | full\_picture |
| `height`<br><br>unsigned int32 | height |
| `icon`<br><br>string | icon |
| `is_app_share`<br><br>bool | is\_app\_share |
| `is_eligible_for_promotion`<br><br>bool | is\_eligible\_for\_promotion |
| `is_expired`<br><br>bool | is\_expired |
| `is_hidden`<br><br>bool | is\_hidden |
| `is_inline_created`<br><br>bool | is\_inline\_created |
| `is_popular`<br><br>bool | is\_popular |
| `is_published`<br><br>bool | is\_published |
| `is_spherical`<br><br>bool | is\_spherical |
| `link`<br><br>uri | link |
| `message`<br><br>string | message<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `message_tags`<br><br>list | message\_tags |
| `multi_share_end_card`<br><br>bool | multi\_share\_end\_card |
| `multi_share_optimized`<br><br>bool | multi\_share\_optimized |
| `name`<br><br>string | name |
| `object_id`<br><br>string | object\_id |
| `parent_id`<br><br>token with structure: Post ID | parent\_id |
| `permalink_url`<br><br>uri | permalink\_url |
| `place`<br><br>[Place](https://developers.facebook.com/docs/graph-api/reference/place/) | place |
| `privacy`<br><br>[Privacy](https://developers.facebook.com/docs/graph-api/reference/privacy/) | privacy |
| `promotable_id`[](#)<br><br>token with structure: Post ID | promotable\_id |
| `properties`<br><br>list | properties |
| `scheduled_publish_time`<br><br>float | scheduled\_publish\_time |
| `shares`<br><br>struct with keys: count | shares |
| `source`<br><br>string | source |
| `status_type`<br><br>string | status\_type |
| `story`<br><br>string | story<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `story_tags`<br><br>list | story\_tags |
| `subscribed`<br><br>bool | subscribed |
| `target`[](#)<br><br>[Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) | target |
| `targeting`<br><br>struct with keys: country, cities, regions, zips, genders, college\_networks, work\_networks, age\_min, age\_max, education\_statuses, college\_years, college\_majors, political\_views, relationship\_statuses, interests, keywords, interested\_in, user\_clusters, user\_clusters2, user\_clusters3, user\_adclusters, excluded\_user\_adclusters, custom\_audiences, excluded\_custom\_audiences, locales, radius, connections, excluded\_connections, friends\_of\_connections, countries, excluded\_user\_clusters, adgroup\_id, user\_event, qrt\_versions, page\_types, user\_os, user\_device, action\_spec, action\_spec\_friend, action\_spec\_excluded, geo\_locations, excluded\_geo\_locations, targeted\_entities, conjunctive\_user\_adclusters, wireless\_carrier, site\_category, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, behaviors, travel\_status, industries, politics, markets, income, net\_worth, home\_type, home\_ownership, home\_value, ethnic\_affinity, generation, household\_composition, moms, office\_type, interest\_clusters\_expansion, dynamic\_audience\_ids, product\_audience\_specs, excluded\_product\_audience\_specs, exclusions, flexible\_spec, engagement\_specs, excluded\_engagement\_specs | targeting |
| `timeline_visibility`<br><br>string | timeline\_visibility |
| `type`<br><br>string | type |
| `updated_time`<br><br>datetime | updated\_time |
| `via`<br><br>User\|Page | via |
| `width`<br><br>unsigned int32 | width |