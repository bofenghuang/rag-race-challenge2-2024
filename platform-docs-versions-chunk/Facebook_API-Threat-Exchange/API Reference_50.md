platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptors


## Parameters

The following query parameters are available (bold params are required):

* **`access_token`** - The key for authenticating to the API, in the format <your-app-id>|<your-app-secret>. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
    
* `include_expired` - When set to true, the API can return data which has expired. Expired data is denoted by having the expire\_time field as non-zero and less than the current time.
    
* `limit` - Defines the maximum size of a page of results. The maximum is 1,000.
    
* `max_confidence` - Define the maximum allowed confidence value for the data returned.
    
* `min_confidence` - Define the minimum allowed confidence value for the data returned.
    
* `owner` - Comma-separated list of AppIDs of the person who submitted the data.
    
* `text` - Freeform text field with a value to search for. This can be a file hash or a string found in other fields of the objects.
    
* `review_status` - A given [ReviewStatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type)
    
* `share_level` - A given [ShareLevelType](https://developers.facebook.com/docs/threat-exchange/reference/apis/share-level-type)
    
* `sort_by` - Sort search results by RELEVANCE or by CREATE\_TIME. When sorting by RELEVANCE, your query will return results sorted by similarity against your text query.
    
* `status` - A given [StatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type)
    
* `strict_text` - When set to 'true', the API will not do approximate matching on the value in text
    
* `tags` - Comma-separated list of tags to filter results
    
* `tags_are_anded` - If omitted or set to `false`, with `tags=a,b` shows descriptors having tags `a` or `b`. If set to `true`, shows descriptors having tags `a` and `b`.
    
* `type` - The type of descriptor to search for (see [IndicatorTypes](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type/))
    
* `since` - Returns descriptors collected after a timestamp
    
* `until` - Returns descriptors collected before a timestamp
    
* `fields` - A list of fields to return in the response
    

Optional parameters for POST -- documented with examples [here](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fapi-reference-examples%2Fjava%2Fte-tag-query&h=AT3ji0eGSzoUG9rZjE916lRF6rRaLUv_HYOBTMvRkyGj44VBq99MBrI7a5P9EX2VQLdCMjutN2YgKEbatwfC00_ccpceFw2wKkAEK1ngDHEzDsJAjooVRCte62wAWeoyAYw9MXBZDqtOb-cf):

* `related_ids_for_upload`
    
* `related_triples_for_upload`
    

Example query for all IP addresses submitted by Facebook Administrator which contain the word "proxy":

https://graph.facebook.com/v2.8/threat\_descriptors?access\_token=555|asDF&amp;type=IP\_ADDRESS&amp;owner=820763734618599&amp;text=proxy

Data returned:

{
  "data": \[
    {
      "id": "600399050063019",
      "indicator": {
        "indicator": "52.68.54.232",
        "type": "IP\_ADDRESS",
        "id": "1117440484937537"
      },
      "owner": {
        "id": "820763734618599",
        "email": "threatexchange@support.facebook.com",
        "name": "Facebook Administrator"
      },
      "type": "IP\_ADDRESS",
      "raw\_indicator": "52.68.54.232",
      "description": "TOR Proxy IP Address",
      "status": "UNKNOWN"
    },
    ...
  \],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MjQZD"
    },
    "next": "https://graph.facebook.com/v2.8/threat\_descriptors?access\_token=555|1234&amp;pretty=0&amp;owner=820763734618599&amp;text=proxy&amp;type=IP\_ADDRESS&amp;limit=25&amp;after=MjQZD"
  },
}

The same query using a cURL:

curl -i -X GET \\
 "https://graph.facebook.com/v2.8/threat\_descriptors?type=IP\_ADDRESS&amp;owner=820763734618599&amp;text=proxy&amp;access\_token=555%7C1234"

The same query in Python:

import requests
import json
import ast
import urllib

app\_id = '555' # Replace this with your app ID
app\_secret = '1234' # Replace this with your app secret
type\_ = 'IP\_ADDRESS'
owner\_app\_id = 820763734618599
text = 'proxy'

query\_params = urllib.urlencode({
    'access\_token' : app\_id + '|' + app\_secret,
    'type' : type\_,
    'owner' : owner\_app\_id,
    'text' : text
    })

r = requests.get('https://graph.facebook.com/v2.8/threat\_descriptors?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))

The same query in Java:

import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class ThreatDescriptors {

    public final static void main(String\[\] args) throws Exception {
        String url = "https://graph.facebook.com/v2.8/threat\_descriptors?";
        String appID = "555"; // Replace this with your app ID
        String appSecret = "12345"; // Replace this with your app secret
        String type = "IP\_ADDRESS";
        String ownerAppID = "820763734618599";
        String text = "proxy";
        
        String query = String.format("access\_token=%s&amp;type=%s&amp;owner=%s&amp;text=%s",
                appID + "|" + appSecret,
                type,
                ownerAppID,
                text
                );
        URLConnection connection = new URL(url + query).openConnection();
        InputStream response = connection.getInputStream();
        System.out.print(convertStreamToString(response));
        response.close();
    }
    
    static String convertStreamToString(InputStream inputStream){
        Scanner scanner = new Scanner(inputStream).useDelimiter("\\\\A");
        return scanner.hasNext() ? scanner.next() : "";
    }
    
}

The same query in PHP:

<?php
  $appID = "555"; // Replace this with your AppID
  $appSecret = "1234"; // Replace this with your App Secret
  $type = 'IP\_ADDRESS';
  $text = 'proxy';
  $ownerAppID = "820763734618599";
  $access\_token = $appID . "|" . $appSecret;

  $ch = curl\_init();
  curl\_setopt($ch, CURLOPT\_URL,
    "https://graph.facebook.com/v2.8/threat\_descriptors?" .
    "access\_token=" . $access\_token .
    "&amp;type=" . $type .
    "&amp;owner=" . $ownerAppID .
    "&amp;text=" . $text);
  curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, 1);
  $response = curl\_exec($ch);
  $json = json\_encode(json\_decode($response), JSON\_PRETTY\_PRINT);
  print($json . PHP\_EOL);
  curl\_close($ch);
?>