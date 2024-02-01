platform: X
topic: Twitter-API-Enterprise
subtopic: Compliance Firehose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Compliance Firehose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/api-reference/compliance-firehose


## GET /compliance/:stream [¶](#get-compliance-stream- "Permalink to this headline")

Establishes a persistent connection to the Compliance firehose data stream, through which the compliance events will be delivered.

|     |     |
| --- | --- |
| **Request Method** | HTTP GET |
| **Connection Type** | Keep-Alive |
| **URL** | Found on the stream's API Help page of your dashboard, and resembles the following structure:  <br>  <br><br>[https://gnip-stream.twitter.com/stream/compliance/accounts/:account\_name/publishers/twitter/:stream\_label.json?partition=1](https://gnip-stream.twitter.com/stream/compliance/accounts/:account_name/publishers/twitter/:stream_label.json?partition=1)<br><br>**Note:** The "partition" parameter is required. You will need to connect to all 8 partitions, each containing 12.5% of the total volume, to consume the full stream. |
| **Compression** | Gzip. To connect to the stream using Gzip compression, simply send an Accept-Encoding header in the connection request. The header should look like the following:  <br>  <br>Accept-Encoding: gzip |
| **Character Encoding** | UTF-8 |
| **Response Format** | JSON. The header of your request should specify JSON format for the response. |
| **Rate Limit** | 10 requests per 60 seconds. |
| **Read Timeout** | Set a read timeout on your client, and ensure that it is set to a value beyond 30 seconds. |
| **Support for Tweet edits** | All Tweet edits trigger a "tweet\_edit" Compliance event. See the [Compliance Data Objects](https://developer.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/guides/compliance-data-objects) documentation for more details. |

**Example Curl Request**

The following example request is accomplished using cURL on the command line:

curl --compressed -v -uexample@customer.com "https://gnip-stream.twitter.com/stream/compliance/accounts/:account\_name/publishers/twitter/:stream\_label.json?partition=1"

_Note:_ the above request is only connecting to `partition=1` of the Compliance firehose - you'll need to connect to all 8 partitions to consume the entirety of this stream.