platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/Errors

### [](#errors)Errors

Every error returned by the CrowdTangle API will assume a standard format. The API will additionally return a proper http status as well. If a `200` is returned, there was no error.

#### [](#error-response)Error Response

| Property | Type | Description |
| --- | --- | --- |
| code | int | The [CrowdTangle error code](https://github.com/CrowdTangle/API/wiki/Errors#errorcodes), if available. |
| message | string | A human-readable message describing the error. Always returned. |
| status | int | The HTTP status code, if available. |
| url | string | A URL for more information, if available. |

For example:

    {
      "status": 401,
      "code": 30,
      "message": "Please supply an API token"
    }
    

#### [](#crowdtangle-error-codes)CrowdTangle Error Codes

| Code | Description |
| --- | --- |
| 20  | Unknown Parameter |
| 21  | Illegal Parameter Value |
| 22  | Missing Parameter |
| 30  | Missing Token |
| 31  | Invalid Token |
| 40  | Does Not Exist |
| 41  | Not Allowed |