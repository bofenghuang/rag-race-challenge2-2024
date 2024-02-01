platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/pagination?context=linkedin%2Fcontext

## Samples

#### Sample Request

    GET https://api.linkedin.com/v2/{service}
    

#### Sample Response

    "elements": [
        {"Result #0"},
        {"Result #1"},
        {"Result #2"},
        {"Result #3"},
        {"Result #4"},
        {"Result #5"},
        {"Result #6"},
        {"Result #7"},
        {"Result #8"},
        {"Result #9"}
    ],
    "paging": {
        "count": 10,
        "start": 0
    }
    

#### Sample Request

    GET https://api.linkedin.com/v2/{service}?start=10&count=10
    

#### Sample Response

    "elements": [
        {"Result #10"},
        {"Result #11"},
        {"Result #12"},
        {"Result #13"},
        {"Result #14"},
        {"Result #15"},
        {"Result #16"},
        {"Result #17"},
        {"Result #18"},
        {"Result #19"}
    ],
    "paging": {
        "count": 10,
        "start": 10
    }