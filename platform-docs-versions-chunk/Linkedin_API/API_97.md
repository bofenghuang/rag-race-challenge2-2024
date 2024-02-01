platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/development-resources/api-clients


## API Client Overview

To simplify development, we have released API client libraries in the following languages, each of which contains comprehensive documentation and examples in their corresponding GitHub repository:

| Language | Installation and API Reference Docs | Examples |
| --- | --- | --- |
| JavaScript | [link](https://github.com/linkedin-developers/linkedin-api-js-client#linkedin-api-javascript-client) | [link](https://github.com/linkedin-developers/linkedin-api-js-client/tree/master/examples#linkedin-api-javascript-client-examples) |
| Python | [link](https://github.com/linkedin-developers/linkedin-api-python-client#linkedin-api-python-client) | [link](https://github.com/linkedin-developers/linkedin-api-python-client/tree/main/examples) |

Note that these client libraries do not support specific APIs - they provide an abstraction on top of the Rest.li protocol, making it easier to construct API requests to LinkedIn. This simplifies the process for you to build your higher-level clients for specific APIs.

Some of the key features of the LinkedIn API Client Libraries include:

* RestliClient with support for all Rest.li methods
* AuthClient with support for token creation/management
* Typed interfaces to enable code completion and inline documentation in IDEs
* Rest.li protocol 2.0 support
* Automatic key/query parameter encoding
* Support for versioned APIs
* Automatic [query tunneling](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/query-tunneling) of requests, if required