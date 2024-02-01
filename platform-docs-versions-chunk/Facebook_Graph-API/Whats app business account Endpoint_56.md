platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/phone_numbers/


### Sample Request

cURLAndroid SDKObjective-C

    curl -i -X POST \
     "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID/phone_numbers?
      cc=COUNTRY-CODE&
      phone_number=PHONE-NUMBER&
      migrate_phone_number=true&
      access_token=USER-ACCESS-TOKEN"

    GraphRequest request = GraphRequest.newPostRequest(
      accessToken,
      "/WHATSAPP-BUSINESS-ACCOUNT-ID/phone_numbers",
      new JSONObject("{\"cc\":\"COUNTRY-CODE\",\"phone_number\":\"PHONE-NUMBER\",\"migrate_phone_number\":true}"),
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID/phone_numbers"
               parameters:@{ @"cc": @"COUNTRY-CODE",@"phone_number": @"PHONE-NUMBER",@"migrate_phone_number": @"true",}
               HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];