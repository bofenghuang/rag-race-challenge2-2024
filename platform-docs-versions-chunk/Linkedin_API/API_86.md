platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/urns?context=linkedin%2Fcontext

# URNs and IDs

## URNs

[URNs](http://www.ietf.org/rfc/rfc2141.txt) are used to represent foreign associations to an entity (persons, organizations, and so on) in an API. A URN is a string-based identifier with the format:

`urn:{namespace}:{entityType}:{id}`

For example:

* `urn:li:person:123`
* `urn:li:organization:456`
* `urn:li:sponsoredAccount:789`

URNs encode more information, including the entity type. Using the entity type, it's possible to dereference a URN and access the underlying data of the entity using a process called [decoration](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin/context).

URN values returned from LinkedIn's APIs are a maximum of 255 characters in length.

## IDs

Simple integer IDs are returned to represent an object's primary key. Your application should support transforming URNs into IDs and vice versa.