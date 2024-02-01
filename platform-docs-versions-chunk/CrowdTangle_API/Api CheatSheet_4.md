platform: CrowdTangle
topic: API
subtopic: Api CheatSheet
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/Api CheatSheet.md
url: https://help.crowdtangle.com/en/articles/3443476-api-cheat-sheet


# Some helpful tips for getting the best API experience:

**For all endpoints, use the _start date_ and _end date_ parameters to prevent CrowdTangle from crashing and to reduce load times.**

**Use a Facebook Dashboard token to call Facebook posts, and an Instagram Dashboard token to call Instagram posts** \-- you unfortunately can't use the same token across different platforms.

**Number of posts returned and pagination**

* /posts and /posts/search will max out at 10,000 posts returned. /links will max out at 1000 posts returned. You must paginate through those posts to reach the end of the query,
    
* You can see up to 100 posts at a time (_count_ parameter goes up to 100). To see the next one hundred posts, paginate using the _offset_ parameter. For example: set _count_ = 100 to see posts 1-100. Then, set _count_ = 100 and _offset_ = 100 to see posts 101 - 200. Continue increasing the _offset_ parameter in successive calls to see all posts.
    
* Each pagination will count against your rate limit. Slice thinly by date or SQL timeframe to separate your results into ~10k batches so you don't miss any data. To get more than 10k posts at a time, use Historical Data in the Dashboard rather than the API.
    

**Making sure you get all posts for a given time period**

* **Make sure to sort by Date to capture all posts.** If you don’t specify the _sortby_ parameter, the API will by default return posts sorted by Overperforming. This will exclude posts that are Underperforming.
    

**Default rate limits and settings:**

* **/posts/search is not enabled by default.**
    
* **Rate limit defaults:** 6 calls/min for all but /links, which is 2 calls/min.
    
* **By default, the API object names do not match the CSV headers. This cannot be changed.**
    
* **The API uses the UTC timezone. This cannot be changed.** The CrowdTangle User Interface allows the user to change the time zone of their dashboard, so always account for time zone differences when comparing results in the API and UI.
    
* **By default, the subscriberCount property will show page Followers** (as of January 26, 2021). You can select either Page Likes or Followers in your Dashboard settings. [Learn more here](https://help.crowdtangle.com/en/articles/4797890-faq-measuring-followers).
    

**Platform IDs**

* **Platform IDs are external IDs native to the selected platform (Facebook, Instagram).** You can use our API (/posts or /leaderboard, for example) to programmatically fetch platformIDs for each account in a List or Dashboard you're interested in. If the post is from Facebook, you can also find the Platform ID in the URL of the post. For example, this url [https://www.facebook.com/81221197163/posts/10158939904512164](https://www.facebook.com/81221197163/posts/10158939904512164) has a platformID of _81221197163\_10158939904512164._