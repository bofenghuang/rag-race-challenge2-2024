platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin%2Fcontext


## Accessing complex type object

When a URN is a field’s key and the value is an object, it is called a complex type object. In the following example, the `messages` field maps to an object with 2 fields that are `MessageUrns`. These 2 `MessageUrns` are keys that map to objects containing data such as `bcc`,`count`, and `content`. To access the `bcc` values for each `MessageUrn`, use the decoration `(person(messages()))(person(messages(*(from,bcc(*)))))`.

**`(person(messages()))`**

    {
        "person": {
            "messages": {
                "urn:li:message:1": {
                    "bcc": [
                        "urn:li:personr:1",
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
            }
        }
    }
    

**`(person(messages(*(from,bcc(*)))))`**

    {
        "person": {
            "messages": {
                "urn:li:message:1": {
                    "bcc": [
                        "urn:li:person:1",
                        "urn:li:person:39"
                    ],
                    "from": "urn:li:person:99"
                },
                "urn:li:message:2": {
                    "bcc": [
                        "urn:li:person:1",
                        "urn:li:person:80"
                    ]
                }
            }
        }
    }