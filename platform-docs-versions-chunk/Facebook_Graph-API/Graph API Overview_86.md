platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/batch-requests


## Upload Binary Data

You can upload multiple binary items as part of a batch call. In order to do this, you need to add all the binary items as multipart/mime attachments to your request, and need each operation to reference its binary items using the `attached_files` property in the operation. The `attached_files` property can take a comma separated list of attachment names in its value.

The following example shows how to upload 2 photos in a single batch call:

curl 
     -F 'access\_token=…' \\
     -F 'batch=\[{"method":"POST","relative\_url":"me/photos","body":"message=My cat photo","attached\_files":"file1"},{"method":"POST","relative\_url":"me/photos","body":"message=My dog photo","attached\_files":"file2"},\]' \\
     -F 'file1=@cat.gif' \\
     -F 'file2=@dog.jpg' \\
    https://graph.facebook.com

\-->

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)