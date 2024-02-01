platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin%2Fcontext


## Selecting all child fields and fully expanding a child field containing a URN

**`(person(current_position(*,company~)))`**

    {
        "person": {
            "current_position": {
                "company": "urn:li:company:1",
                "company~": {
                    "active": true,
                    "administrators": [
                        "urn:li:person:6611647"
                    ],
                    "allEmployeesAsAdmins": false,
                    "attributes": {
                        "disableThirdPartyNews": false,
                        "enableStatusUpdate": false,
                        "owns300x250RightAdSlot": false,
                        "paidCareers": false,
                        "paidGoldPlusCareers": false,
                        "paidPlatinumCareers": false,
                        "paidProducts": false,
                        "paidSilverCareers": false,
                        "paidSilverPlusCareers": false,
                        "showAnalytics": false,
                        "showBrandTree": false,
                        "showNews": true,
                        "showPastEmployees": false,
                        "silverProducts": false,
                        "useParentCareers": false
                    },
                    "companyId": 1,
                    "companyType": "PUBLIC_COMPANY",
                    "creationTime": 1375816467585,
                    "creator": "urn:li:person:6611647",
                    "dataVersion": 4,
                    "descriptions": [
                        {
                            "description": "test test test testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest test",
                            "locale": "en_US"
                        }
                    ],
                    "employeeCountRange": "MYSELF_ONLY",
                    "heroImage": {
                        "cropHeight": 220,
                        "cropWidth": 646,
                        "cropXPosition": 0,
                        "cropYPosition": 0,
                        "croppedImage": "urn:li:media:/p/2/005/045/187/3d49ef0.png",
                        "height": 220,
                        "uncroppedImage": "urn:li:media:/p/2/005/045/187/3b333d8.png",
                        "width": 646
                    },
                    "images": [
                        {
                            "originalMedia": "urn:li:media:/p/2/005/045/188/1d5f329.png",
                            "type": "SQUARE_LOGO_LEGACY",
                            "urn": "urn:li:media:/p/2/005/045/188/1d5f329.png"
                        },
                        {
                            "originalMedia": "urn:li:media:/p/2/005/045/188/24809b3.png",
                            "type": "LOGO_LEGACY",
                            "urn": "urn:li:media:/p/2/005/045/188/24809b3.png"
                        }
                    ],
                    "industries": [
                        "ACCOUNTING"
                    ],
                    "lastEditor": "urn:li:person:6611647",
                    "lastModifiedTime": 1375816467585,
                    "logo": "urn:li:media:/p/2/005/045/188/24809b3.png",
                    "names": [
                        {
                            "active": true,
                            "locale": "en_US",
                            "name": "r-NQkR5TwJ",
                            "type": "CANONICAL"
                        }
                    ],
                    "organizationalEntity": "urn:li:organization:1",
                    "squareLogo": "urn:li:media:/p/2/005/045/188/1d5f329.png",
                    "status": "OPERATING",
                    "stockSymbol": "",
                    "twitterId": "",
                    "universalName": "r-nqkr5twj",
                    "websiteUrl": "https://www.whatismyreferer.com/"
                },
                "from": "2009",
                "job_title": "SWE"
            }
        }
    }