platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights

### Response

A JSON object containing the results of your query. Results can include the following data, based on your query specifications:

{
  "data": \[
    {
      "name": "{name}",
      "period": "{period}",
      "values": \[
        {
          "value": {value}
        }
      \],
      "title": "{title}",
      "description": "{description}",
      "total\_value": {
        "value":{value},
        "breakdowns": \[
          {
            "dimension\_keys": \[
              "{dimension-key-1}",
              "{dimension-key-2}"
              ...
            \],
            "results": \[
              {
                "dimension\_values": \[
                  "dimension-value-1",
                  "dimension-value-2"
                  ...
                \],
                "value": {value}
              },
              ...
            \]
          }
        \]
      },
      "id": "{id}"
    }
  \]
}