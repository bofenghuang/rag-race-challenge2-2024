platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/


### Requirements

* For apps that have been granted the
    
    [`pages_read_engagement`](#)
    
    and
    
    [`pages_read_user_content`](#)
    
    permissions, only data owned by the Page is accessible.
    
* For apps that have been approved for either the
    
    [Page Public Content Access (PPCA)](#)
    
    or
    
    [Page Public Metadata Access (PPMA)](#)
    
    feature, only public data is accessible.
    
    [Learn more.](https://developers.facebook.com/docs/pages/overview/permissions-features#features)
    
* The `instagram_business_account` field requires a User access token from a User who is able to perform appropriate [tasks](https://developers.facebook.com/docs/instagram-api/overview#tasks) on the Page. Refer to the Instagram Graph API's [Page reference](https://developers.facebook.com/docs/instagram-api/reference/page) for more information.
    
* If using a [business system user](https://www.facebook.com/business/help/327596604689624) in your request, the [`business_management` permission](https://developers.facebook.com/docs/permissions/reference/business_management) may be required.
    

#### Limitations

* A Page access token is required for any fields that may include User information.
    
* All users requesting access to a Page using permissions must be able to perform the
    
    [`MODERATE` task](#)
    
    on the Page being queried.
    
* When using the Page Public Content Access feature, use a [system user access token](https://www.facebook.com/business/help/503306463479099) to avoid [rate limiting](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#pages) issues.
    
* If the page url is being used as the query input, ensure the page url is set up the following way: facebook.com/<pageusername>. More information on the [page username.](https://www.facebook.com/help/121237621291199)
    

#### Public Page Data

Requirements vary based on the Page's status, unpublished or published, and unrestricted or restricted. Restrictions include any visibility restrictions such as by age or region. Note that for restricted Pages, the app user must also satisfy any restrictions in order for data to be returned.

| Page Status | Access Token | Feature, to retrieve public data | Permissions, to retrieve Page owned data |
| --- | --- | --- | --- |
| Unpublished | [Page Access Token](https://developers.facebook.com/docs/facebook-login/access-tokens#pagetokens) or [User Access Token](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | None | None |
| Published, Unrestricted | [App Access Token](https://developers.facebook.com/docs/facebook-login/access-tokens#apptokens) or [User Access Token](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | PPCA or PPMA | [`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement) [`pages_read_user_content`](https://developers.facebook.com/docs/permissions/reference/pages_read_user_content) [`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list) |
| Published, Restricted | [Page Access Token](https://developers.facebook.com/docs/facebook-login/access-tokens#pagetokens) or [User Access Token](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens). | PPCA or PPMA | [`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement) [`pages_read_user_content`](https://developers.facebook.com/docs/permissions/reference/pages_read_user_content) [`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list) |