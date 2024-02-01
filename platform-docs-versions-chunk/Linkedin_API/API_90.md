platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/webhook-validation?context=linkedin%2Fcontext

# Webhooks

Webhooks allow you to receive real-time HTTP notifications for subscribed events. This functionality is only available for applications with an approved use case for webhooks.

## Webhook Registration and Validation

Notifications will only be sent to webhooks that are registered and validated.

To begin, register your webhook in the "Webhooks" tab of your application in the [developer portal](https://www.linkedin.com/developers/apps).

Note

The Webhooks tab is only enabled for applications with a use case for webhooks. For Lead Syncing use cases, webhook subscriptions must be created via the Lead Notification Subscriptions API and cannot be created via the UI.