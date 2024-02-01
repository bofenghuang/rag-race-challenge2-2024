platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin%2Fcontext

## Selecting all child fields and expanding child field with a URN for a single value

**`(person(current_position(*,company~(vanityName))))`**

    {
        "person": {
            "current_position": {
                "company": "urn:li:company:1",
                "company~": {},
                "from": "2009",
                "job_title": "SWE"
            }
        }
    }