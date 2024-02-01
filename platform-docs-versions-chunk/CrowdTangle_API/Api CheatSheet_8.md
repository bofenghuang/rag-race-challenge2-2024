platform: CrowdTangle
topic: API
subtopic: Api CheatSheet
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/Api CheatSheet.md
url: https://help.crowdtangle.com/en/articles/3443476-api-cheat-sheet


## /posts/search

* This endpoint acts like Historical Data, but with more nuanced search terms. It lets you search **the entire CT database.** You can differentiate account types using the _accountTypes_ parameter.
    
* The _SearchField_ parameter allows you to search for URLs with query strings, image text only, and account names, in addition to the usual post text and image text.
    
* /posts/search does not support regular expressions, or any sort of wildcard search.
    
* You can pull in from Lists and Saved Search by using the _ListID_ parameter, just like in the /posts endpoint. You can also pull in from Account using _AccountID_ parameter.
    
* You can use "OR," “AND” and “NOT” for terms and Lists to search, but you cannot use Weights. 
    
* Most of the functionality you’d want from this is easily available by setting up a Saved Search in your Dashboard, and pulling it in through the /posts endpoint.
    
* The default number of posts returned at a time is 10. The _count_ parameter can only go to between 1-100 -- paginate using the _offset_ parameter to view all posts. 
    
* Use the _includeHistory_ parameter to get time-series data for each post -- this is the same data you get when you download a single post CSV in the UI. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle.
    
* Use the _accounts_ parameter to search by the account handle or platform ID.
    
* If you submit a query with a blank searchTerm (i.e., searchTerm=" "), the result set will be limited to the Dashboard associated with the supplied API token. System-wide blank searches are not supported by default. Please reach out to [support@crowdtangle.com](mailto:support@crowdtangle.com) for more information.