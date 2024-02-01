platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/get-started


### Step 2. Generate an Access Token

Click the **Generate Access Token** button. A **Log in With Facebook** window will pop up. This popup is your app asking for your permission to get your name and profile picture from Facebook.

|     |     |
| --- | --- |
| This flow is our [Facebook Login](https://developers.facebook.com/docs/facebook-login) product that allows a person to log into an app using their Facebook credentials. Facebook Login allows an app to ask a person to access the person's Facebook data, and for the person to accept or decline access. Your name and profile picture are public, to allow people to find you on Facebook, so no additional requirements are needed to run this request.<br><br>Click **Continue as...**<br><br>A User Access Token is created. This token contains information such as the app making the request, the person using the app to make a request, if the access token is still valid (it expires in about an hour), the expiration time, and the scope of data the app can request. In this request the scope is `public_profile` which includes your name and profile picture. | ![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/231956490_308313234407833_1605768375436620205_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=hbftUPteRbYAX_D7LLx&_nc_ht=scontent-cdg4-3.xx&oh=00_AfC3hs11ArhwMcojKlD1lXsFnbRHJ-SuhtXtjWgIxQbtCQ&oe=65D585AE) |

|     |     |
| --- | --- |
| ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/232991718_592378688435455_3147910228443606263_n.png?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=8uWNMGbSDoAAX-_x18G&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDSkL2isgCmFyaVEMCuxvPYmv043i2rXkO8jLqaKNCz2A&oe=65D58A34) | Click the information circle icon next to the acces token to view the token's information. |