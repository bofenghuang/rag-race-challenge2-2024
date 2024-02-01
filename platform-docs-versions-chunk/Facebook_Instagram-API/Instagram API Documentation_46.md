platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/content-publishing

## Collaborator Tags

You can add public Instagram users in an image, carousel and reel as a collaborators and they will receive an invite to be a collaborator for that particular media. To tag users in an image, follow the Single Media Posts steps above, but when creating the media container, include the collaborators parameter and an array of strings indicating the Instagram usernames of users whom you want to invite as a collaborator on the media.

#### Sample Requeset

POST graph.facebook.com/17841400008460056/media
?image\_url\=https://www.example.com/images/bronzed-fonzes.jpg
&caption\=#BronzedFonzes!
&collaborators\= \[‘username1’,’username2’\]

#### Notes

* The collaborators value must be an array of strings.
* You can only tag users with public Instagram accounts.
* No more than 3 collaborators can be added to a media.
* Collaborators cannot be added to Story media.

[](#)