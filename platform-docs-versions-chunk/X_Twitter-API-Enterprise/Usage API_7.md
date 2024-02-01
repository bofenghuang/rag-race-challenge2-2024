platform: X
topic: Twitter-API-Enterprise
subtopic: Usage API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Usage API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/usage-api/api-reference/get-usage


## Requesting and Receiving Data [¶](#requesting-and-receiving-data- "Permalink to this headline")

The Usage API works by issuing an HTTP GET request with HTTP BASIC-AUTH credentials to the API endpoint for your account.

#### GET Request:

Make a GET request to the following endpoint with your user credentials and account name:

https://gnip-api.twitter.com/metrics/usage/accounts/:account\_name.json

  
**Additional Parameters**  

|     |     |
| --- | --- |
| bucket | Optional. The unit of time for which usage data will be provided. Usage data can be returned with daily or monthly granularity.  <br>  <br>Requests made without a specified bucket will return monthly granularity.  <br>  <br>Options: 'month' or 'day' |
| fromDate (YYYYMMDDHHMM) | Optional. Usage data is only available starting from May 1, 2018. The oldest UTC timestamp from which the usage data will be provided. Timestamp is in day granularity and is inclusive (i.e., 201805010000 includes the 0501 day). Requests that contain values other than '0000' for hour and minute granularity will be defaulted to '0000'.  <br>  <br>Requests made without a fromDate or toDate will return usage data by month for the current month and include a historical reference for the past two months.  <br>  <br>**Please note:** Starting June 1, 2019, you can access the past 13 calendar months of usage data. For example, if it was the 10th of October, you can access usage data back to September 1st of the previous year.  <br>**Example:** 201810010000 will return data starting October 1st, 2018 onward, including October 1st. |
| toDate (YYYYMMDDHHMM) | Optional. The latest UTC timestamp to which the usage data will be provided. Timestamp is in day granularity and is not inclusive (i.e., 201703020000 does not include data for the 0302 day). When a toDate is specified for either the current day or a day in the future, usage data will be returned up to the last full day (UTC). Requests that contain values other than '0000' for hour and minute granularity will be defaulted to '0000'.  <br>  <br>A request with no toDate, will default to the next bucket (tomorrow for bucket=day and next month for bucket=month). A request made with no fromDate and toDate will default to bucket=month, and show data for the current month plus the two immediately previous months.  <br>  <br>**Example:** 201703050000 will return data to March 5, 2017, not including any data from March 5th. |

  
**Example GET Request**

This request will return data by month granularity from March 1, 2017 to March 5, 2017, not including any data from March 5, 2017.

curl -u "https://gnip-api.twitter.com/metrics/usage/accounts/:account\_name.json?bucket=month&fromdate=201403010000&toDate=201403150000"