platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/app/translations

### Permissions

* An app access token is required to return translations for that app.
    

### Modifiers

| Name | Description | Type |
| --- | --- | --- |
| `locale` | Specifies which locale of language to request. This is a required parameter when reading this edge. | `enum{`[locale](https://www.facebook.com/translations/FacebookLocales.xml)`}` |

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `id` | A unique ID for each individual string. | `string` |
| `translation` | The translated string. | `string` |
| `approval_status` | The approval status of the string. | `enum{auto-approved, approved, unapproved}` |
| `native_string` | The original string that was translated. | `string` |
| `description` | The provided description of the string. | `string` |