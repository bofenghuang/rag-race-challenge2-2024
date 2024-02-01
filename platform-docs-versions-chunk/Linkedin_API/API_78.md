platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin%2Fcontext


## Sample Projections

Consider the following data model of a sample resource and review the below samples showing how to access various parts of this data in order to decorate.

    {
        "person": {
            "current_position": {
                "company": "urn:li:company:1",
                "from": "2009",
                "job_title": "SWE"
            },
            "firstname": "First Name",
            "following_companies": [
                "urn:li:company:1",
                "urn:li:company:2"
            ],
            "lastname": "Last Name",
            "messages": {
                "urn:li:message:1": {
                    "bcc": [
                        "urn:li:person:1",
                        "urn:li:person:39"
                    ],
                    "content": "xyz",
                    "from": "urn:li:person:99"
                },
                "urn:li:message:2": {
                    "bcc": [
                        "urn:li:person:1",
                        "urn:li:person:80"
                    ],
                    "content": "abc",
                    "count": 1929
                }
            },
            "phone": "200-100-200",
            "position_history": [
                {
                    "company": "urn:li:company:4888383",
                    "from": "2006",
                    "job_title": "SSE",
                    "to": "2009"
                },
                {
                    "company": "urn:li:company:39939",
                    "from": "1999",
                    "job_title": "SE",
                    "to": "2006"
                }
            ]
        }
    }