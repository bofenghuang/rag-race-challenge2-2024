platform: Facebook
topic: Graph-API
subtopic: Whats app business hsm Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business hsm Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/


### Example

Requirements

* whatsapp\_business\_management permission
    
* whatsapp\_business\_messaging permission
    
* public\_profile permission
    
* WHATSAPP MESSAGE TEMPLATE ID
    
* USER ACCESS TOKEN
    

Request

cURLAndroid SDKObjective-C

    curl -i -X GET \
     "https://graph.facebook.com/LATEST-VERSION/WHATS-APP-MESSAGE-TEMPLATE-ID?access_token=USER-ACCESS-TOKEN"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/WHATS-APP-MESSAGE-TEMPLATE-ID",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/WHATS-APP-MESSAGE-TEMPLATE-ID"
               parameters:nil
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

Response

{
  "name": "shiptest",
  "components": \[
    {
      "type": "BODY",
      "text": "testing"
    }
  \],
  "language": "en\_US",
  "status": "REJECTED",
  "category": "TRANSACTIONAL",
  "id": "WHATS-APP-MESSAGE-TEMPLATE-ID"
}