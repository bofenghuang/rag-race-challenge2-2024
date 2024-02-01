platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/changelog


## December 2, 2020

In compliance with the European Union's [ePrivacy Directive](https://l.facebook.com/l.php?u=https%3A%2F%2Feur-lex.europa.eu%2Flegal-content%2FEN%2FTXT%2F%3Furi%3DCELEX%253A02002L0058-20091219&h=AT1mlokNMGdddzAmj9sv9CHu239X9UK2sG8IiznWBh4PaO9_FvLYxMueicaTxpkOap3RqL7ADupqwDH5sNSEUC0hggtryXUFh8sRaTzayAf7v1XHN93yeCjsh3v7m6krrRG8zJxDpcKa9EuLtJTX-A), messaging-related Story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) interactions performed by users in the European Economic Area (EEA) after December 1, 2020, will no longer be included in some metric calculations:

* For Stories created by users in the EEA, the [`replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights#metrics) metric will now return a value of `0`.
* For Stories created by users outside the EEA, the [`replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights#metrics) metric will return the number of replies, but replies made my users in the EEA will not be included in its calculation.

This change applies to all versions.

[](#)