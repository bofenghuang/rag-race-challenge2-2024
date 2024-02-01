platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/versioning

### Can my app make calls to versions older than the current version?

You can specify older versions in your API calls as long as they are available and your app has made calls to that version. For example, if your app was created after v2.0 was released and makes calls using v2.0, it will be able to make calls to v2.0 until the version expires even after newer versions have been released. If you created your app after v2.0 but did not make any calls until v2.2, your app will not be able to make calls using v2.0 or to v2.1. It will only be able to make calls using v2.2 and newer versions.

### Marketing API Versioning

The [Marketing API](https://developers.facebook.com/docs/marketing-apis) has its own versioning scheme. Both version numbers and their schedules are different from the Graph API's state of things.

[Learn more about Marketing API Versioning](https://developers.facebook.com/docs/marketing-api/versions)

## Making Versioned Requests