platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/lists


## [](#get-lists)GET /lists

Retrieve the lists, saved searches and saved post lists of the dashboard associated with the token sent in.

#### [](#endpoint)Endpoint

`GET https://api.crowdtangle.com/lists`

#### [](#parameters)Parameters

This endpoint accepts no parameters other than the token.

#### [](#response)Response

The Response contains both a status code and a result. The status will always be 200 if there is no error. The result contains an array of list objects.

    //Call: https://api.crowdtangle.com/lists?token=TOKEN
    {
        "status": 200,
        "result": {
            "lists": [
                {
                    "id": 1172985,
                    "title": "Music Media & Artist Pages",
                    "type": "LIST"
                },
                {
                    "id": 1177583,
                    "title": "Television",
                    "type": "LIST"
                },
                {
                    "id": 1191568,
                    "title": "candidato presidencial, presidente, elección",
                    "type": "SAVED_SEARCH"
                },
                {
                    "id": 1224851,
                    "title": "Test",
                    "type": "SAVED_POSTS"
                },
                {
                    "id": 1391155,
                    "title": "Women of the US Senate",
                    "type": "LIST"
                },
                {
                    "id": 1394602,
                    "title": "coronavirus, 2019nCoV, covid19, covid-19, covid",
                    "type": "SAVED_SEARCH"
                },
                {
                    "id": 1424665,
                    "title": "2020 US Election",
                    "type": "LIST"
                },
                {
                    "id": 1447044,
                    "title": "APAC Media",
                    "type": "LIST"
                }
                
            ]
        }
    }