platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/protocol-version?context=linkedin%2Fcontext

## Multiple Resource Keys

To perform a `BATCH_GET` in protocol version 1.0:

    GET https://api.linkedin.com/people?ids=1&ids=2&ids=3
    

In protocol version 2.0, you must change this query to a `List` syntax:

    GET https://api.linkedin.com/v2/people?ids=List(1,2,3,4)
    

## Complex Keys

In protocol version 1.0, if a resource has complex keys:

    GET https://api.linkedin.com/people?ids[0].$params.a=value0A&ids[0].$params.b=value0B&ids[1].$params.a=value1A&ids[1].$params.b=value1B&ids[2].$params.a=value2A&ids[2].$params.b=value2B
    

In protocol version 2.0, if a resource has complex keys:

    GET https://api.linkedin.com/people?ids=List(($params.a:value0A,$params.b:value0B),($params.a:value1A,$params.b:value1B),($params.a:value2A,$params.b:value2B))
    

Note

The values and the resource parameters must be URL encoded but not the `,` grouping the fields and values. The single resource key had the `,` encoded because it was part of the whole value.