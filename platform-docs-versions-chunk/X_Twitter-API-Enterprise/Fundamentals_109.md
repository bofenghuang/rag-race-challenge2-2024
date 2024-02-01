platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls

### Filtering operators

The following operators will filter and provide a tokenized match on the related fields of URL metadata:

**url:**

* Example: “url:tennis”
* Tokenized match on any Expanded URL that includes the word tennis
* Could also be used as a filter to include or exclude links from a specific website using something like “url:npr.org”

**url\_title:**

* Example: “url\_title:tennis”
* Tokenized match on any Expanded URL HTML title that includes the word tennis
* Matches on the HTML title data included in the payload, which is limited to 300 characters.

**url\_description:**

* Example: “url\_description:tennis”
* Tokenized match on any Expanded URL HTML description that includes the word tennis
* Matches on the HTML description included in the payload, which is limited to 1000 characters.