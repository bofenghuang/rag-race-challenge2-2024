platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/conversation_analytics/


### Example

Requirements

* whatsapp\_business\_management permission
    
* whatsapp\_business\_messaging permission
    
* public\_profile permission
    
* WHATSAPP BUSINESS ACCOUNT ID
    
* USER ACCESS TOKEN
    

Request

_Formatted for readability._

cURLAndroid SDKObjective-C

    curl -i -X GET \ 
    "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID?fields=conversation_analytics.start(1651698000).end(1652302800).granularity(DAILY).phone_numbers(PHONE-NUMBER).country_codes().metric_types().conversation_types().conversation_directions().dimensions(CONVERSATION_DIRECTIONCONVERSATION_TYPECOUNTRYPHONE)&
    access_token=USER-ACCESS-TOKEN"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/WHATSAPP-BUSINESS-ACCOUNT-ID",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    Bundle parameters = new Bundle();
    parameters.putString("fields", "conversation_analytics.start(1651698000).end(1652302800).granularity(DAILY).phone_numbers(["PHONE-NUMBER "]).country_codes([]).metric_types([]).conversation_types([]).conversation_directions([]).dimensions(["CONVERSATION_DIRECTION","CONVERSATION_TYPE","COUNTRY","PHONE"])");
    request.setParameters(parameters);
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID"
               parameters:@{ @"fields": @"conversation_analytics.start(1651698000).end(1652302800).granularity(DAILY).phone_numbers(["PHONE-NUMBER"]).country_codes([]).metric_types([]).conversation_types([]).conversation_directions([]).dimensions(["CONVERSATION_DIRECTION","CONVERSATION_TYPE","COUNTRY","PHONE"])",}
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

Response

{
  "conversation\_analytics": {
    "data": \[
      {
        "data\_points": \[
          {
            "start": 1651698000,
            "end": 1651784400,
            "conversation": 281,
            "phone\_number": "PHONE-NUMBER",
            "country": "US",
            "conversation\_type": "FREE\_TIER",
            "conversation\_direction": "BUSINESS\_INITIATED",
            "cost": 0
          },
          {
            "start": 1652130000,
            "end": 1652216400,
            "conversation": 631,
            "phone\_number": "PHONE-NUMBER",
            "country": "US",
            "conversation\_type": "FREE\_TIER",
            "conversation\_direction": "BUSINESS\_INITIATED",
            "cost": 0
          }
        \]
      }
    \]
  },
  "id": "WHATSAPP-BUSINESS-ACCOUNT-ID"
}