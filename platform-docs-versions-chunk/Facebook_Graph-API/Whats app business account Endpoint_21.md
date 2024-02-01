platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_template_previews/

### Request Syntax

GET /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID>/message\_template\_previews
  ?category=AUTHENTICATION,
  &language=<LANGUAGE>,
  &add\_security\_recommendation=<ADD\_SECURITY\_RECOMMENDATION>,
  &code\_expiration\_minutes=<CODE\_EXPIRATION\_MINUTES>,
  &button\_types=<BUTTON\_TYPES>

### Response

A list of [WhatsApp Business Account Message Template Preview](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account-message-template-preview/) nodes.

### Sample Request

curl 'https://graph.facebook.com/`v19.0`/102290129340398/message\_template\_previews?category=AUTHENTICATION&languages=en\_US%2Ces\_ES&add\_security\_recommendation=true&code\_expiration\_minutes=10&button\_types=OTP' \\
-H 'Authorization: Bearer EAAJB...'