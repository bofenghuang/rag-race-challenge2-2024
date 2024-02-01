platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicators


## Parameters

The following query parameters are available (bold parameters are required):

* **`access_token`** - The key for authenticating to the API. It is a concatenation of &lt;your-app-id&gt;|&lt;your-app-secret&gt;. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
    
* `limit` - Defines the maximum size of a page of results. The maximum is 1,000.
    
* `text` - Freeform text field with a value to search for. This can be a file hash or a string found in other fields of the objects.
    
* `sort_order` - A given [SortOrderType](https://developers.facebook.com/docs/threat-exchange/reference/apis/sort-order-type)
    
* `sort_by` - Sort results by RELEVANCE or by CREATE\_TIME. When sorting by RELEVANCE, your query will return results sorted by similarity against your text query.
    
* `strict_text` - When set to 'true', the API will not do approximate matching on the value in text
    
* `threat_type` - The broad threat type the indicator is associated with (see [ThreatTypes](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-type/))
    
* `type` - The type of indicators to search for (see [IndicatorTypes](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type/))
    
* `since` - Returns indicators collected after a timestamp
    
* `until` - Returns indicators collected before a timestamp
    
* `fields` - A list of fields to return in the response
    

Example query for all malicious IP addresses that are proxies:

https://graph.facebook.com/v2.7/threat\_indicators?access\_token=555|aSdF123GhK&amp;type=IP\_ADDRESS&amp;text=proxy

The data returned by this API call changed in Platform version 2.4. Data returned in Platform v2.3:

{
  "data": \[
    {
      "added\_on": "2015-02-25T14:46:37+0000", 
      "confidence": 50, 
      "description": "Localhost IP", 
      "indicator": "127.0.0.1", 
      "severity": "INFO", 
      "share\_level": "GREEN", 
      "status": "NON\_MALICIOUS", 
      "type": "IP\_ADDRESS", 
      "threat\_types": \[
        "MALICIOUS\_IP"
      \], 
      "id": "804745332940593"
    }
  \], 
  "paging": {
    "cursors": {
      "before": "MA==", 
      "after": "MA=="
    }
  }
}

Data returned in Platforms v2.4 and above:

{
  "data": \[
    {
      "indicator": "77.2.132.202",
      "type": "IP\_ADDRESS",
      "id": "675010235935327"
    },
    ...
  \],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MjQZD"
    },
    "next": "https://graph.facebook.com/v2.7/threat\_indicators?access\_token=555|1234&amp;pretty=0&amp;text=proxy&amp;type=IP\_ADDRESS&amp;limit=25&amp;after=MjQZD"
  },
}

The same query using a cURL:

curl -i -X GET \\
 "https://graph.facebook.com/v2.7/threat\_indicators?type=IP\_ADDRESS&amp;text=proxy&amp;access\_token=555%7C1234"

The same query in Python:

import requests
import json
import ast
import urllib

app\_id = '555' # Replace this with your app ID
app\_secret = '1234' # Replace this with your app secret
type\_ = 'IP\_ADDRESS'
text = 'proxy'

query\_params = urllib.urlencode({
    'access\_token' : app\_id + '|' + app\_secret,
    'type' : type\_,
    'text' : text
    })

r = requests.get('https://graph.facebook.com/v2.7/threat\_indicators?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))

The same query in Java:

import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class ThreatIndicators {

    public final static void main(String\[\] args) throws Exception {
        String url = "https://graph.facebook.com/v2.7/threat\_indicators?";
        String appID = "5555"; // Replace this with your app ID
        String appSecret = "12345"; // Replace this with your app secret
        String type = "IP\_ADDRESS";
        String text = "proxy";
        
        String query = String.format("access\_token=%s&amp;type=%s&amp;text=%s",
                appID + "|" + appSecret,
                type,
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
  $access\_token = $appID . "|" . $appSecret;

  $ch = curl\_init();
  curl\_setopt($ch, CURLOPT\_URL,
    "https://graph.facebook.com/v2.7/threat\_indicators?" .
    "access\_token=" . $access\_token .
    "&amp;type=" . $type .
    "&amp;text=" . $text);
  curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, 1);
  $response = curl\_exec($ch);
  $json = json\_encode(json\_decode($response), JSON\_PRETTY\_PRINT);
  print($json . PHP\_EOL);
  curl\_close($ch);
?>