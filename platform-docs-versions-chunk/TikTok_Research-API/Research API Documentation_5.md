platform: TikTok
topic: Research-API
subtopic: Research API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Documentation.md
url: https://developers.tiktok.com/doc/research-api-get-started/

## Query condition

Similar to the WHERE clause in SQL, a condition can be used to filter data returned in a query operation. The above request is equivalent to the following SQL query:

     SELECT id,like_count FROM video_table WHERE region_code IN ["US", "CA"] AND create_date > 20220615

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required?** |
| field\_name | string | The field name this condition is restricting | "region\_code" | TRUE |
| operation | string | The comparison logic of this condition. One of: "EQ", "IN", "GT", "GTE", "LT", "LTE" | "GT" | TRUE |
| field\_values | list\[string\] | A list of values to be compared with | \["US", "IN"\] | TRUE |

Note: approximate string matching (or fuzzy string searching) is used to match conditions.