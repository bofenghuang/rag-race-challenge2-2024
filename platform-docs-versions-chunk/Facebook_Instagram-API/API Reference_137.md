platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights

### Response

A JSON object containing the results of your query. Results can include the following data, based on your query specifications:

{
  "data": \[
    {
      "name": "{data}",
      "period": "{period}",
      "title": "{title}",
      "description": "{description}",
      "total\_value": {
        "value": {value},
        "breakdowns": \[
          {
            "dimension\_keys": \[
              "{key-1}",
              "{key-2",
              ...
            \],
            "results": \[
              {
                "dimension\_values": \[
                  "{value-1}",
                  "{value-2}",
                  ...
                \],
                "value": {value},
                "end\_time": "{end-time}"
              },
              ...
            \]
          }
        \]
      },
      "id": "{id}"
    }
  \],
  "paging": {
    "previous": "{previous}",
    "next": "{next}"
  }
}