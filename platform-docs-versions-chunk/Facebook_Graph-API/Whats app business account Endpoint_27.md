platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/


### Sample Response

{
  "data": \[
    {
      "name": "order\_delivery\_update",
      "components": \[
        {
          "type": "HEADER",
          "format": "LOCATION"
        },
        {
          "type": "BODY",
          "text": "Good news {{1}}! Your order #{{2}} is on its way to the location above. Thank you for your order!",
          "example": {
            "body\_text": \[
              \[
                "Mark",
                "566701"
              \]
            \]
          }
        },
        {
          "type": "FOOTER",
          "text": "To stop receiving delivery updates, tap the button below."
        },
        {
          "type": "BUTTONS",
          "buttons": \[
            {
              "type": "QUICK\_REPLY",
              "text": "Stop Delivery Updates"
            }
          \]
        }
      \],
      "language": "en\_US",
      "status": "APPROVED",
      "category": "UTILITY",
      "id": "1667192013751005"
    },
    ...
  \],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MjQZD"
    }
  }
}