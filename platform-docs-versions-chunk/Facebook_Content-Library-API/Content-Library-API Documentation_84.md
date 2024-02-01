platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/adv-search


## General rules

The following general rules apply to forming queries:

* The following operators are supported: AND, OR, NOT.
* Use an ampersand character (&) or a blank space to indicate AND.
* Use a pipe character ( | ) to indicate OR.
* Use a hyphen character (-) to indicate NOT. The en-dash and em-dash characters are _not_ interpreted as substitutes for hyphen and are treated instead as keywords.
* For queries with multiple operators, NOT clauses are processed first, followed by AND, followed by OR. Imagine the terms grouped as if with parentheses.
* For clauses of equal precedence, there is a default left-to-right processing order.
* Grouping using parentheses is supported. Grouping can be used to modify the default processing order.
* You can use single-word keywords only (not phrases).
* Wild cards are not supported.
* Extra spaces around operators are ignored, so you can have them or not.

Because they have special meaning in the context of query syntax, the following characters cannot be used as keywords or embedded in keywords:

* & ampersand
* | pipe
* ‐ hyphen
* space
* ( open parenthesis
* ) close parenthesis