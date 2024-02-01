platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/projections?context=linkedin%2Fcontext

## Child Objects

In the above example, `baz` is returned in the response due to the field projection specified because `baz` is an object that has its own fields. Use field projections to select the data you need.

Use the `parentField:(child**Field_1,…,childField_n**)` syntax to select fields for a child object:

    GET https://api.linkedin.com/v2/sampleService/42?fields=id,baz:(beep)
    

#### Sample Response

    {
        "baz": {
            "beep": "Yay!"
        },
        "id": 42
    }