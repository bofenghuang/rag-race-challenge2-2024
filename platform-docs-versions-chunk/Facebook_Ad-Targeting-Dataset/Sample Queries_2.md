platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Sample Queries
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Sample Queries.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/sample-queries

## Get data on ad targeting by user interest

### SQL query

SELECT
    archive\_id,
    include
FROM {database}.{table}
WHERE
    CARDINALITY(
        FILTER(
            CAST(JSON\_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))),
            (x) -> ELEMENT\_AT(x, 'Joe Biden') = 'Interests'))  > 0

### Python and R

RPython

    sql <- sprintf("SELECT archive_id, include FROM %s.%s WHERE CARDINALITY( FILTER( CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))), (x) -> ELEMENT_AT(x, 'Joe Biden') = 'Interests')) > 0", database, table)
    athena$QueryAthena(sql)

    sql = f"SELECT archive_id, include FROM {database}.{table} WHERE CARDINALITY( FILTER( CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))), (x) -> ELEMENT_AT(x, 'Joe Biden') = 'Interests')) > 0"
    execute(sql)

### Dataframe result

## Get data and number of ads targeting by education levels