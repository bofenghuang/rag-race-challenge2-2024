platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/query-tunneling?context=linkedin%2Fcontext


### Requests without Body

1. Change the request from `GET` to `POST`.
2. Add the `X-HTTP-Method-Override` header, using the original HTTP method (-H "X-HTTP-Method-Override: GET").
3. Add the `Content-Type` header (-H "Content-Type: application/x-www-form-urlencoded").
4. Move the query string to the body of the request.

#### Example

Let’s use the example request below to see how we can quickly convert our existing request to the organizationalEntityAcls API using query tunneling.

##### Current Request

    curl -X GET 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
    -H 'Authorization: Bearer redacted'
    

1. Change the request type from GET to POST.

    curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
    -H 'Authorization: Bearer redacted'
    

2. Add the method override header and append the original GET request type.

    curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
    -H 'X-HTTP-Method-Override: GET'
    -H 'Authorization: Bearer redacted'
    

3. Add the `Content-Type` header.

    curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
    -H 'X-HTTP-Method-Override: GET'
    -H 'Content-Type: application/x-www-form-urlencoded'
    -H 'Authorization: Bearer redacted'
    

4. Move the query string of the request URL to the request body.

    curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls' \
    -H 'X-HTTP-Method-Override: GET'
    -H 'Content-Type: application/x-www-form-urlencoded' 
    -H 'Authorization: Bearer redacted'
    --data 'q=roleAssignee&projection=(elements*(organizationalTarget~))'