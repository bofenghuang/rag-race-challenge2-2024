platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/submitting

## Creating with templates

Using the Create button is fine for sharing a single threat descriptor -- but what if you have a hundred or a thousand? As we'll see immediately below, bulk-upload from CSV or JSON files solves this problem in a very general way.

But there's a common case that's simpler -- when you don't really need a CSV file. ThreatExchange users often find they're submitting a number of threat descriptors which have all the same metadata except for the indicator value. The **create-with-templates** feature fits the bill.

To use templates, simply proceed as above by selecting the Create button -- then select the .

Since template mode is selected, once you hit OK you'll be taken to a commit screen (the same as for upload from file) where you can make any revisions, if any, then commit.

The same works for the Copy button as for the Create button -- this way you can easily make "more of the same" as your organization has more data to share on a given topic.