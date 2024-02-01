platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Sample Queries
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Sample Queries.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/sample-queries

### SQL query

SELECT
    exclusion,
    exclusion\_type,
    COUNT(\*)
FROM {database}.{table}
CROSS JOIN UNNEST(CAST(JSON\_EXTRACT(exclude, '$') AS MAP(VARCHAR, VARCHAR))) AS t (
        exclusion,
        exclusion\_type
    )
GROUP BY
    exclusion,
    exclusion\_type;

### Python and R

RPython

    sql <- sprintf("SELECT exclusion, exclusion_type, COUNT(*) FROM %s.%s CROSS JOIN  UNNEST(CAST(JSON_EXTRACT(exclude, '$') AS MAP(VARCHAR, VARCHAR))) AS t (exclusion, exclusion_type) GROUP BY exclusion, exclusion_type;", database, table)
    athena$QueryAthena(sql)

    sql =f"SELECT exclusion, exclusion_type, COUNT(*) FROM {database}.{table} CROSS JOIN UNNEST(CAST(JSON_EXTRACT(exclude, '$') AS MAP(VARCHAR, VARCHAR))) AS t (exclusion, exclusion_type) GROUP BY exclusion, exclusion_type;"
    execute(sql)

### Dataframe result

## Get data on ad targeting by specific country