platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks


### Additional security guidelines

The following are additional security guidelines to consider for your web application. Not having these guidelines implemented will not prevent your webhook from functioning, but are highly reccomended by the Twitter Information Security team. If you are unfamilair with the below recommendations consult with your server administrator.

#### Twitter aggregate network blocks  

For added security you may wish to add the following aggregate network blocks to an allowlist:

* 199.59.148.0/22
* 199.16.156.0/22
* 192.133.77.0/26
* 64.63.15.0/24  
    
* 64.63.31.0/24
* 64.63.47.0/24
* 202.160.128.0/24
* 202.160.129.0/24
* 202.160.130.0/24

#### Recommended server configurations

* "A" rating on [ssllabs.com](http://ssllabs.com/) test
* **Enable TLS 1.2**
* Enable Forward Secrecy
* Turn off SSLv2
* Turn off SSLv3 (because of POODLE)
* Turn off TLS 1.0
* Turn off TLS 1.1
* Turn off TLS Compression
* Turn off Session Tickets unless you rotate session ticket keys.
* Set the “ssl\_prefer\_server\_ciphers” or “SSLHonorCipherOrder” option in the SSL Configuration “on”.
* Ensure the list of ciphers is a modern list such as:  
    `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES128-SHA256:AES128-SHA:AES256-GCM-SHA384:AES256-SHA256:AES256-SHA:ECDHE-RSA-DES-CBC3-SHA:DES-CBC3-SHA`