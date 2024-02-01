platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/insights

# Insights

You can use the Instagram Graph API to get social interaction metrics for [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user) and their [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects. Amounts for each metric are calculated upon API request.

Due to privacy rules, messaging-related Story IG Media interactions performed by users in some regions will no longer be included in some metric calculations. These regions include: Europe starting December 1, 2020 and Japan starting April 14, 2021.

* For Stories created by users in affected regions, the [`replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights#metrics) metric will now return a value of `0`.
* For Stories created by users outside affected regions, the [`replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights#metrics) metric will return the number of replies, but replies made by users in affected regions will not be included in the calculation.