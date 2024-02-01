platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/search-quality


### Methods

#### Initial test queries

We generated test search results for each endpoint (Facebook Pages, groups, events, and posts, and Instagram business and creator accounts, and posts) using a sample of 130 terms chosen to span a breadth of set size (for example, obscure words such as _stopthesteal_ and common words such as _spray_), polarization (for example, neutral words such as _sugar_ and socially charged words such as _transphobic_), as well as most queried keywords by researchers in Meta platforms. These initial test queries consisted of single terms all in English without non-Latin characters or any symbols (for example ‘, #, $ or @). Additional query parameters for each endpoint are listed in [Test search scope for endpoints](#scope). Test queries resulting in > 100,000 results were excluded from further analysis.

#### Validation data

Lists of expected entities for test queries were generated from regex-based full-text searches on a SQL-like database backend. Tables in this database are built from periodic snapshots of logged platform content and thus are known to differ slightly from what is available in Meta Content Library and API at search time due to time lags and incomplete visibility filters. This dataset thus constitutes a secondary validation channel rather than source of truth and regressions in quality metrics may be a composite of both true indexing errors and/or measurement noise. See [Caveats and known limitations](#caveats).