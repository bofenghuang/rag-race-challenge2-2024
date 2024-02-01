platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/secure-requests

### Add the Proof

You add the result as an `appsecret_proof` parameter to each call you make:

curl \\
  -F 'access\_token=<access\_token>' \\
  -F 'appsecret\_proof=<app secret proof>' \\
  -F 'batch=\[{"method":"GET", "relative\_url":"me"},{"method":"GET", "relative\_url":"me/friends?limit=50"}\]' \\
  https://graph.facebook.com

### Require the Proof

In the **Settings > Advanced** section of your app dashboard in the **Security** section, you enable **Require App Secret**. When this is enabled, we will only allow API calls that include the `appsecret_proof`.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)