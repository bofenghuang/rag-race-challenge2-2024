platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling?context=linkedin%2Fcontext

## 429 Rate Limit

On LinkedIn's platform, all API requests that you make are [rate limited](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/rate-limits?context=linkedin/context) to prevent abuse and to ensure service stability. These errors will return an error message of "Resource level throttle limit for calls to this resource is reached." If you get a `429 Rate Limit` error, check if too many redundant calls are being made and review your application’s Usage & Limits in the Developer Portal. If you've confirmed that the current rate limits do not meet your application’s needs, contact us if you are our partner, or join our partner program through [https://developer.linkedin.com/partner-programs](https://developer.linkedin.com/partner-programs).

In rare cases, LinkedIn may also return a 429 response as part of infrastructure protection. API service will return to normal automatically.