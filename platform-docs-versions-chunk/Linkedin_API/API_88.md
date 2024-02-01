platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/urns?context=linkedin%2Fcontext

## URN Deconstruction

To get more information about the owner of the share, we can deconstruct the URN by removing the `urn:li:person` prefix and making an additional call to the `people` API. We need to deconstruct the URN and parse the ID because the `people` API expects an ID.

#### Sample Request

    GET https://api.linkedin.com/v2/people/id=-f_Ut43FoQ?projection=(id,localizedFirstName,localizedLastName)
    

    {
        "id": "-f_Ut43FoQ",
        "localizedFirstName": "Dwight",
        "localizedLastName": "Schrute"
    }