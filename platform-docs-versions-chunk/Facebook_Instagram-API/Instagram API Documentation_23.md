platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/getting-started


## 3\. Get a User Access Token

Once you've implemented Facebook Login, make sure you are signed into your Facebook Developer account, then access your app and trigger the Facebook Login modal. Remember, your Facebook Developer account must be able to perform [Tasks](https://developers.facebook.com/docs/instagram-api/overview#tasks) on the [Facebook Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the Instagram account you want to query.

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/57343078_287134128874563_1329098073791528960_n.png?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=SXKqtpgjOXUAX-DKTg5&_nc_ht=scontent-cdg4-2.xx&oh=00_AfCpG6WFDSl_A_30lpI6kBhBeiEsfJLa6MGVOsqPlNLnLA&oe=65D576B9)

Once you have triggered the modal, click **OK** to grant your app the `instagram_basic` and `pages_show_list` permissions.

The API should return a User access token. Capture the token so your app can use it in the next few queries. If you are using the Graph API Explorer, it will be captured automatically and displayed in the **Access Token** field for reference:

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/57308062_276123556625959_4652658984229011456_n.png?_nc_cat=110&ccb=1-7&_nc_sid=e280be&_nc_ohc=GSL2E_feeZcAX90FAt9&_nc_ht=scontent-cdg4-1.xx&oh=00_AfClWFOu8mhz-uUY70lzoDYELYgHDnjY5I6tKMh28xYv2w&oe=65D5899F)

[](#)