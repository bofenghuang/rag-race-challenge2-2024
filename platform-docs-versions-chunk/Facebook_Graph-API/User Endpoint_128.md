platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/picture/

### Notes

* Supports App-Scoped User IDs (ASID), User IDs (UID), and Page-Scoped User IDs (PSID).
* By default this edge will return a `302` redirect to the image. To get data about the image, include the `redirect=false` query string parameter.
* Profile picture URLs returned by this edge will expire.
* Tokenless requests on ASIDs made by apps that are [inactive](https://developers.facebook.com/docs/apps/#inactive-apps) or that have not completed [Data Use Checkup](https://developers.facebook.com/docs/apps/certifying_data_use) will receive an error code in response.

### Limitations

* Apps in [Development mode](https://developers.facebook.com/docs/apps#development-mode) that make tokenless requests on ASIDs will receive a silhouette image in response.
* Apps in Development mode that make requests with a [Client token](https://developers.facebook.com/docs/facebook-login/access-tokens/#clienttokens) will receive a silhouette image in response.