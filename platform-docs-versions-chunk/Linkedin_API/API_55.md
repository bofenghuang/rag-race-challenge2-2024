platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/projections?context=linkedin%2Fcontext

## Parent Field as Map

Objects can have nested objects with child fields of their own such as the example below:

#### Sample Data

    {
        "baz": {
            "1": {
                "beep": "Yay!",
                "foo": "foo1"
            },
            "2": {
                "beep": "Nay!",
                "foo": "foo2"
            }
        },
        "id": 42
    }
    

Use the `$*:(childField_1,…,childField_n)` syntax to control the fields requested from nested objects:

    GET https://api.linkedin.com/v2/sampleService/42?fields=id,baz:($*:(beep))
    

#### Sample Response

    {
        "baz": {
            "1": {
                "beep": "Yay!"
            },
            "2": {
                "beep": "Nay!"
            }
        },
        "id": 42
    }