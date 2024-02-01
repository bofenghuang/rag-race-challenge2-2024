platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/integrate


## Working with resumable uploads

When using the Batch compliance endpoints, developers can batch upload large amounts of Twitter data and understand what action is needed to ensure that their datasets reflect user intent and the current state of the content on Twitter. Uploading large amounts of data to a remote server is a relatively straightforward operation when systems and connectivity are stable and reliable. However, this may not always be the case. Some environments may impose a connection timeout, effectively cutting the connection between your app and the upload server after a set amount of time; you may also encounter connection issues, for example when trying to upload a large file from your laptop over a wi-fi connection. In these circumstances, it’s desirable to upload smaller portions of that file at a time, rather than having one single continuous connection.

Twitter’s batch compliance endpoints rely on Google Cloud Storage to process large files. This type of storage is optimized for various applications; Cloud Storage supports a technique to manage large files called resumable uploads.

If the upload goes wrong at any point, Google Cloud Storage is able to resume the operation from where it was left off.