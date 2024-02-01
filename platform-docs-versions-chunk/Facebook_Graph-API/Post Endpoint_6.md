platform: Facebook
topic: Graph-API
subtopic: Post Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Post Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/post/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>token with structure: Post ID | The post ID. |
| `actions`<br><br>list | Action links |
| `admin_creator`<br><br>BusinessUser\|User\|Application | The admin creator of a Page Post. Only available if there exists more than one admin for the page. |
| `allowed_advertising_objectives`<br><br>list<string> | The only objectives under which this post can be advertised |
| `application`<br><br>[Application](https://developers.facebook.com/docs/graph-api/reference/application/) | Information about the app this post was published by. |
| `backdated_time`<br><br>datetime | The backdated time for backdate post. For regular post, this field will be set to null. |
| `call_to_action`<br><br>struct with keys: type, value | The call to action type used in any Page posts for mobile app engagement ads. |
| `can_reply_privately`<br><br>bool | Whether the page viewer can send a private reply to this post |
| `caption`<br><br>string | The caption of a link in the post (appears beneath the name). |
| `child_attachments`<br><br>list | Sub-shares of a multi-link share post |
| `comments_mirroring_domain`<br><br>string | If comments are being mirrored to an external site, this function returns the domain of that external site. |
| `coordinates`<br><br>struct with keys: checkin\_id, author\_uid, page\_id, target\_id, target\_href, coords, tagged\_uids, timestamp, message, target\_type | An array of information about the attachment to the post |
| `created_time`<br><br>datetime | The time the post was published, expressed as UNIX timestamp<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `description`<br><br>string | A description of a link in the post (appears beneath the caption). |
| `event`[](#)<br><br>[Event](https://developers.facebook.com/docs/graph-api/reference/event/) | If this Post has a place, the event associated with the place |
| `expanded_height`<br><br>unsigned int32 | An array of information about the attachment to the post |
| `expanded_width`<br><br>unsigned int32 | An array of information about the attachment to the post |
| `feed_targeting`<br><br>struct with keys: country, cities, regions, genders, age\_min, age\_max, education\_statuses, college\_years, relationship\_statuses, interests, interested\_in, user\_adclusters, locales, countries, geo\_locations, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, industries, politics, ethnic\_affinity, generation, fan\_of, relevant\_until\_ts | Object that controls news feed targeting for this post. Anyone in these groups will be more likely to see this post, others will be less likely, but may still see it anyway. Any of the targeting fields shown here can be used, none are required (applies to Pages only). |
| `from`<br><br>User\|Page | The ID of the user, page, group, or event that published the post |
| `full_picture`<br><br>string | If the photo's largest dimension exceeds 720 pixels, it is resized, with the largest dimension set to 720. |
| `height`<br><br>unsigned int32 | An array of information about the attachment to the post |
| `icon`<br><br>string | A link to an icon representing the type of this post. |
| `is_app_share`<br><br>bool | Whether or not the post references an app |
| `is_eligible_for_promotion`<br><br>bool | Whether the post is eligible for promotion. |
| `is_expired`<br><br>bool | Whether the post has expiration time that has passed |
| `is_hidden`<br><br>bool | Whether a post has been set to hidden |
| `is_inline_created`<br><br>bool | Returns True if the post was created inline when creating ads. |
| `is_popular`<br><br>bool | Whether the post is currently popular. Based on whether the total actions as a percentage of reach exceeds a certain threshold |
| `is_published`<br><br>bool | Indicates whether a scheduled post was published (applies to scheduled Page Post only, for users post and instanlty published posts this value is always true) |
| `is_spherical`<br><br>bool | Whether the post is a spherical video post |
| `link`<br><br>uri | A description of a link in the post (appears beneath the caption). |
| `message`<br><br>string | The message written in the post<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `message_tags`<br><br>list | Profiles mentioned or tagged in a message. This is an object with a unique key for each mention or tag in the message. |
| `multi_share_end_card`<br><br>bool | Whether display the end card for a multi-link share post |
| `multi_share_optimized`<br><br>bool | Whether automatically select the order of the links in multi-link share post when used in an ad |
| `name`<br><br>string | The name of the link. |
| `object_id`<br><br>string | The ID of any uploaded photo or video attached to the post. |
| `parent_id`<br><br>token with structure: Post ID | The ID of a parent post for this post, if it exists. For example, if this story is a 'Your Page was mentioned in a post' story, the parent\_id will be the original post where the mention happened |
| `permalink_url`<br><br>uri | The permanent static URL to the post on www.facebook.com. Example: https://www.facebook.com/FacebookforDevelopers/posts/10153449196353553 |
| `place`<br><br>[Place](https://developers.facebook.com/docs/graph-api/reference/place/) | ID of the place associated with the post |
| `privacy`<br><br>[Privacy](https://developers.facebook.com/docs/graph-api/reference/privacy/) | The privacy settings for a post |
| `promotable_id`[](#)<br><br>token with structure: Post ID | ID of post to use for promotion for stories that cannot be promoted directly |
| `properties`<br><br>list | A list of properties for any attached video, for example, the length of the video. |
| `scheduled_publish_time`<br><br>float | UNIX timestamp of the scheduled publish time for the post |
| `shares`<br><br>struct with keys: count | Number of times the post has been shared |
| `source`<br><br>string | A URL to any Flash movie or video file attached to the post. |
| `status_type`<br><br>string | Description of the type of a status update. |
| `story`<br><br>string | Text of stories not intentionally generated by users, such as those generated when two users become friends. You must have the "Include recent activity stories" migration enabled in your app to retrieve this field<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `story_tags`<br><br>list | The list of tags in the post description |
| `subscribed`<br><br>bool | Whether user is subscribed to the post |
| `target`[](#)<br><br>[Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) | The profile this was posted on if different from the author |
| `targeting`<br><br>struct with keys: country, cities, regions, zips, genders, college\_networks, work\_networks, age\_min, age\_max, education\_statuses, college\_years, college\_majors, political\_views, relationship\_statuses, interests, keywords, interested\_in, user\_clusters, user\_clusters2, user\_clusters3, user\_adclusters, excluded\_user\_adclusters, custom\_audiences, excluded\_custom\_audiences, locales, radius, connections, excluded\_connections, friends\_of\_connections, countries, excluded\_user\_clusters, adgroup\_id, user\_event, qrt\_versions, page\_types, user\_os, user\_device, action\_spec, action\_spec\_friend, action\_spec\_excluded, geo\_locations, excluded\_geo\_locations, targeted\_entities, conjunctive\_user\_adclusters, wireless\_carrier, site\_category, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, behaviors, travel\_status, industries, politics, markets, income, net\_worth, home\_type, home\_ownership, home\_value, ethnic\_affinity, generation, household\_composition, moms, office\_type, interest\_clusters\_expansion, dynamic\_audience\_ids, product\_audience\_specs, excluded\_product\_audience\_specs, exclusions, flexible\_spec, engagement\_specs, excluded\_engagement\_specs | Object that limited the audience for this content. Anyone not in these demographics will not be able to view this content. This will not override any Page-level demographic restrictions that may be in place. |
| `timeline_visibility`<br><br>string | Timeline visibility information of the post |
| `type`<br><br>string | A string indicating the object type of this post. |
| `updated_time`<br><br>datetime | The time the post was last updated, which occurs when a user comments on the post. |
| `via`<br><br>User\|Page | ID of the user or Page the post was shared from |
| `width`<br><br>unsigned int32 | An array of information about the attachment to the post |