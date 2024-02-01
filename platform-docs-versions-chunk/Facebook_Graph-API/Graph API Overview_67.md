platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/get-started

### Step 3. Submit the Request

Click the **Submit** button in the upper right corner.

#### What You Should See

In the [Response Window](https://developers.facebook.com/docs/graph-api/guides/explorer#response-window), you will see a JSON response with your Facebook User ID and your name.

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/232902382_904467853476103_7217229934737479641_n.png?_nc_cat=105&ccb=1-7&_nc_sid=e280be&_nc_ohc=yzqX1kwM9ckAX_Wm0-Z&_nc_oc=AQkpX8mi-4tMVmdYiKrLKBbUe96pnBfjkyV2LDDjl9vMU-R14_vmjb9a6STN6OIu3nY&_nc_ht=scontent-cdg4-1.xx&oh=00_AfCsn5fx7bM1kd4Ehh3crciBFe5GlbgyWp1b4UeIXQ3hjw&oe=65D57D63)

If you remove `?fields=id,name` from the query string field and click **Submit**, you will see the same result since `name` and `id` are the User node fields returned by default.

## Your Second Request