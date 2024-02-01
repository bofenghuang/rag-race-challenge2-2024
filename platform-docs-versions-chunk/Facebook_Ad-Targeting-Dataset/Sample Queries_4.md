platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Sample Queries
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Sample Queries.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/sample-queries

### Python and R

RPython

    sql <- sprintf("WITH education_table AS ( SELECT REDUCE( CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))), MAP(), (s, x) -> (MAP_CONCAT(s, MAP_FILTER(x, (k, v) -> v = 'Education level'))), s -> s) AS education_levels FROM %s.%s) SELECT education_levels, COUNT(*) AS count FROM education_table GROUP BY education_levels ORDER BY -count;", database, table)        
    athena$QueryAthena(sql)

    sql = f"WITH education_table AS ( SELECT REDUCE( CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))), MAP(), (s, x) -> (MAP_CONCAT(s, MAP_FILTER(x, (k, v) -> v = 'Education level'))), s -> s) AS education_levels FROM {database}.{table}) SELECT education_levels, COUNT(*) AS count FROM education_table GROUP BY education_levels ORDER BY -count;"
    execute(sql)

### Dataframe result

## Get data and count of ads targeting by non-interest