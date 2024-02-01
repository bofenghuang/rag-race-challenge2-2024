platform: TikTok
topic: Research-API
subtopic: Research API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Documentation.md
url: https://developers.tiktok.com/doc/research-api-faq/


## Research API Usage FAQs

1. **Why does User** **API** **not return responses sometimes even though the user name is accurate?**

1. TikTok's Research API does have some filters. To cite some examples, public data of users under the age of 18 and data from Canada is not returned in the responses

3. **Why is my access token invalid?**

1. Access tokens are set to expire every two hours. If you experience an invalid token error within two hours of generating it, please submit a support ticket to us with your token and client key, and we will investigate the issue.

5. **Why did I receive a response back with code: "scope\_not\_authorized" and message: "The user did not authorize the scope required for completing this request?"**

1. This indicates that you have not yet submitted your Research API application for our review and have not passed the necessary approval evaluations. If you are interested in accessing the Research API, visit our [Research API](https://developers.tiktok.com/products/research-api/) page to learn more, check eligibility requirements and apply for access.

7. **Why is the query video data (view\_count, comment\_count, like\_count, share\_count) significantly inaccurate, often showing lower numbers than what is live at the moment?**

1. The User info API only retrieves data for an individual user, so we use online data. However, the video query API searches for the full dataset, so we use archived data instead of the current online data. New videos take up to 48 hours to be added to the search engine, and statistics such as view count and follower count can take up to 10 days to update.