platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/search-quality


## Search overview

Queries in Meta Content Library and API are powered by a version of Facebook’s [search engine infrastructure](https://research.facebook.com/publications/unicorn-a-system-for-searching-the-social-graph/), which relies on a combination of indexing and ranking to return relevant entities. The retrieval function combines matched and ranked IDs from a query using the same distributed [memory caching layer](https://l.facebook.com/l.php?u=https%3A%2F%2Fengineering.fb.com%2F2013%2F06%2F25%2Fcore-data%2Ftao-the-power-of-the-graph%2F&h=AT1-Q7Wgi5KB4QxoLpmG2GlumDaDJaFx-Gy4AGLKCweWro_nv71laUM-gb4OHWV8kv9t0ThHlPx8T-qY162Or5GqbNhyBSRrjmGQu5qDDKIFEGD_cc-uyOs2xAeRrRTyZi5Yy2wUs4CqPANp) which serves live platform content. This ensures that results represent the most current state of content on the platform and meet privacy-preserving visibility criteria (see [Frequently asked questions](https://developers.facebook.com/docs/content-library-api/disclosures) for details).

As content is created or modified on Meta platforms, associated entities are registered to a search index built from individual words extracted from text fields as _tokens_. Tokenization generally isolates words separated by spaces or punctuation ( ?@$%^\*()+=~\[{}\];:"<>|. ), with some URL normalization and locale-specific adjustments for non-English languages. Tokenization is exact, in that it does not introduce additional word variants ("cats" will not be tokenized to "cat"). Direct mentions of users or other platform entities (via @) are not tokenized and are scrubbed from returned text fields, and are thus not searchable.

At query time, relevant content is identified by exact matching between tokens and individual search terms. Candidate matches are then subject to additional filtering via Boolean query logic (see [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)) and other selected filters. Matching is performed independently by word in a query, meaning that searching by phrase is not supported (queries “All for one” and “One for all” are equivalent).