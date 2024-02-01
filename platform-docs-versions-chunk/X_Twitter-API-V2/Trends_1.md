platform: X
topic: Twitter-API-V2
subtopic: Trends
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Trends.md
url: https://developer.twitter.com/en/docs/twitter-api/trends/introduction

Introduction

## Introduction

The Trends lookup endpoint allow developers to get the Trends for a location, specified using the where-on-earth id (WOEID).

**Note**: WOEID is a legacy identifier created by Yahoo and has been deprecated. X API uses the numeric value to identify town and country trend locations. Reference our legacy [blog post](https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends.html), or [archived data](https://archive.org/details/geoplanet_data_7.10.0.zip0.)

The `tweet_count` for the last 24 hours is also returned for many trends if this is available.

This endpoint supports app-auth authentication and has a rate limit of 75 requests per 15-minute window.