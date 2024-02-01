platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/ad_accounts/create)Create ad account

Create a new ad account. Different ad accounts can support different currencies, payment methods, etc. An ad account is needed to create campaigns, ad groups, and ads; other accounts (your employees or partners) can be assigned business access and appropriate roles to access an ad account.

You can set up up to 50 ad accounts per user. (The user must have a business account to create an ad account.)

For more, see [Create an advertiser account](https://help.pinterest.com/en/business/article/create-an-advertiser-account).

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### Request Body schema: application/json

Ad account to create.

|     |     |
| --- | --- |
| country | string (Country)<br><br>Enum: "AD" "AE" "AF" "AG" "AI" "AL" "AM" "AO" "AQ" "AR" "AS" "AT" "AU" "AW" "AX" "AZ" "BA" "BB" "BD" "BE" … 228 more<br><br>Country ID from ISO 3166-1 alpha-2. |
| name | string (name) <= 256 characters<br><br>Ad Account name. |
| owner\_user\_id | string (owner\_user\_id) ^\\d+$<br><br>Advertiser's owning user ID. |