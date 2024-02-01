platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/editing


## Bulk-editing using the UI

First, perform any descriptor-search, then choose "Bulk edit". All descriptors in the search that are owned by you (if any) will be bulk-editable.

  

Choose "Select all", then "Bulk-revise selected items".

  

At this point you can edit various attributes. Here, we show that the collection being edited has multiple values for Severity; we can set them all to the same value if we like -- say, INFO. To continue the example, let's add a new tag -- `testing-bulk-edit-for-doc` -- to all selected descriptors.

  

In the create-tag popup we can fill out the attributes and then hit OK.

  

Having bulk-edited some attributes, we can OK the bulk-edit popup.

  

We can now continue editing if we like -- perhaps select any particular descriptor and revise it further using the "Revise" button on a given row. (Or we can abandon the edits entirely -- they're still browser-local only, not yet saved to ThreatExchange.) Instead, let's go ahead and save our changes.

  

We now see the committed descriptors along with their IDs.