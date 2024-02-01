platform: CrowdTangle
topic: API
subtopic: Api CheatSheet
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/Api CheatSheet.md
url: https://help.crowdtangle.com/en/articles/3443476-api-cheat-sheet

## /leaderboard

* This acts like Lists Leaderboard -- **NOT** Search Leaderboard. You will not get a list of the number of posts that match your search parameters through this endpoint.
    

## /links

* This endpoint acts like the Chrome Extension. However, it will pull in Facebook, Instagram
    
* You can specify the number of posts to pull in - the maximum is 1000. 
    
* Set the _summary_ parameter to “true” to get the top-line summary of interactions for the link.
    
* Use the _includeHistory_ parameter to get time-series data for each post -- this is the same data you get when you download a single post CSV in the UI. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle.
    
* The _SearchField_ parameter allows you to search for URLs with query strings.