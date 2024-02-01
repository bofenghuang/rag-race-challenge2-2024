platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/projections?context=linkedin%2Fcontext

# Field Projections

Field projection controls how much of an entity's data is displayed in response to an API request.

All APIs have a default set of field projections that control which fields are returned. If you don't need certain fields, you can decrease response time and payload size by using a projection to ask only for the fields your application is interested in.

By default, services may not always return all of the information that your application requests. In these cases, you'll need to use a projection to retrieve any non-default fields.

Field projections are defined using the `&fields=` query parameter and narrowed by providing a comma-separated list of field names that you want returned as the value of the parameter.

In the following example, a service returns these types of objects:

#### Sample Objects

    {
        "id" : int,      <- Default projection field
        "foo": string,   <- Default projection field
        "bar": boolean,
        "baz": Object
    }
    

A GET call to retrieve one of these objects provides the following response:

    GET https://api.linkedin.com/v2/sampleService/42
    

#### Sample Response

    {
        "foo": "Zing!",
        "id": 42
    }
    

Notice how the `bar` and `baz` fields were not returned in the response. This is because they are not part of the service's default field projection.

If you want to get `id`, `bar`, and `baz` back in the response (but not `foo`, because it's irrelevant to your application), use a field projection:

    GET https://api.linkedin.com/v2/sampleService/42?fields=id,bar,baz
    

#### Sample Response

    {
        "bar": true,
        "baz": {
            "beep": "Yay!",
            "bloop": "Meh",
            "blorp": "Boo!"
        },
        "id": 42
    }