platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/development-resources/api-clients


## Background

The [Rest.li protocol](https://linkedin.github.io/rest.li/spec/protocol) defines 14 resource methods as a higher-level abstraction on top of the standard HTTP methods, each with its own standardized interface and intended semantics.

For example, to retrieve one or more entities, any one of these Rest.li methods can be implemented for a resource, depending on the use case: [GET](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods#get), [BATCH\_GET](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods#batch_get), [GET\_ALL](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods#get_all), [FINDER](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods#finder-findername), or [BATCH\_FINDER](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods#batch_finder-findername). Each of those Rest.li methods would have its own standard request and response interfaces.

The Rest.li protocol also supports complex resource keys and query parameters, and it has a custom protocol for encoding them.

Nearly all of LinkedIn's APIs are built on the Rest.li framework with additional LinkedIn-specific details, which results in a robust yet complex protocol that can be challenging to implement correctly.