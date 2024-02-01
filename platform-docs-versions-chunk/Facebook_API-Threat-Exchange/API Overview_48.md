platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/examples


## PHP

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.

<?php
$appID = "555"; // Replace this with your AppID
$appSecret = "1234"; // Replace this with your App Secret
$type = 'IP\_ADDRESS';
$text = 'proxy';
$access\_token = $appID . "|" . $appSecret;

$ch = curl\_init();
curl\_setopt($ch, CURLOPT\_URL,
"https://graph.facebook.com/v2.5/threat\_indicators?" .
"access\_token=" . $access\_token .
"&amp;type=" . $type .
"&amp;text=" . $text);
curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, 1);
$response = curl\_exec($ch);
$json = json\_encode(json\_decode($response), JSON\_PRETTY\_PRINT);
print($json . PHP\_EOL);
curl\_close($ch);
?>

Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.

<?php
$appID = "555"; // Replace this with your AppID
$appSecret = "1234"; // Replace this with your App Secret
$type = 'IP\_ADDRESS';
$text = 'proxy';
$ownerAppID = "820763734618599";
$access\_token = $appID . "|" . $appSecret;

$ch = curl\_init();
curl\_setopt($ch, CURLOPT\_URL,
"https://graph.facebook.com/v2.5/threat\_descriptors?" .
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