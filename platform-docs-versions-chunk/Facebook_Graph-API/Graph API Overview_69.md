platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/get-started


### Step 2. Add a Permission

|     |     |
| --- | --- |
| In the right side panel, under **Permissions**, click the **Add a Permission** dropdown menu. Click **User Data Permissions** and select **email**.<br><br>#### Generate A New User Access Token<br><br>Because you are changing the scope of the access token, you need to create a new one. Click **Generate Access Token**. Just like your first request, you must give your app permission to access your email in the Facebook Login dialog.<br><br>Once the new token has been created, click **Submit**. Now all fields in your request will be returned. | ![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/234580746_367949518031866_340317674627083357_n.png?_nc_cat=104&ccb=1-7&_nc_sid=e280be&_nc_ohc=EO1oTfdZnowAX9PiTuu&_nc_ht=scontent-cdg4-3.xx&oh=00_AfBesoVPqGkmS8wiSiPci4OCdvw0g0V7uzyk4d6fyOFWYQ&oe=65D5639E) |

Try getting your Facebook posts.

[See the steps.](#)

#### Links in the Response

Notice that `id` values returned in the response window are links. These links can represent nodes, such as User, Page, or Post. If you click on a link, the ID will replace the contents of the query string field. Now you can run requests on that node. Because this node is connected to the parent node, a Post of a User, you may not need to add permissions. You can click on a Post ID now since we will be using it in the next example.

Notice: Some IDs are a combination of the parent ID and a new ID string. For example, a User's Post will have a Post ID that looks something like this: `1028223264288_102224043055529` where `1028223264288` is the User ID.