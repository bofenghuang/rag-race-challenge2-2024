platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Sample Queries
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Sample Queries.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/sample-queries

### SQL query

In this query, we use the Ad Library data table (`ad_archive_api`) to combine targeting data with delivery data.

SELECT
    a.\*
FROM {database}.{table} AS a,
    {database}.{api\_table} AS b
WHERE
    a.ds = b.ds
    AND a.archive\_id = b.fbid
    AND b.reached\_countries LIKE '%US%';
      

### Python and SQL

RPython

    sql <- sprintf("SELECT a.* FROM %s.%s AS a, %s.%s AS b WHERE a.ds = b.ds AND a.archive_id = b.fbid AND b.reached_countries LIKE '%%US%%';", database, table, database, api_table)
    athena$QueryAthena(sql)

    sql = f"SELECT a.* FROM {database}.{table} AS a, {database}.{api_table} AS b WHERE a.ds = b.ds AND a.archive_id = b.fbid AND b.reached_countries LIKE '%US%';"
    execute(sql)

### Dataframe result