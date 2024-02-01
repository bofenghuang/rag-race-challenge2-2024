platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin%2Fcontext


## Decorating within Arrays/Lists

In some circumstances, a service might return a collection of URNs that are not all of the same type. In this case, provide multiple decoration instructions to tell the service how to deal with any potential URN type that is returned. See the following sample request and the list of different URN types that it returns within entities:

#### Sample Request

    GET https://api.linkedin.com/v2/{service}/1234
    

#### Sample Data

    {
        "entities": [
            "urn:li:foo:123",
            "urn:li:bar:234",
            "urn:li:baz:345"
        ],
        "id": 1234
    }
    

To decorate each of the `foo`, `bar`, and `baz` URN types in this response, use the following projection syntax in your request:

#### Sample Request

    GET https://api.linkedin.com/v2/{service}/1234?projection=entities*~foo(a,b)~bar(c,d)~baz(e,f))
    

#### Sample Response

    {
        "entities": [
            {
                "a": 1,
                "b": 2
            },
            {
                "c": 10,
                "d": 20
            },
            {
                "e": 100,
                "f": 200
            }
        ],
        "id": 1234
    }