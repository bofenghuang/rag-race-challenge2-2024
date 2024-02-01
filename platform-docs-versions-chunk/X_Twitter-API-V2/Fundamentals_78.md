platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/pagination


### Pagination example

Here, there are three pages of results because max\_results is set to 100 and there are a total of ~295 Tweets created by user ID 2244994945 (@TwitterDev) between January 1st, 2019 at 17:00:00 UTC and December 12th at 00:00:00 UTC. The first Tweet on the first page (1337498609819021312) is the most recent, and the last Tweet on the third page of results (1082718487011885056) is the oldest.  
 

#### Initial request

      `https://api.twitter.com/2/users/2244994945/tweets?tweet.fields=created_at&max_results=100&start_time=2019-01-01T17:00:00Z&end_time=2020-12-12T01:00:00Z`
    

#### Sequence

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|     | **First Request** | **Second page** | **Third page** | **Fourth page** |
| **Request Parameters** | max\_results\=100<br><br>tweet.fields\=created\_at<br><br>start\_time\=2019-01-01T17:00:00Z<br><br>end\_time\=2020-12-12T01:00:00Z | max\_results\=100<br><br>tweet.fields\=created\_at<br><br>start\_time\=2019-01-01T17:00:00Z<br><br>end\_time\=2020-12-12T01:00:00Z<br><br>pagination\_token\=7140w | max\_results\=100<br><br>tweet.fields\=created\_at<br><br>start\_time\=2019-01-01T17:00:00Z<br><br>end\_time\=2020-12-12T01:00:00Z<br><br>pagination\_token\=7140k9 | max\_results\=100<br><br>tweet.fields\=created\_at<br><br>start\_time\=2019-01-01T17:00:00Z<br><br>end\_time\=2020-12-12T01:00:00Z<br><br>pagination\_token\=71408hi |
| **Response** | {<br>  "data": \[<br>    {<br>      "created\_at": "2020-12-11T20:44:52.000Z",<br>      "id": "1337498609819021312",<br>      "text": "Thanks to everyone who tuned in today..."<br>    },<br>    .<br>    .<br>    .<br>   {<br>      "created\_at": "2020-05-06T17:24:31.000Z",<br>      "id": "1258085245091368960",<br>      "text": "It’s now easier to understand Tweet impact..."<br>    }<br>  \],<br>  "meta": {<br>    "oldest\_id": "1258085245091368960",<br>    "newest\_id": "1337498609819021312",<br>    "result\_count": 100,<br>    "next\_token": "7140w"<br>  }<br>} | {<br>  "data": \[<br>    {<br>      "created\_at": "2020-04-29T17:01:44.000Z",<br>      "id": "1255542797765013504",<br>      "text": "Our developer community is full of inspiring ideas..."<br>    },<br>    .<br>    .<br>    .<br>    {<br>      "created\_at": "2019-11-21T16:17:23.000Z",<br>      "id": "1197549579035496449",<br>      "text": "Soon, we'll be releasing tools in..."<br>    }<br>  \],<br>  "meta": {<br>    "oldest\_id": "1197549579035496449",<br>    "newest\_id": "1255542797765013504",<br>    "result\_count": 100,<br>    "next\_token": "7140k9",<br>    "previous\_token": "77qp8"<br>  }<br>} | {<br>  "data": \[<br>    {<br>      "created\_at": "2019-11-21T16:17:23.000Z",<br>      "id": "1197549578418941952",<br>      "text": "We know that some people who receive a large volume of replies may..."<br>    },<br>    .<br>    .<br>    .<br>    { <br>      "created\_at": "2019-01-08T19:19:37.000Z",<br>      "id": "1082718487011885056",<br>      "text": "Updates to Grid embeds..."<br>    }<br>  \],<br>  "meta": {<br>    "oldest\_id": "1082718487011885056",<br>    "newest\_id": "1197549578418941952",<br>    "result\_count": 95,<br>    "next\_token": "71408hi",<br>    "previous\_token": "77qplte"<br>  }<br>} | {<br> "meta": {<br>    "result\_count": 0,<br>    "previous\_token": "77qpw8l"<br>  }<br>} |
| **Actions to take for next request** | To get the next page, take the next\_token value directly from the response (7140w) and set it as the pagination\_token for the next request call. | To continue to get all results: take the next\_token value directly from the response (7140k9) and set it as the pagination\_token for the next request call.  <br>  <br>  <br>To traverse to previous page: take the previous\_token value directly from the response (77qp8) and set it as the pagination\_token for the next request call. | To continue to get all results: take the next\_token value directly from the response (71408hi) and set it as the pagination\_token for the next request call.  <br>  <br>  <br>To traverse to previous page: take the previous\_token value directly from the response (77qplte) and set it as the pagination\_token for the next request call. | Note that there is no next\_token, which indicates that all results have been received.  <br>  <br>  <br>To traverse to previous page: take the previous\_token value directly from the response (77qpw8l) and set it as the pagination\_token for the next request call. |