platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin%2Fcontext

## Accessing URN within a child object

**`(person(current_position(company)))`**

    {
        "person": {
            "current_position": {
                "company": "urn:li:company:1"
            }
        }
    }
    

## Accessing URNs within an array of child objects

**`(person(position_history(*(company))))`**

    {
        "person": {
            "position_history": [
                {
                    "company": "urn:li:company:4888383"
                },
                {
                    "company": "urn:li:company:39939"
                }
            ]
        }
    }
    

## Accessing URNs within an array of URNs

**`(person(following_companies(*)))`**

    {
        "person": {
            "following_companies": [
                "urn:li:company:1",
                "urn:li:company:2"
            ]
        }
    }