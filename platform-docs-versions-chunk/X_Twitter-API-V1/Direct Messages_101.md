platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/custom-profiles/api-reference/new-profile

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **name** (required) | The string ID of of the custom profile. 48 characters max length. |
| **avatar.media.id** (required) | The string ID of the media to associate with the profile. See [Uploading Media](https://developer.twitter.com/en/docs/media/upload-media/overview) for further details on generating a media ID. |

## Example Request[¶](#example-request "Permalink to this headline")

    {
      "custom_profile": {
        "name": "Jon C, Partner Engineer",
        "avatar": {
            "media": {
               "id": "1234"
           }
        }
    }

### Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -A 'Content-type: application/json' /1.1/custom_profiles/new.json -d ' { "custom_profile": { "name": "Jon C, Partner Engineer", "avatar": { "media": { "id": "1234" } } }'