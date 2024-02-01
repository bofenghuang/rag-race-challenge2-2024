platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Sample Queries
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Sample Queries.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/sample-queries

### SQL query

WITH education\_table AS (
    SELECT
        REDUCE(
            CAST(JSON\_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))),
            MAP(),
            (s, x) -> (
                    MAP\_CONCAT(s, MAP\_FILTER(x, (k, v) -> v = 'Education level'))
                ),
            s -> s
        ) AS education\_levels
    FROM {database}.{table}
)
SELECT
    education\_levels,
    COUNT(\*) AS count
FROM education\_table
GROUP BY
    education\_levels;
ORDER BY
    -count;