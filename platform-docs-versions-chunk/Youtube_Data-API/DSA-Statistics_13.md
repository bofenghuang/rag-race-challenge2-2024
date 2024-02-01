platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### I18nRegions

An `**i18nRegion**` resource identifies a geographic area that a YouTube user can select as the preferred content region. The content region can also be referred to as a content locale. For the YouTube website, a content region could be automatically selected based on heuristics like the YouTube domain or the user's IP location. A user could also manually select the desired content region from the YouTube site footer.  
  
Each `i18nRegion` resource identifies a region code and a name. The region code can be used as the value of the `regionCode` parameter when calling API methods like `search.list`, `videos.list`, `activities.list`, and `videoCategories.list`.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/i18nRegions#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/i18nRegions#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[list](https://developers.google.com/youtube/v3/docs/i18nRegions/list)` | `GET /i18nRegions` | Returns a list of content regions that the YouTube website supports. |