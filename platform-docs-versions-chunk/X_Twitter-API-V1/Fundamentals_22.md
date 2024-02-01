platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/geo


### Tweet with exact location

    {
      "geo": {
        "type": "Point",
        "coordinates": [
          40.74118764,
          -73.9998279
        ]
      },
      "coordinates": {
        "type": "Point",
        "coordinates": [
          -73.9998279,
          40.74118764
        ]
      },
      "place": {
        "id": "01a9a39529b27f36",
        "url": "https://api.twitter.com/1.1/geo/id/01a9a39529b27f36.json",
        "place_type": "city",
        "name": "Manhattan",
        "full_name": "Manhattan, NY",
        "country_code": "US",
        "country": "United States",
        "bounding_box": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                -74.026675,
                40.683935
              ],
              [
                -74.026675,
                40.877483
              ],
              [
                -73.910408,
                40.877483
              ],
              [
                -73.910408,
                40.683935
              ]
            ]
          ]
        },
        "attributes": {
          
        }
      }
    }