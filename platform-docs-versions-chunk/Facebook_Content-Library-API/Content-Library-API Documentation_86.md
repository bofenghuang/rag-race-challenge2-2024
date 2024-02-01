platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/adv-search


## Multiple operators

When multiple operators are included in a single query string, the operators are processed (parsed) in a specific order: NOT first, followed by AND, followed by OR. This is important to understand because it means the order in which you place the operators in your query might be different from the order in which they are parsed, which might or might not affect the results.

The examples in this section demonstrate the use of multiple operators in a single query.

| Search objective | How to write it | Examples |
| --- | --- | --- |
| Find matches that include both of two search terms (AND clause), as well as matches that include a third term (OR clause). | Use both an AND clause and an OR clause. The AND clause is parsed first. | lemon lime \| grapefruit<br><br>grapefruit \| lemon lime<br><br>  <br><br>Results include matches containing both “lemon” and “lime”, plus those containing “grapefruit”. |
| Find:<br><br>1. Matches that contain one search term, excluding those containing a second term, and<br>    <br>2. Matches that contain a third term<br>    <br><br>**Note**: Some matches might meet both criteria 1 and 2, but to be included in the query results, the only requirement is to match at least one. | Use both a NOT clause and an OR clause. The NOT clause is parsed first. | fuyu \| persimmon - astringent<br><br>persimmon - astringent \| fuyu<br><br>  <br><br>Results include:<br><br>1. Matches containing “persimmon” but not “astringent” (imagine persimmon - astringent grouped as if in parentheses), and<br>    <br>2. Matches containing “fuyu”<br>    <br><br>Some matches might contain “persimmon” but not “astringent” and also contain “fuyu” (matching both 1 and 2 above), but this is not a requirement to be included in the query results.<br><br>  <br><br>**Note**: If you actually want to exclude “astringent” from “fuyu” as well, you could achieve that using grouping, a technique for customizing the order of precedence. See the next section on [Grouping](#grouping-section). |