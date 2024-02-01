platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-stream


## GET /track/:stream [¶](#get-track-stream- "Permalink to this headline")

Establishes a persistent connection to the PowerTrack data stream, through which the social data will be delivered.

**IMPORTANT:** After you establish the connection [see here](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data) for details on consuming streaming data.

|     |     |
| --- | --- |
| **Request Method** | HTTP GET |
| **Connection Type** | Keep-Alive  <br>  <br>This should be specified in the header of the request. |
| **URL** | Found on the stream's API Help page of your console dashboard, and resembles the following structure:  <br>  <br><br>[https://gnip-stream.twitter.com/stream/powertrack/accounts/](https://gnip-stream.twitter.com/stream/powertrack/accounts/){gnip\_account\_name}/publishers/twitter/{stream\_label}.json |
| **Compression** | Gzip. To connect to the stream using Gzip compression, simply send an Accept-Encoding header in the connection request. The header should look like the following:  <br>  <br>Accept-Encoding: gzip |
| **Character Encoding** | UTF-8 |
| **Response Format** | JSON. The header of your request should specify JSON format for the response. |
| **Rate Limit** | 60 requests per minute. |
| **Read Timeout** | Set a read timeout on your client, and ensure that it is set to a value beyond 30 seconds. |
| **Support for Tweet edits** | All Tweet objects will include Tweet edit metadata describing the Tweet's edit history. See the ["Edit Tweets" fundamentals page](https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets) for more details. |

  

#### Responses

The following responses may be returned by the API for these requests. Most error codes are returned with a string with additional details in the body. For non-200 responses, clients should attempt to reconnect.

| Status | Text | Description |
| --- | --- | --- |
| 200 | Success | The connection was successfully opened, and new activities will be sent through as they arrive. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 406 | Not Acceptable | Generally, this occurs where your client fails to properly include the headers to accept gzip encoding from the stream, but can occur in other circumstances as well.  <br>  <br>Will contain a JSON message similar to "This connection requires compression. To enable compression, send an 'Accept-Encoding: gzip' header in your request and be ready to uncompress the stream as it is read on the client end." |
| 429 | Rate Limited | Your app has exceeded the limit on connection requests. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/), contact support or emergency if unable to connect after 10 minutes. |

  

**Example curl Request**

The following example request is accomplished using cURL on the command line. However, note that these requests may also be sent with the programming language of your choice.

curl --compressed -v -uexample@customer.com "https://gnip-stream.twitter.com/stream/powertrack/accounts/:account\_name/publishers/twitter/:stream\_label.json"