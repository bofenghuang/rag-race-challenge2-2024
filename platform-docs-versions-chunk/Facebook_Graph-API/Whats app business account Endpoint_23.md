platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_template_previews/


### Parameters

| Parameter | Description |
| --- | --- |
| `add_security_recommendation`<br><br>boolean | Default value: `false`<br><br>  <br>Set to `true` if you want the security recommendation body string included in the response.<br><br>  <br>If omitted, the security recommendation string will not be included. |
| `button_types`<br><br>array<enum {OTP}> | Default value: `[]`<br><br>  <br>Comma-separated list of strings indicating button type.<br><br>  <br>If included, the response will include the button text for each button in the response.<br><br>  <br>For authentication templates, this value must be `OTP`. |
| `category`<br><br>enum {AUTHENTICATION} | The category of the message template. Set to `AUTHENTICATION` for authentication templates.<br><br>Required |
| `code_expiration_minutes`<br><br>int64 | For authentication templates, set to an integer if you want the code expiration footer string included in the response.<br><br>  <br>If omitted, the code expiration footer string will not be included.<br><br>  <br>Value indicates number of minutes until code expires.<br><br>  <br>Minimum `1`, maximum `90`. |
| `languages`<br><br>array<string> | Default value: `["af","sq","ar","az","bn","bg","ca","zh_CN","zh_HK","zh_TW","hr","cs","da","nl","en","en_GB","en_US","et","fil","fi","fr","ka","de","el","gu","ha","he","hi","hu","id","ga","it","ja","kn","kk","ko","ky_KG","lo","lv","lt","mk","ml","ms","mr","nb","fa","pl","pt_BR","pt_PT","pa","ro","ru","rw_RW","sr","sk","sl","es","es_AR","es_ES","es_MX","sw","sv","ta","te","th","tr","uk","ur","uz","vi","zu"]`<br><br>  <br>Comma-separated list of language and locale codes of language versions you want returned.<br><br>  <br>If omitted, versions of all supported languages will be returned. |