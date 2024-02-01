platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/query-tunneling?context=linkedin%2Fcontext

# Query Tunneling

To improve our network infrastructure and better serve API traffic globally, LinkedIn will begin rejecting API calls not meeting new criteria.

Note

For more information about API specific examples, see our [_Migration Guide_](https://learn.microsoft.com/en-us/linkedin/shared/references/migrations/query-tunneling-migration).

## Requirements

Ensure your LinkedIn API requests comply with the following size requirements. If your request exceeds any of the size requirements listed below, your request will receive a 414 response.

| Request parameter | Size in KB |
| --- | --- |
| Raw URL | 8 KB max length (scheme + hostname + port + path + query string of the URL) |
| Query String | 4 KB max length |
| Request URL | 28 KB max length (headers + cookies + URI + queryString, but excluding POST data) |
| URL path segment | 4 KB max characters (the area between slashes in a URL) |