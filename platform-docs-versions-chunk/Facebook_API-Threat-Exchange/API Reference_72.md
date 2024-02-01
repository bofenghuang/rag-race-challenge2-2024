platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/editing

## Using the API, option 1

In this example, we are updating the description field of [ThreatDescriptor](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor) object with ID `3047058802049882`:

curl -s -X POST \\
'https://graph.facebook.com/v4.0/3047058802049882/'\\
'?access\_token=REDACTED'\\
'&description=Updating+description'

Data returned:

{
"success": true
}

## Using the API, option 2

You can use the same API call as in [Submitting Data](https://developers.facebook.com/docs/threat-exchange/reference/submitting).

* If you do that -- resubmit data with the same indicator-type and indicator-text, but different values for other fields -- the same threat descriptor will be edited.
    
* It will insist that you pass it all the minimum parameters necessary for creating a new descriptor even if you only want to edit one attribute of an existing descriptor.
    
* Thus, option 1 is preferred if you want to only specify a single attribute to update.