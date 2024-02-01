platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks


### Challenge-Response Checks 

In order to verify that you are both the owner of the app and the webhook URL, Twitter will perform a Challenge-Response Check (CRC), which is not to be confused with a cyclic redundancy check. When a CRC is sent, Twitter will make a GET request of your web app with a ;_`crc_token`_ parameter. When that request is received, your web app needs to build an encrypted `response_token` based on the _`crc_token`_ parameter and your app's Consumer Secret (details below). The response\_token must be encoded in JSON (see example below) and returned within three seconds. When successful, a webhook `id` will be returned. 

A CRC will be sent when you register your webhook URL, so implementing your CRC response code is a fundamental first step. Once your webhook is established, Twitter will trigger a CRC roughly every 24 hours from the last time we received a successful response. Your app can also trigger a CRC when needed by making a PUT request with your webhook `id`. Triggering a CRC is useful as you develop your webhook application, after deploying new code and restarting your service. 

The _`crc_token`_ should be expected to change for each incoming CRC request and should be used as the message in the calculation, where your Consumer Secret is the key.

In the event that the response is not posted within 3 seconds or becomes invalid, events will cease to be sent to the registered webhook.

#### The CRC request will occur:  

* When a webhook URL is registered.
* Approximately _hourly_ to validate your webhook URL.
* You can manually trigger a CRC by making a PUT request. As you develop your webhook client, you should plan on manually triggering the CRC as you develop your CRC response.   
     

#### Response requirements:

* A base64 encoded HMAC SHA-256 hash created from the `crc_token` and your app Consumer Secret
* Valid response\_token and JSON format.
* Latency less than 3 seconds.
* 200 HTTP response code.  
     

#### Language-specific HMAC libraries:

* [Java/Scala](https://docs.oracle.com/javase/8/docs/api/index.html?javax/crypto/Mac.html)
* [Ruby](http://ruby-doc.org/stdlib-2.1.0/libdoc/openssl/rdoc/OpenSSL/HMAC.html)
* [Node.js](https://nodejs.org/api/crypto.html#crypto_class_hmac)
* [Python](https://docs.python.org/2/library/hmac.html) 

#### Example response token generation in Python:

The following defines a route in a Python 2.7 Flask webapp that will respond to the challenge response check correctly.

import base64
import hashlib
import hmac
import json