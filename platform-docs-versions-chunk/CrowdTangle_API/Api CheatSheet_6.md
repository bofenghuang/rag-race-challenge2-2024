platform: CrowdTangle
topic: API
subtopic: Api CheatSheet
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/Api CheatSheet.md
url: https://help.crowdtangle.com/en/articles/3443476-api-cheat-sheet


## /posts

* This endpoint lets you stream data from posts in a List or Saved Search. It’s as if you were looking at a List or Saved Search in your Dashboard. **It does not let you search the entire CT database -- if you do not specify a ListID, this endpoint will search through all the lists in your dashboard.**
    
* You can search for terms within the List or Saved Search using Boolean syntax with the SearchTerm parameter.
    
* Make sure to grab your ListID from the URL or the /lists endpoint in order to pull in posts -- this ID exists for both Lists and Saved Searches.
    

[](https://downloads.intercomcdn.com/i/o/248633578/44c6f1fd031f9416baca101a/Screen+Shot+2020-09-22+at+11.58.48+AM.png?expires=1620880985&signature=f7f6c83c2f65374017c5d458ee6b0f6d9b30ee69f6200fd10a3ecef6572ea82d)

* You can use Weights just like in a List or Saved Search in the Dashboard, on a scale of 1-10
    
* The default number of posts returned at a time is 10. The _count_ parameter can only go to between 1-100 -- paginate using the _offset_ parameter to view all posts. 
    
* Use the _includeHistory_ parameter to get time-series data for each post -- this is the same data you get when you download a single post CSV in the UI. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle.
    
* Use the _accounts_ parameter to search by the account handle or platform ID.