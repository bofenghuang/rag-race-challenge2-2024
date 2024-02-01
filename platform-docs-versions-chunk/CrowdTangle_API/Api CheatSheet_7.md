platform: CrowdTangle
topic: API
subtopic: Api CheatSheet
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/Api CheatSheet.md
url: https://help.crowdtangle.com/en/articles/3443476-api-cheat-sheet

## /post/:id

* Retrieves a specific post according to its Facebook ID. [Read more about the endpoint here](https://github.com/CrowdTangle/API/wiki/Posts#get-postid).
    
* Use the _includeHistory_ parameter to get time-series data for each post -- this is the same data you get when you download a single post CSV in the UI. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle.
    

## /ctpost/:id

* Retrieves a specific post according to its CrowdTangle ID. [Read more about the endpoint here.](https://github.com/CrowdTangle/API/wiki/Posts#endpoint---crowdtangle-id) 
    
* Use the _includeHistory_ parameter to get time-series data for each post -- this is the same data you get when you download a single post CSV in the UI. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle.