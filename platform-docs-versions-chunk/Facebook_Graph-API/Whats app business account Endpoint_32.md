platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/


### Sample Request

curl 'https://graph.facebook.com/`v19.0`/102290129340398/message\_templates' \\
-H 'Content-Type: application/json' \\
-H 'Authorization: Bearer EAAJB...' \\
-d '
{
  "name": "seasonal\_promotion",
  "language": "en",
  "category": "MARKETING",
  "components": \[
    {
      "type": "HEADER",
      "format": "TEXT",
      "text": "Our {{1}} is on!",
      "example": {
        "header\_text": \[
          "Summer Sale"
        \]
      }
    },
    {
      "type": "BODY",
      "text": "Shop now through {{1}} and use code {{2}} to get {{3}} off of all merchandise.",
      "example": {
        "body\_text": \[
          \[
            "the end of August","25OFF","25%"
          \]
        \]
      }
    },
    {
      "type": "FOOTER",
      "text": "Use the buttons below to manage your marketing subscriptions"
    },
    {
      "type":"BUTTONS",
      "buttons": \[
        {
          "type": "QUICK\_REPLY",
          "text": "Unsubcribe from Promos"
        },
        {
          "type":"QUICK\_REPLY",
          "text": "Unsubscribe from All"
        }
      \]
    }
  \]
}'