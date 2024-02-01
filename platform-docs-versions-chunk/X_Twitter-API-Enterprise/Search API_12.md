platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/quick-start/enterprise-30-day


### Accessing the counts endpoint

With the counts endpoint, we’ll retrieve the number of Tweets originating from the @TwitterDev account in English grouped by `day`.

* [cURL](#tab1)
* [cURL example](#tab2)
* [](#tab4)

cURL

cURL example

_cURL is a command-line tool for getting or sending files using the URL syntax._

Copy the following cURL request into your command line after making changes to the following:

* **Username** `<USERNAME>` e.g. `email@domain.com`  
    
* **Account name** `<ACCOUNT-NAME>` e.g. `john-doe`  
    
* **Label** `<LABEL>` e.g. `prod`  
    
* **fromDate and toDate** e.g. `"fromDate":"201811010000", "toDate":"201811122359"`

_After sending your request, you will be prompted for your password._

      `curl -X POST -u<USERNAME> "https://gnip-api.twitter.com/search/30day/accounts/<ACCOUNT-NAME>/<LABEL>/counts.json" -d '{"query":"from:TwitterDev lang:en","fromDate":"<yyyymmddhhmm>","toDate":"<yyyymmddhhmm>","bucket":"day"}'`
    

_This is an example cURL request. If you try to run this it will not work._ 

      `curl -X POST -uemail@domain.com "https://gnip-api.twitter.com/search/30day/accounts/john-doe/prod/counts.json" -d '{"query":"from:TwitterDev lang:en","fromDate":"201811100000","toDate":"201812012359","bucket":"day"}'`
    

#### Counts endpoint response payload

The payload you get back from your API request will appear in JSON format, as shown below.

      `{ 	"results": [ 		{ 			"timePeriod": "201811010000", 			"count": 0 		}, 		{ 			"timePeriod": "201811020000", 			"count": 1 		}, 		{ 			"timePeriod": "201811030000", 			"count": 0 		}, 		{ 			"timePeriod": "201811040000", 			"count": 0 		}, 		{ 			"timePeriod": "201811050000", 			"count": 0 		} 	], 	"totalCount": 1, 	"requestParameters": { 		"bucket": "day", 		"fromDate": "201811010000", 		"toDate": "201811060000" 	} }`
    

Great job! Now you've successfully accessed the enterprise Search Tweets: 30-Day API.