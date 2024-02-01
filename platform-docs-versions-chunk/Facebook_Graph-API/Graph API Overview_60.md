platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/versioning

### Social Plugins

If you're using the HTML5 or xfbml versions of [our social plugins](https://developers.facebook.com/docs/plugins/), the version rendered will be determined by the version specified when you're [initialising the JavaScript SDK](#jssdk).

If you're inserting an iframe or plain link version of one of our plugins, you'd prepend the version number to the source path of the plugin:

<iframe
  src="//www.facebook.com/`v19.0`/plugins/like.php?href=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;width&amp;layout=standard&amp;action=like&amp;show\_faces=true&amp;share=true&amp;height=80&amp;appId=634262946633418" 
  scrolling="no" 
  frameborder="0" 
  style="border:none; overflow:hidden; height:80px;" 
  allowTransparency="true">
</iframe>

## Making Versioned Requests from SDKs

If you're using the Facebook SDK for iOS, Android or JavaScript, making versioning calls is largely automatic. Note that this is distinct from each SDKs own versioning system.