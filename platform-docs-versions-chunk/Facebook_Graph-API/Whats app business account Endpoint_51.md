platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/phone_numbers/

### Sample Response

{
  "data" : \[
    {
      "code\_verification\_status" : "VERIFIED",
      "display\_phone\_number" : "+1 555-555-5555",
      "id" : "106853218861309",
      "quality\_rating" : "GREEN",
      "verified\_name" : "Jaspers Market"
    }
  \],
  "paging" : {
    "cursors" : {
      "after" : "QVFIU...",
      "before" : "QVFIU..."
    }
  }
}

### Sample Request with Filtering

See [Filtering Phone Numbers](https://developers.facebook.com/docs/whatsapp/business-management-api/manage-phone-numbers#filter-phone-numbers).

curl GET \\
"https://graph.facebook.com/`v19.0`/102289599326934/phone\_numbers \\
 ?fields=id,is\_official\_business\_account,display\_phone\_number,verified\_name \\
 &filtering=\[{'field':'account\_mode','operator':'EQUAL','value':'SANDBOX'}\]" \\
-H 'Authorization: Bearer EAAJi...'