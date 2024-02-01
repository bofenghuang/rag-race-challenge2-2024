platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/field-expansion

# Field expansion

There are a number of fields in the data available through the Meta Content Library API that are nested. For example, the `statistics` field contains the `like_count`, `haha_count`, and several other fields. When you create search objects, you might want to include some or all of the nested fields in your search. _Field expansion_ allows you to perform queries for multiple fields and their nested fields in a single call. We refer to the nested fields as _expanded fields_.

In the [Data dictionary](https://developers.facebook.com/docs/content-library-api/data), expanded fields are indicated by a dot notation. For example, `statistics.like_count` indicates that `like_count` is available within `statistics`. To specify expanded fields in your search objects, you can either use this dot notation or you can append the names of the expanded fields in curly braces after the parent field. See the examples in this section.