platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/webhook-validation?context=linkedin%2Fcontext


## Requirements for Processing Notifications

Upon receiving notifications from LinkedIn, your webhook must fulfill the following requirements:

#### Verify the integrity of the push event and prevent malicious entities from impersonating LinkedIn as the sender

The POST request sent by LinkedIn will include a header called `X-LI-Signature`. The value of this header is the HMACSHA256 hash of the JSON-encoded string representation of the POST body prefixed by `hmacsha256=` and it is computed using your app’s clientSecret. On receiving the push event, you must compute the signature on the POST body prefixed by `hmacsha256=` using the HMACSHA256 hashing algorithm and your clientSecret. Discard the event if your computed value does not match the value sent in the `X-LI-Signature` header.

#### Deduplicate notifications

A notification can occasionally be delivered multiple times to your webhook. Your webhook must be able to deduplicate notifications using the Notification ID included in the payload.

#### Respond with an HTTP response

For each notification delivered to your webhook, it must return a 2xx HTTP status code to indicate successful delivery of the notification to your webhook. Any other response code returned will be treated by LinkedIn as a failure.

#### Test with lambda/serverless functions on a cloud provider

We recommend testing webhooks processing using lambda/serverless functions on a cloud provider.

Note

ngrok URIs are not supported.