platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/query-tunneling?context=linkedin%2Fcontext


### Requests with Body

1. Change the request type from PUT to POST if the original request type was PUT. If the original request type was POST, keep it as POST.
2. Add the X-HTTP-Method-Override header using the original HTTP method `-H 'X-HTTP-Method-Override: POST'` for POSTs or `-H 'X-HTTP-Method-Override: PUT'` for PUTs.
3. Add the Content-Type header `-H 'Content-Type: multipart/mixed; boundary=xyz'`. Note that here we need to specify a boundary delimiter (here we use `xyz` for illustration) for multipart body, this delimiter needs to be unique and not appearing in your request content body or url.
4. Move the query string and original request body to body as two sections explained above.

#### Example

Let’s use the example request below to see how we can quickly convert our existing request to the adCreativesV2 API using query tunneling.

###### Current Request

    curl -X POST 'https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196)' \
    -H 'Authorization: Bearer redacted' \
    -H 'Content-Type: application/json' \
    -H 'X-Restli-Protocol-Version: 2.0.0' \
    -H 'X-RestLi-Method:  BATCH_PARTIAL_UPDATE' \
    --data '{"entities": {"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}'
    

1. Change the request type from PUT to POST if the original request type was PUT. If the original request type was POST, keep it as POST.

    curl -X POST https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196) \
      -H 'Authorization: Bearer redacted' \
      -H 'X-RestLi-Method: BATCH_PARTIAL_UPDATE' \
      -H 'X-RestLi-Protocol-Version: 2.0.0' \
      --data ${"entities": {{"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}}'
    

2. Add the X-HTTP-Method-Override header using the original HTTP method `-H 'X-HTTP-Method-Override: POST'` for POSTs or `-H 'X-HTTP-Method-Override: PUT'` for PUTs.

    curl -X POST https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196) \
      -H 'X-HTTP-Method-Override: POST' \
      -H 'Authorization: Bearer redacted' \
      -H 'X-RestLi-Method: BATCH_PARTIAL_UPDATE' \
      -H 'X-RestLi-Protocol-Version: 2.0.0' \
      --data ${"entities": {{"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}}'
    

3. Add the Content-Type header `-H 'Content-Type: multipart/mixed; boundary=xyz'`.

    curl -X POST https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196) \
      -H 'X-HTTP-Method-Override: POST' \
      -H 'Content-Type: multipart/mixed; boundary=xyz' \
      -H 'Authorization: Bearer redacted' \
      -H 'X-RestLi-Method: BATCH_PARTIAL_UPDATE' \
      -H 'X-RestLi-Protocol-Version: 2.0.0' \
      --data ${"entities": {{"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}}'
    

4. Move the query string and original request body to body as two sections.

    curl -X POST https://api.linkedin.com/v2/adCreativesV2 \
      -H 'X-HTTP-Method-Override: POST' \
      -H 'Content-Type: multipart/mixed; boundary=xyz' \
      -H 'Authorization: Bearer redacted' \
      -H 'X-Restli-Protocol-Version: 2.0.0' \
      -H 'X-RestLi-Method:  BATCH_PARTIAL_UPDATE' \
      --data $'--xyz\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\nids=List(47770196)\r\n--xyz\r\n 
             Content-Type: application/json\r\n\r\n{"entities": {"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}\r\n--xyz--'