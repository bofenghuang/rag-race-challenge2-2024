platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/webhook-validation?context=linkedin%2Fcontext

### Re-validation and Blocked Endpoints

Webhook endpoints will be periodically re-validated after the initial validation every 2 hours. If the re-validation check fails 3 times in a row, the endpoint will move to a blocked state where events will no longer be sent.

Developers associated with that developer application will receive warning emails for any failed validation attempts. After re-validation checks fail 3 times in a row, an email will be sent notifying developers that the webhook has been blocked. The endpoint will also show as "Blocked" in the developer portal.

After resolving the issue, developers can manually kick off another validation check from the developer portal.