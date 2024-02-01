platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities


### Photo Media URL Formatting

Photo media on Twitter can be loaded in different sizes.  It is best to load the smallest size image that is larger enough to fit into a particular image viewport.  To load different sizes, the [Size Object](#size) and [media\_url](#media) (or [media\_url\_https](#media)) need to be combined in a particular format.  We'll use the [media entity](#entitiesobject) example object already provided for our example in constructing a photo media URL.

The `media_url` or `media_url_https` on their own can be loaded, which will result in the medium variant being loaded by default.  It is preferable, however, to provide a fully formatted photo media URL when possible.  

There are three parts of a photo media URL:

|     |     |
| --- | --- |
| Base URL | The base URL is the media URL without the file extension.<br><br>For example:  <br><br>"media\_url\_https": "https://pbs.twimg.com/media/DOhM30VVwAEpIHq.jpg",<br><br>The base URL is then:  <br><br>_https://pbs.twimg.com/media/DOhM30VVwAEpIHq_ |
| Format | The format is the type of photo the image is formatted as.  Possible formats are _jpg_ or _png_, which is provided as the extension of the media URL.<br><br>For example:  <br><br>"media\_url\_https": "https://pbs.twimg.com/media/DOhM30VVwAEpIHq.jpg",<br><br>The format is then: _jpg_ |
| Name | The name is the field name of the size to load.<br><br>For example:<br><br>{  <br> "sizes": {  <br>   "thumb": {  <br>     "h": 150,  <br>     "resize": "crop",  <br>     "w": 150  <br>   },  <br>   "large": {  <br>     "h": 1366,  <br>     "resize": "fit",  <br>     "w": 2048  <br>   },  <br>   "medium": {  <br>     "h": 800,  <br>     "resize": "fit",  <br>     "w": 1200  <br>   },  <br>   "small": {  <br>     "h": 454,  <br>     "resize": "fit",  <br>     "w": 680  <br>   }  <br> }  <br>}<br><br>The name when loading the large-sized photo would be: _large_ |

We take these three parts (base URL, format and name) and combine them into the photo media URL to load.  There are 2 formats for loading images this way, _legacy_ and _modern_.  All image loads should stop using the _legacy_ format and use the _modern_ format.  Using the _modern_ format will result in better CDN hit rate for the caller, thus improving load latencies by being less likely to have to generate and load the media from the Data Center.

|     |     |
| --- | --- |
| Legacy format | The legacy format is deprecated.  Photo media loads should all move to the modern format.<br><br>_<base\_url>.<format>:<name>_  <br><br>For example:  <br><br>_https://pbs.twimg.com/media/DOhM30VVwAEpIHq.jpg:large  <br>_ |
| Modern format | The modern format for loading photos was established at Twitter in 2015 and has been defacto since 2017.  All photo media loads should move to this format.<br><br>_<base\_url>?format=<format>&name=<name>_  <br><br>For example:  <br><br>_https://pbs.twimg.com/media/DOhM30VVwAEpIHq?format=jpg&name=large  <br>_<br><br>Note: the items in the query string for the photo media URL are in alphabetical order.  If media loading were to add any additional query items, alphabetical ordering would continue to be necessary.  For example, if there was the hypothetical new query item called _preferred\_format_, it would go after _format_ and _name_ in the query string. |