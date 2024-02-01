platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/examples


## Java

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.

import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class ThreatIndicators {

public final static void main(String\[\] args) throws Exception {
String url = "https://graph.facebook.com/v2.4/threat\_indicators?";
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

Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.

import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class ThreatDescriptors {

public final static void main(String\[\] args) throws Exception {
String url = "https://graph.facebook.com/v2.4/threat\_descriptors?";
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