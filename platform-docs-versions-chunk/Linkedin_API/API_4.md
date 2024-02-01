platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access?context=linkedin%2Fcontext


## Marketing

Developers seeking to build a marketing related integration using Advertising APIs permissions must be approved. You can apply for access through the [Developer Portal](https://www.linkedin.com/developers/). This can be done by selecting your app from [My Apps](https://www.linkedin.com/developers/apps), navigate to the Products tab, and add the Marketing Developer Platform product. Qualifications to be an Advertising APIs partner are available at [Become a Partner](https://business.linkedin.com/marketing-solutions/marketing-partners/become-a-partner/marketing-developer-program).

Audiences permissions may be applied for after being an approved Marketing Developer Platform partner. Contact support or your partner rep for application information.

| Product/Program | Permission | Description |
| --- | --- | --- |
| Advertising APIs | rw\_organization\_admin | **Member Auth**: Manage an authenticated member’s company pages and retrieve reporting data. |
| Advertising APIs | r\_organization\_admin | **Member Auth**: Retrieve an authenticated member’s company pages and their reporting data. |
| Advertising APIs | w\_organization\_social | **Member Auth**: Post, comment and like posts on behalf of an organization. Restricted to organizations in which the authenticated member has one of the following company page roles.* `ADMINISTRATOR`<br>* `DIRECT_SPONSORED_CONTENT_POSTER`<br>* `LEAD_GEN_FORMS_MANAGER` |
| Advertising APIs | r\_organization\_social | **Member Auth**: Retrieve organizations' posts, comments, and likes. |
| Marketing Developer Platform (MDP) | w\_member\_social | **Member Auth**: Post, comment, and like posts on behalf of an authenticated member. |
| Advertising APIs | rw\_ads | **Member Auth**: Manage and read an authenticated member's ad accounts. Restricted to ad accounts in which the authenticated member has one of the following ad account roles.* `ACCOUNT_BILLING_ADMIN`<br>* `ACCOUNT_MANAGER`<br>* `CAMPAIGN_MANAGER`<br>* `CREATIVE_MANAGER` |
| Advertising APIs | r\_ads | **Member Auth**: Read an authenticated member's ad accounts. Restricted to ad accounts in which the authenticated member has one of the following ad account roles:<br><br>* `ACCOUNT_BILLING_ADMIN`<br>* `ACCOUNT_MANAGER`<br>* `CAMPAIGN_MANAGER`<br>* `CREATIVE_MANAGER`<br>* `VIEWER` |
| Advertising APIs | r\_ads\_reporting | **Member Auth**: Retrieve reporting for advertising accounts. |
| Advertising APIs | r\_1st\_connections\_size | **Member Auth**: Retrieve the count of an authenticated member's 1st-degree connections. |
| Advertising APIs | r\_basicprofile | **Member Auth**: Read an authenticated member's basic profile including name, photo, headline, and public profile URL. |
| Lead Sync | r\_marketing\_leadgen\_automation | **Member Auth**: Access your lead generation forms and retrieve leads (including event leads, ad leads, and organization page leads). |
| Audiences | rw\_dmp\_segments | **Member Auth**: Create and manage matched audiences. |