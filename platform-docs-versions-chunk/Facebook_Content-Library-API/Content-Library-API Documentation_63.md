platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-ig-accounts


### Search for Instagram accounts by account ID

You can search for Instagram accounts using specific account IDs obtained from previous account searches.

To get data on specific Instagram accounts that contain specific keywords or phrases, create a search object using the `search_ig_accounts()` method with the `q` parameter (specifying the keywords or phrases) and the `account_ids` parameter (specifying the list of account IDs you want included). If you omit the `q` argument, all accounts in the list of IDs are included, not just those with a specific keyword or phrase.

RPython

    # Create a search object limiting the response to specific account IDs 
            account_search <- client$search_ig_accounts(q=`fifa`, account_ids=[`315242517956050`], fields=`id,name,creation_date`)

    # Create a search object limiting the response to specific account IDs 
            account_search=client.search_ig_accounts(q=`fifa`, account_ids=[`315242517956050`], fields=`id,name,creation_date`)

For using Instagram account IDs to search for posts from specific Instagram accounts, see [Guide to Instagram posts data](https://developers.facebook.com/docs/content-library-api/guide-ig-posts).