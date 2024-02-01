platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/adv-search


## Grouping

You can use grouping with parentheses to influence the order in which clauses are parsed. Clauses enclosed in parentheses are parsed first, followed by operators outside of parentheses.

The examples shown here demonstrate how this works.

| Search objective | How to write it | Examples |
| --- | --- | --- |
| Find matches that contain at least one of two search terms, excluding those that also contain a third term. | Use an OR clause enclosed in parentheses to ensure it is parsed first, followed by a NOT clause. Without the parentheses, the NOT clause would be parsed first. | (fuyu \| persimmon) - astringent<br><br>  <br><br>Results include matches containing either “fuyu” or “persimmon” (or both), but exclude those that also contain “astringent”. |
| Find matches that contain both of two search terms or at least one of two other search terms. Exclude from that list all results that also contain a fifth search term. | Use an AND clause in parentheses, and an OR clause in parentheses. Separate the two parenthetical clauses by an OR operator. Group those two groupings together. Finally, add the NOT clause.<br><br>  <br><br>The extra grouping ensures that "outlaw" is not excluded only from the (newman \| redford) results, but also from the (action movie) results. | ((action movie) \| (newman \| redford)) - outlaw<br><br>  <br><br>Results:<br><br>* Include matches containing both “action” and “movie”<br>* Include matches containing either “newman” or “redford” (can contain both)<br>* Exclude matches that also contain “outlaw” |