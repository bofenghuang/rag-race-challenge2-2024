platform: X
topic: Twitter-API-Enterprise
subtopic: Usage API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Usage API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/usage-api/overview

Overview

## Overview

Enterprise

The Usage API is a free REST API that provides programmatic access and visibility into activity consumption across products for your enterprise account. It is the most important and _best_ tool for helping to monitor and manage usage across the different APIs under your account.

**Important Disclaimer:**

The usage counts returned from the Usage API may not match those on a billing invoice due to trials and other billing adjustments. All numbers are based on deduped activities consumed within a given day (in UTC).

### Features

* Programmatically retrieving usage data that is available in the console.gnip.com UI
* Stream level usage data - provides usage data at the stream level (e.g., dev and prod) in addition to the product level
* Granular and descriptive data - search "requests" are broken out by Full-Archive and 30-Day Search products 
* Historical PowerTrack “days” and “jobs”