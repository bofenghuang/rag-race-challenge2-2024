platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/integrate


### Creating a resumable job

#### Step one:

First, you will have to create a compliance job and specify whether you will be uploading Tweet IDs or user IDs (using the type parameter). Additionally, add resumable to the body and set it to true. Make sure to replace the $BEARER\_TOKEN below with your bearer token below.

      `curl --request POST \  'https://api.twitter.com/2/compliance/jobs' --header 'Authorization: Bearer $BEARER_TOKEN --header 'Content-Type: application/json' --data-raw '{    "type": "tweets",    "resumable": true }'`
    

If your API call is successful, you will get a response similar to the following:

      `{    "data": {        "download_expires_at": "2021-08-18T19:42:55.000Z",        "status": "created",        "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1425543269983784962/submission/1202726487847104512_1425543269983784962?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210811%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210811T194255Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=355e4c4739ae508304d3df15b4e13e64b6c7752d8d79d73676a4d8e60dc5241f83924ad2a1f8b7bddcc768062bb9c64d39b8e8f7cce7f66ffbea9f9ed33a4da975b3a2c127fb738c1c1ff3c3964bd4d9dc0706e6c8a70e67522160ea774e090d2793e06f890d1158ce86be3031c1c471b74f961b6f18743a28730611000336286ad0111b41fb5d14aa813ff00cf06b3572dc68d0b3c6fdc07f25c1b1196c1af4325a9ead68994944bbef0d2123585ea051deb9765aa7f5832446440bc9ba76af327b69df1fd7b1a99bd4419c128f1f697dbbacbc62bbc7c2c9aebc82a2128be0ed05d48a54d814162daad1232a0d13081e9543ab8557f567149af82281193f37",        "created_at": "2021-08-11T19:42:55.000Z",        "resumable": false,        "id": "1425543269983784962",        "type": "tweets",        "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1425543269983784962/delivery/1202726487847104512_1425543269983784962?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210811%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210811T194255Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=0a11dd5a3c5adb508f32ce904568abada863dc9499ba2adeafb3452ccee0dcb3dade17910dbc502dcbe54c130ac4d8638eb176c8b7344de068139b06c970794efa6312f0a5149f40da441eafcaf475f670c93ca73951999902a531d34dfab1e5490918929e5b06ae803b5604e0c0c26852255ccdbc79a2c1e2eefe924e5e6bf5b6603a7f287d1621333b9548ec6cc203716070528bebc2e67c12e92b1f4e54471db92c15a54799f2b855ae224250ca44c47993fd7d79a4940a0f68fe09f73fc8b291e88cfd10ade860b4b35c2b964d1777c1d93cd300c313138d9ca90aa8b3ecd3bf9dc73d3ebe32ba7634228fe07e1e4ecdda57cd94c802afc520162735d5a3",        "upload_expires_at": "2021-08-11T19:57:55.000Z"    } }`
    

Take note of the value from the upload\_url, you will need it in the following steps.

#### Step two: 

Next, you will need to initiate the resumable upload. In order to do so, make a **POST** call to the upload\_url from the previous step and make sure to include the following headers:

Content-Type: text/plain

Content-Length: 0

x-goog-resumable: start

      `curl --request POST \ 'https://storage.googleapis.com/twttr-tweet-compliance/1430227686685757442/submission/1202726487847104512_1430227686685757442?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210824%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210824T175707Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-length%3Bcontent-type%3Bhost%3Bx-goog-resumable&X-Goog-Signature=890d958f9c7dcb7f238e4971b59da5afc5b8329fb197c67b5930fe0f9dfe180afe2d4bec341111809b88ccfab46ab1f81f4242abc1af7b67c6e8977c52e6d486f5f43ce6a37a7a6530d25f15e2bcd9bb54655fe4ee22b26f8886ba71b67b7b11afd1198d658d1b6f0c41260f55260a260e1be0239977feba43dce40bc0e8e6293a4a3a3f7ee0afc74d3d2f7f2d3d514f108d5887a52ac85760385e5b9bb67cd26bfcf6b1c19151ea8111e217a29407722dc0dc9ab373334e88c18159546237ec9334f9a1e33717dc82800c6a45bba82706d5aece84ecdf3fcac52b21c8a3085a639047cf2707a8b9e4c296fc7cf05edbb110f07b89e38f0f5ea77e8b313cade7' \ --header 'Content-Type: text/plain' --header \  'Content-Length: 0' --header \  'x-goog-resumable: start`
    

If this call is successful, you will get a 201 response code. Then, in the response header, copy the value for the location header which will look something like this:

      `https://storage.googleapis.com/twttr-tweet-compliance/1430227686685757442/submission/1202726487847104512_1430227686685757442?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210824%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210824T175707Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-length%3Bcontent-type%3Bhost%3Bx-goog-resumable&X-Goog-Signature=890d958f9c7dcb7f238e4971b59da5afc5b8329fb197c67b5930fe0f9dfe180afe2d4bec341111809b88ccfab46ab1f81f4242abc1af7b67c6e8977c52e6d486f5f43ce6a37a7a6530d25f15e2bcd9bb54655fe4ee22b26f8886ba71b67b7b11afd1198d658d1b6f0c41260f55260a260e1be0239977feba43dce40bc0e8e6293a4a3a3f7ee0afc74d3d2f7f2d3d514f108d5887a52ac85760385e5b9bb67cd26bfcf6b1c19151ea8111e217a29407722dc0dc9ab373334e88c18159546237ec9334f9a1e33717dc82800c6a45bba82706d5aece84ecdf3fcac52b21c8a3085a639047cf2707a8b9e4c296fc7cf05edbb110f07b89e38f0f5ea77e8b313cade7&upload_id=ADPycds-_Ow7aqcpbG4XguXSVAgd_2fy-XiDA2qm-It9PCwBlZhF4e2bfOAQzEmRJ4T_l6jU6LfYdfrKa_KlFFBOyx3PjYzrxQ`
    

You can then upload your Tweet or User IDs to this location by following step two onwards, [from the quick start guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/compliance/batch-compliance/quick-start).

  
Because of their technical complexity, resumable uploads are best used in conjunction with code. This guide will use Node.js with the [needle request library](https://www.npmjs.com/package/needle).