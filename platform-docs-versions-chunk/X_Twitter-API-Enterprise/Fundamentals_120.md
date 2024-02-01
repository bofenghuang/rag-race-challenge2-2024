platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo

### Sample Payload

{
    "user": {
        "derived": {
            "locations": \[
                {
                    "country": "United States",
                    "country\_code": "US",
                    "locality": "Birmingham",
                    "region": "Alabama",
                    "sub\_region": "Jefferson County",
                    "full\_name": "Birmingham, Alabama, United States",
                    "geo": {
                        "coordinates": \[
                            -86.80249,
                            33.52066
                        \],
                        "type": "point"
                    }
                }
            \]
        }
    }
}