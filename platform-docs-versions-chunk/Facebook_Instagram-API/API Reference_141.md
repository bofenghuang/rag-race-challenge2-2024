platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights

### Sample Demographic Metric Request

curl -i -X GET \\
  "https://graph.facebook.com/`v19.0`/17841405822304914/insights?metric=engaged\_audience\_demographics&period=lifetime&timeframe=last\_90\_days&breakdowns=country&metric\_type=total\_value&access\_token=EAAOc..."