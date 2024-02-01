platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/urns?context=linkedin%2Fcontext

## IDs versus URNs

IDs are self-referencing identifiers similar to a primary key. URNs are Globally Unique Identifiers (GUID) used to represent an entity's foreign associations.

In the example below, we fetch details about a share and use a [projection](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/projections?context=linkedin/context) to limit the results to the `id` and `owner` fields. The `shares` API returns an `id` that is the primary key and an `owner` that is a foreign reference to the person who created the share in the form of a `URN`.

| Resource Type | URN | ID  |
| --- | --- | --- |
| Share | `urn:li:share:1234` | 1234 |
| Person | `urn:li:person:-f_Ut43FoQ` | \-f\_Ut43FoQ |

#### Sample Request

    GET https://api.linkedin.com/v2/shares/1234?projection=(id,owner)
    

    {
        "id": "1234",
        "owner": "urn:li:person:-f_Ut43FoQ"
    }