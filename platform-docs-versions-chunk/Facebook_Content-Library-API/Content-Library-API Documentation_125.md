platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/field-expansion


## Specifying expanded fields

You can specify which expanded fields you want returned on any associated data by using the dot notation in your query to specify first the parent field, then the expanded field (such as `statistics.haha_count`).

RPython

    post_search <- client$search_posts(q='cybercrime', fields="id,statistics.like_count,statistics.haha_count")
    post_search$query_next_page()

    post_search = client.search_posts(q="cybercrime", fields="id,statistics.like_count,statistics.haha_count")
    display(post_search.query_next_page())

Alternatively, you can append a comma-separated list of expanded field names wrapped in curly braces to the end of any parent field name.

RPython

    post_search <- client$search_posts(q='cybercrime', fields="id,statistics{like_count,haha_count}")
    post_search$query_next_page()

    post_search = client.search_posts(q="cybercrime", fields="id,statistics{like_count,haha_count}")
    display(post_search.query_next_page())

If you specify a field but do not specify any of its expanded fields, default expanded fields on the associated node are included in the response. If you omit the `fields` parameter altogether, default expanded fields on default parent fields on the associated data are included in the response.