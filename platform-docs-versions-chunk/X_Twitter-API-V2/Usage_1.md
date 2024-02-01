platform: X
topic: Twitter-API-V2
subtopic: Usage
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Usage.md
url: https://developer.twitter.com/en/docs/twitter-api/usage/tweets/introduction

Introduction

## Introduction

The Usage API in the Twitter API v2 allows developers to programmatically retrieve their project usage. Using thie endpoint, developers can keep a track and monitor of the number of Tweets they have pulled for a given billing cycle.

Developers can use the GET endpoint to get the daily project usage for upto the last 90 days. The usage can also be aggregated per client app connected to your peoject.

There is a app rate limit of 50 requests per 15 minutes for this GET endpoint.