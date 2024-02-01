platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/protocol-version?context=linkedin%2Fcontext

# Protocol Versions

LinkedIn V2 APIs support two protocol versions: 1.0 and 2.0. See the following syntax differences to help you migrate from 1.0 to 2.0.

LinkedIn plans to deprecate protocol version 1.0 in the near future. We strongly encourage developers to migrate as soon as possible and take advantage of the performance improvements in protocol version 2.0.

To use version 2.0, you must pass `X-Restli-Protocol-Version: 2.0.0` as the header in your API requests. If you don't pass a header, your call will default to version 1.0.