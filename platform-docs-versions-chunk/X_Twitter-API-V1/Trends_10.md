platform: X
topic: Twitter-API-V1
subtopic: Trends
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Trends.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/trends/locations-with-trending-topics/api-reference/get-trends-available


## Example Response[¶](#example-response "Permalink to this headline")

    [
      {
        "country": "Sweden",
        "countryCode": "SE",
        "name": "Sweden",
        "parentid": 1,
        "placeType": {
          "code": 12,
          "name": "Country"
        },
        "url": "http://where.yahooapis.com/v1/place/23424954",
        "woeid": 23424954
      },
      {
        "country": "United States",
        "countryCode": "US",
        "name": "New Haven",
        "parentid": 23424977,
        "placeType": {
          "code": 7,
          "name": "Town"
        },
        "url": "http://where.yahooapis.com/v1/place/2458410",
        "woeid": 2458410
      },
      {
        "country": "Japan",
        "countryCode": "JP",
        "name": "Sapporo",
        "parentid": 23424856,
        "placeType": {
          "code": 7,
          "name": "Town"
        },
        "url": "http://where.yahooapis.com/v1/place/1118108",
        "woeid": 1118108
      },
      ...
      {
        "country": "United States",
        "countryCode": "US",
        "name": "Providence",
        "parentid": 23424977,
        "placeType": {
          "code": 7,
          "name": "Town"
        },
        "url": "http://where.yahooapis.com/v1/place/2477058",
        "woeid": 2477058
      },
      {
        "country": "United States",
        "countryCode": "US",
        "name": "Cincinnati",
        "parentid": 23424977,
        "placeType": {
          "code": 7,
          "name": "Town"
        },
        "url": "http://where.yahooapis.com/v1/place/2380358",
        "woeid": 2380358
      }
    ]