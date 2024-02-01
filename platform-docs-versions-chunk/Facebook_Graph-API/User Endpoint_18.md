platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/accounts/

# User Accounts

The Facebook Pages that a person owns or is able to perform tasks on.

## Reading

Pages the User has a role on

### Permissions

A Page access token for a User with a role (other than Live Contributor) on the Page and the following permissions:

* The `pages_show_list` permission
    
* To access accounts using a `business_id` or for a user who owns any business Pages, the app must be approved for the [`business_management` permission](https://developers.facebook.com/docs/apps/review/login-permissions#business-management).
    

**Note:** In order for a Page to be returned, the User must also grant the app running the query the `pages_show_list` permissions for that Page.

### Limitations

* **It does not return pages that you are connected with through a business. To retrieve pages that you are connected with via businesses, the `business_management` permission is required**