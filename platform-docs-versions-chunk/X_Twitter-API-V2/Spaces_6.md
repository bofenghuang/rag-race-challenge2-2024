platform: X
topic: Twitter-API-V2
subtopic: Spaces
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Spaces.md
url: https://developer.twitter.com/en/docs/twitter-api/spaces/overview

### Hosts

The primary Hosts can make one or more users co-hosts. In the Spaces data dictionary, these Hosts will appear as host\_ids, which can be expanded into a list of user objects. Host designation can change throughout the duration of a Space, and the metadata returned by these endpoints will reflect the status at the time of the request.

Your app will know the primary host by checking the creator\_id value, and who are the co-hosts by checking the host\_ids values.  
 

### Speaker

Speakers are users who have permission to talk in the Space. Zero or more Speakers can be present at any time, and there may be up to 10 Speakers (including the Hosts) in a Space. In the Space data dictionary, speakers will be returned in the speaker\_ids list, which you can expand into a list of user objects.