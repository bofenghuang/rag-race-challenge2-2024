platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/rate-limiting


### Content Library API

If you reach the maximum number of queries per minute (rate limit) in Content Library API, you will see a log message indicating that the system will retry your last request after a wait time.

This is an example of what the message looks like:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/398010007_1547315062763139_1392026401103332627_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=NP6X6VD0OGAAX_SFTrM&_nc_ht=scontent-cdg4-3.xx&oh=00_AfCKU1SWTvndm9HaBhS17f_-tgq-DlUDoXfLdebijXhc5A&oe=65BEBA05)  
  

If you reach the maximum number of data records retrieved per seven-day rolling window (query budget), you will see an error message indicating that you have reached your allotted query budget and recommending that you retry your latest query later. In this case, the system does not handle retrying the request for you.

This is an example of what the message looks like:

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/397449533_1025873445329811_6969197869066569786_n.png?_nc_cat=107&ccb=1-7&_nc_sid=f537c7&_nc_ohc=WGs01JS5DaoAX99umgY&_nc_ht=scontent-cdg4-2.xx&oh=00_AfA-ykVKwerwXBPSK7bVPoxU_JiaLodSeBRU3qLLiqUcRA&oe=65BEE104)