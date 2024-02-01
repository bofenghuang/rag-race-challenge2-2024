platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### I18nLanguages

An `**i18nLanguage**` resource identifies an application language that the YouTube website supports. The application language can also be referred to as a UI language. For the YouTube website, an application language could be automatically selected based on Google Account settings, browser language, or IP location. A user could also manually select the desired UI language from the YouTube site footer.  
  
Each `i18nLanguage` resource identifies a language code and a name. The language code can be used as the value of the `hl` parameter when calling API methods like `videoCategories.list` and `guideCategories.list`.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/i18nLanguages#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/i18nLanguages#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[list](https://developers.google.com/youtube/v3/docs/i18nLanguages/list)` | `GET /i18nLanguages` | Returns a list of application languages that the YouTube website supports. |