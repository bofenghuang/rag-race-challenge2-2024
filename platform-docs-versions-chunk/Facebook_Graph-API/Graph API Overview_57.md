platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/versioning

### What happens if I don't specify a version for an API?

We refer to an API call made without specifying a version as an **unversioned** call. For example, let's say the current version is v4.0. The call is as follows:

curl -i -X "https://graph.facebook.com/v4.0/{my-user-id}&access\_token={access-token}"

The same unversioned call is as follows:

curl -i -X "https://graph.facebook.com/{my-user-id}&access\_token={access-token}"

An unversioned call uses the version set in the app dashboard **Upgrade API Version** card under **Settings > Advanced**. In following example, the version set in the app dashboard is v2.10 and the unversioned call is equivalent to:

curl -i -X "https://graph.facebook.com/v2.10/{my-user-id}&access\_token={access-token}"

We recommend you always specify the version where possible.

#### Limitations

* You can not make unversioned API calls to the Facebook JavaScript SDK.