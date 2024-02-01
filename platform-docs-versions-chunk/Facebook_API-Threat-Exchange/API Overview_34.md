platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/reference/ui/descriptors

# ThreatExchange UI Descriptors Tab

## Searching

You have multiple ways to search for ThreatDescriptors (and more to come -- see [status here](https://developers.facebook.com/docs/threat-exchange/ui#status)):

Search results are rendered as a table. You can view (or clone) ones you do not own, or edit ones you do own:

Details are shown in a popup -- here is a descriptor owned by another app:

## Broadening your searches

Given search results, you may wish to fan out to similar results. In this example, let's start with sample data.

  

From there, we can find other descriptors with the same indicator (hash):

  

We can also find other descriptors which have been related to these (see [Submitting Connections](https://developers.facebook.com/docs/threat-exchange/reference/submitting-connections)):

  

Note that we can poke the fanout buttons multiple times to traverse deeper depths of connection.