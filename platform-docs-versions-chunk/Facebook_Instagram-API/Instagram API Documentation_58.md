platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/copyright-detection


### Sample Responses

|     |     |
| --- | --- |
| #### Violation found<br><br>{<br>  "copyright\_check\_information": {<br>     "status": {<br>       "status": "complete",<br>       "matches\_found": true<br>     },<br>     "copyright\_matches": \[<br>       {<br>         "content\_title": "In My Feelings",<br>         "author": "Drake",<br>         "owner\_copyright\_policy": {<br>           "name": "UMG",<br>           "actions": \[<br>             {<br>               "action": "BLOCK",<br>               "territories": "3",<br>               "geos": \[<br>                 "Canada",<br>                 "India",<br>                 "United States of America"<br>               \]<br>             },<br>             {<br>               "action": "MUTE",<br>               "territories": "4",<br>               "geos": \[<br>                 "Taiwan",<br>                 "Tanzania",<br>                 "Saudi Arabia",<br>                 "United Kingdom of Great Britain and Northern Ireland"<br>               \]<br>             }<br>           \]<br>         },<br>         "matched\_segments": \[<br>          {<br>            "start\_time\_in\_seconds": 2.4,<br>            "duration\_in\_seconds": 5.1,<br>            "segment\_type": "AUDIO"<br>          },<br>          {<br>            "start\_time\_in\_seconds": 10.2,<br>            "duration\_in\_seconds": 4.5,<br>            "segment\_type": "VIDEO"<br>          }<br>        \]<br>      }<br>    \]<br>  },<br>  "id": "90012800291314"<br>} | #### No violation found<br><br>{<br>  "copyright\_check\_information": {<br>    "status": {<br>      "status": "complete",<br>      "matches\_found": false<br>    }<br>  },<br>  "id": "{ig-media-id}"<br>} |

[](#)