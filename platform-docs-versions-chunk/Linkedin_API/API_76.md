platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin%2Fcontext

# Response Decoration

Warning

**Deprecation Notice**  
The use of Response Decoration is deprecated in some versions of LMS APIs. Please refer the [Recent Changes](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/recent-changes) page for information on the specific API versions that are affected by this deprecation.

When you call an API, the response may contain [URNs](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/urns?context=linkedin/context) referencing the different types of objects provided by LinkedIn's services. These URNs are valuable on their own; however, there may be instances when you want to expand a URN and access the values associated with the entity.

Decoration is a mechanism in LinkedIn's APIs to fetch data belonging to a URN object without having to make an extra call to that object's API. Decoration uses a syntax very similar to LinkedIn's [Field Projections](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/projections?context=linkedin/context).

See the following example of a service that returns URN references to another type of entity:

#### Sample Request

    GET https://api.linkedin.com/v2/{service}/1234
    

#### Sample Response

    {
        "id": 1234,
        "relatedEntity": "urn:li:relatedEntity:6789"
    }
    

Rather than taking the `relatedEntity` URN value and making a second GET call to its parent service, you can use decoration to define how you'd like the `relatedEntity` object to be expanded within the original API request. To do this, append the `~` character to the entity you wish to expand, and then provide the field projection in parentheses afterwards. For example:

#### Sample Request

    GET https://api.linkedin.com/v2/{service}/1234&projection=(id,relatedEntity~($URN,foo,bar))
    

#### Sample Response

    {
        "id": 1234,
        "relatedEntity": {
            "$URN": "urn:li:relatedEntity:6789",
            "bar": "bloop",
            "foo": "bleep"
        }
    }