platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-ig-posts

# Guide to Instagram posts data

You can perform searches for Instagram posts from public Instagram creator, business, and a subset of personal accounts by calling the Meta Content Library API client's `search_ig_posts()` method.

Public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT1kMMNbwTabLwbZHs52apB3Cz3CknBf53XMxF49QYYHRdbAB-9lk8gaIw5qI3S2BuvWq4zt_q4_4zgau_jsofnJT4schF1BpRXSOSn58DKd66sKL6rsyx-Hklz5hk9UAneEJnm8ikmnNr_J) and have either a verified badge or 50,000 or more followers. A [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT2gWNSoCC5XSFudCGbDRbWLeguZVjLhpBRF7WGmo3V1Q51-qtD7GW9Y8ipAGQLjk_Ak6e_oHtI0ufpRBlcEJfHnWEEwfXcgO9eZTexJXMkLvXB5ZMucutiaquWsPnvbBSXI7HSizswXPuUx) in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription.

This document describes the `search_ig_posts()` method and its syntax and parameters, and shows how to perform basic queries using the method.

All of the examples in this document assume you have already created a Jupyter notebook and have created a client object. See [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-post) for detailed information about the fields that are available on an Instagram post node.