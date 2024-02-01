platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/protocol-version?context=linkedin%2Fcontext


## Single Resource Key

When performing a GET, PARTIAL\_UPDATE, or DELETE on a resource, you must supply the resource key. See the following protocol version 1.0 example:

    GET https://api.linkedin.com/urn:li:endorsement:(urn:li:person:2qXA98-mVk,65761962366)
    

In protocol version 2.0, you must URL encode the entire resource key. The `(` must be encoded to `%28`, `)` to `%29`, `:` to `%3A` and `,` to `%2C`. See the following example:

    GET https://api.linkedin.com/v2/endorsement/urn%3Ali%3Aendorsement%3A%28urn%3Ali%3Aperson%3A2qXA98-mVk%2C65761962366%29
    

Note that special characters in a params string not part of a resource key should not be encoded. See the following example where parentheses are not encoded:

    GET https://api.linkedin.com/v2/ugcPosts?q=authors&authors=List(urn%3Ali%3Aorganization%3A12345)
    

In cases where only numeric ID are passed in as the primary resource key, nothing will change from 1.0 to 2.0. Some APIs require a compound or complex key. The following table lists the syntax differences:

| Key Type | Version 1.0 | Version 2.0 |
| --- | --- | --- |
| primitive key, long | 3   | 3   |
| primitive key, string | someString | someString |
| compound key with association | stringKey=string&longKey=5 | (stringKey:string,longKey:5) |
| complex key | $param.a=value&$param.b=value &keyPart1=value1&keyPart2=value2 | ($param:(a:value,b:value), keyPart1:value1,keyPart2=value2) |