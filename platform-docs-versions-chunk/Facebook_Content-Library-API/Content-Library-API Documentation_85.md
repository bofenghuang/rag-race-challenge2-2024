platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/adv-search


## Using operators

The examples included here demonstrate the basic use of the AND, OR, and NOT operators.

| Search objective | How to write it | Examples |
| --- | --- | --- |
| Find matches that include all of the provided search terms. | Use the AND operator expressed as an ampersand character (&) or a blank space. | cat&dog&allergy<br><br>cat dog allergy<br><br>cat&dog allergy<br><br>cat dog&allergy<br><br>  <br><br>Each match contains all three terms: “cat”, “dog”, and “allergy”. |
| Find matches that include at least one of the provided search terms. | Use the OR operator expressed as a pipe character (\|). | cat \| dog<br><br>cat\|dog<br><br>cat \|dog<br><br>cat\| dog<br><br>  <br><br>Each match contains “cat” or “dog”, and could contain both. |
| Find matches that include the provided search term, excluding a second term. | Use the NOT operator expressed as a hyphen character (-). | dog -puppy<br><br>dog-puppy<br><br>dog- puppy<br><br>dog - puppy<br><br>  <br><br>Each match contains “dog” but not “puppy”. Results containing both “dog” and “puppy” are excluded. |