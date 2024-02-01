platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/urns?context=linkedin%2Fcontext

## URN Decoration

To make this query more efficient, we can use [decoration](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin/context) to expand the share owner URN and return the owner's first and last name in a single call. This saves an API call by not having to make a separate call to the `people` API.

#### Sample Request

    GET https://api.linkedin.com/v2/shares/1234?projection=(id,owner~(localizedFirstName,localizedLastName))
    

    {
        "id": "1234",
        "owner": "urn:li:person:-f_Ut43FoQ",
        "owner~": {
            "localizedFirstName": "Schrute",
            "localizedLastName": "Dwight"
        }
    }
    

## URNs and Namespaces

For common URNs and their namespace conversions, see [URN Namespaces](https://learn.microsoft.com/en-us/linkedin/shared/references/v2/urn-namespace?context=linkedin/context).