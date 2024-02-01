platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/protocol-version?context=linkedin%2Fcontext

## Parameters

When performing a `FINDER` in version 1.0, you often have query parameters such as filters represented as an array:

    GET https://api.linkedin.com/resource?q=FinderParam&param.aList[0]=foo&param.aList[1]=bar&param.aList[2]=baz& param.anObject.aField=1&param.anObject.anotherField=value
    

In protocol version 2.0, you must change this query to a `List` syntax, much like the multiple keys:

    GET https://api.linkedin.com/resource?q=myFinder&param=(aList:List(foo,bar,baz),anObject:(aField:1,anotherField:value))
    

Note

The values and the resource parameters must be URL encoded but not the `,` grouping the fields and values. The single resource key had the `,` encoded because it was part of the whole value.