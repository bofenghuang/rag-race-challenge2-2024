platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/connecting


## HTTP Error Codes

Most error codes are returned with a string with additional details. For all codes greater than 200, clients should wait before attempting another connection. See the Connecting section, above.

|     |     |     |
| --- | --- | --- |
| Status | Text | Description |
| **200** | **Success** | Self evident. |
| **401** | **Unauthorized** | HTTP authentication failed due to either:<br><br>* Invalid basic auth credentials, or an invalid OAuth request.<br>* Out-of-sync timestamp in your OAuth request (the response body will indicate this).<br>* Too many incorrect passwords entered or other login rate limiting. |
| **403** | **Forbidden** | The connecting account is not permitted to access this endpoint. |
| **404** | **Unknown** | There is nothing at this URL, which means the resource does not exist. |
| **406** | **Not Acceptable** | At least one request parameter is invalid. For example, the filter endpoint returns this status if:<br><br>* The track keyword is too long or too short.<br>* An invalid bounding box is specified.<br>* Neither the track nor follow parameter are specified.<br>* The follow user ID is not valid. |
| **413** | **Too Long** | A parameter list is too long. For example, the filter endpoint returns this status if:<br><br>* More track values are sent than the user is allowed to use.<br>* More bounding boxes are sent than the user is allowed to use.<br>* More follow user IDs are sent than the user is allowed to follow. |
| **416** | **Range Unacceptable** | For example, an endpoint returns this status if:<br><br>* A count parameter is specified but the user does not have access to use the count parameter.<br>* A count parameter is specified which is outside of the maximum/minimum allowable values. |
| **420** | **Rate Limited** | The client has connected too frequently. For example, an endpoint returns this status if:<br><br>* A client makes too many login attempts in a short period of time.<br>* Too many copies of an application attempt to authenticate with the same credentials. |
| **503** | **Service Unavailable** | A streaming server is temporarily overloaded. Attempt to make another connection, keeping in mind the connection attempt rate limiting and possible DNS caching in your client. |