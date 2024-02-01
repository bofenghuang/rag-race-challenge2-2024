platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/secure-requests

# Secure Graph API Calls

Almost every Graph API call requires an [access token](https://developers.facebook.com/docs/facebook-login/access-tokens/). Malicious developers can steal access tokens and use them to send spam from your app. Meta has automated systems to detect this, but you can help us secure your app. This document covers some of the ways you can improve security in your app.

## Meta Crawler

A number of platform services such as Social Plugins and Open Graph require our systems to be able to reach your web pages. We recognize that there are situations where you might not want these pages on the public web, during testing or for other security reasons.

We've provided information on IP allow lists and User Agent strings for Meta's crawlers in our [Meta Crawler guide](https://developers.facebook.com/docs/sharing/webmasters/crawler).