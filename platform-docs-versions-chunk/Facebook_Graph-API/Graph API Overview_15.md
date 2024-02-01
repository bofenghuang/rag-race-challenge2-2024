platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/access-levels

# Access Levels

This document is only applicable to apps created using an App Type.

**[Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#advanced-access) now requires Business Verification**

As of February 1, 2023 apps requesting [advanced access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#advanced-access) for permissions may have to be connected to a verified business. [See this blog post for more information.](https://developers.facebook.com/blog/post/2023/02/01/developer-platform-requiring-business-verification-for-advanced-access/)

Access levels are an additional layer of Graph API authorization that apply to [permissions](https://developers.facebook.com/docs/permissions/reference) and [features](https://developers.facebook.com/docs/apps/features-reference) for [Business](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#business), [Consumer](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#consumer), and [Gaming](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#gaming-services) apps.

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/130946061_668701493796906_1998528720072373367_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=pdXGPxVtMVwAX-S7_bh&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDNvWmLhyXL_MMlkjbYrrGpK9s_yc0dOHJGJYt8PSsKQA&oe=65D578A0)

There are two access levels: [Standard](#standard-access) and [Advanced](#advanced-access). Apps can request permissions with Advanced Access from any app user, and features with Advanced Access are active for all app users. Permissions with Standard Access, however, can only be requested from app users who have a role on the requesting app, and features with Standard Access are only active for app users who have a role on the app.

If your app will only be used by people who have a role on it, the permissions and features your app requires will only need Standard Access. If your app will be used by people who do not have a role on it, the permissions and features that your app requires will need Advanced Access.

All Business, Consumer, and Gaming apps are automatically approved for Standard Access for all permissions and features. Advanced Access, however, must be approved on an individual permission and feature basis through the [App Review](https://developers.facebook.com/docs/app-review) process.