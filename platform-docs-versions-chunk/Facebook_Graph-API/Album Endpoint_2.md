platform: Facebook
topic: Graph-API
subtopic: Album Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Album Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/album/


### Requirements

Requirements depend on the type of node that the Album is on.

| Requirement | User nodes | Page nodes | Group nodes |
| --- | --- | --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | Any | Any | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | None | To get public Page content of Pages you can not [perform a task](https://developers.facebook.com/docs/pages/overview#tasks) on, you will need [`Page Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-PAGES_ACCESS) | None |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`user_photos`](https://developers.facebook.com/docs/apps/review/login-permissions#user-photos) | Unpublished Pages:<br><br>* You must be able to [perform the `CREATE` task](https://developers.facebook.com/docs/pages/overview#tasks) on the Page<br>    <br>* [`pages_read_engagement`](https://developers.facebook.com/docs/pages/overview#tasks)<br>    <br><br>Published Pages:<br><br>* [`pages_read_engagement`](https://developers.facebook.com/docs/pages/overview#tasks) | None |
| [Group Roles](https://www.facebook.com/help/1686671141596230?helpref=about_content) | Not applicable | Not applicable | Admin |