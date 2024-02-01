platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin%2Fcontext

## Rate Limiting

Response decoration makes calls to other services in order to resolve the requested, decorated entity. These calls are subject to rate limiting. It is possible for calls to return a 200 while the decoration call is rate limited.

The following example makes a request to the `/me` endpoint and uses response decoration to resolve the `digitalMediaAsset` URN in the `displayImage` field. The call to the `/me` endpoint is successful, but the decoration call to resolve `displayImage` is rate limited.

    GET https://api.linkedin.com/v2/me?projection=(id,profilePicture(displayImage~(*)))
    

    {
        "profilePicture": {
            "displayImage!": {
                "serviceErrorCode": 101,
                "message": "Resource level throttle limit for calls to this resource is reached.",
                "status": 429
            },
            "displayImage": "urn:li:digitalmediaAsset:C4D03AQGFBHiaY1XXNA"
        },
        "id": "z6_nnTIGu-"
    }