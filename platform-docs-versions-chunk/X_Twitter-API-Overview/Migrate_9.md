platform: X
topic: Twitter-API-Overview
subtopic: Migrate
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Overview/Migrate.md
url: https://developer.twitter.com/en/docs/twitter-api/migrate/whats-new


###   
Tweet annotations

Annotations can be used to discover Tweets on topics of interest or to segment Tweets by entity categories. 

Tweets are analyzed and annotated based on the content of the Tweet text by both semantic labeling (context annotations) and internal machine learning algorithms (named entity recognition). These annotations are now available via API in the response payload. We call these new elements “annotations” and they are delivered as two fields, context\_annotations and entity, and can be used to filter search Tweets, Tweet counts, and filtered stream responses.

Learn more about [Tweet annotations](https://developer.twitter.com/en/docs/twitter-api/annotations).

Here is an example of what this would look like in your payload:

      `"context_annotations": [       {         "domain": {           "id": "45",           "name": "Brand Vertical",           "description": "Top level entities that describe a Brands industry"         }       },       {         "domain": {           "id": "46",           "name": "Brand Category",           "description": "Categories within Brand Verticals that narrow down the scope of Brands"         },         "entity": {           "id": "781974596752842752",           "name": "Services"         }       },       {         "domain": {           "id": "47",           "name": "Brand",           "description": "Brands and Companies"         },         "entity": {           "id": "10026364281",           "name": "Apple"         }       },       {         "domain": {           "id": "48",           "name": "Product",           "description": "Products created by Brands.  Examples: Ford Explorer, Apple iPhone."         },         "entity": {           "id": "10044903039",           "name": "Apple - iOS"         }       }     ],     "created_at": "2020-05-12T19:44:51.000Z",     "entities": {       "annotations": [         {           "start": 49,           "end": 51,           "probability": 0.8997,           "type": "Product",           "normalized_text": "iOS"         }       ]`