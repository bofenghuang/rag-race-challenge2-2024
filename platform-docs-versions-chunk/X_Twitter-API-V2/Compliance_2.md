platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/introduction


## Introduction

Twitter is committed to our community of developers who build with the Twitter API. As part of this commitment, we aim to make our API open and fair to developers, safe for people on Twitter, and beneficial for the Twitter platform as a whole. It is crucial that any developer who stores Twitter content offline, ensures the data reflects user intent and the current state of content on Twitter. For example,when someone on Twitter deletes a Tweet or their account, protects their Tweets, or scrubs the geo information from their Tweets, it is critical for both Twitter and our developers to honor that person’s expectations and intent. The batch compliance endpoints provide developers an easy tool to help maintain Twitter data in compliance with the [Twitter Developer Agreement and Policy](https://developer.twitter.com/en/developer-terms/policy). 

These batch compliance endpoints allow you to upload large datasets of Tweet or user IDs to retrieve their compliance status in order to determine what data requires action in order to bring your datasets into compliance. Please note, use of the batch compliance endpoints is restricted to aforementioned use cases, and any other purpose is prohibited and may result in enforcement action.

Typically, there are 4 steps involved in working with this endpoint:

1. **Create a compliance job**  
    You can specify the job type (with the value tweets or users to indicate whether the dataset you want to upload has Tweet IDs or user IDs. You can have one concurrent job per job type at any time.
2. **Upload your dataset to the upload\_url**  
    Next, you upload your dataset as a plain text file to the provided upload\_url, with each line of the file containing a single Tweet ID or user ID. The upload\_url expires after 15 minutes.
3. **(Optional) Check the job status**  
    You can check the status of your compliance job to see whether it is created, in\_progress, failed or complete.
4. **Download the results**  
    When your job is complete, you can download the results using the download\_url. The download\_url expires after one week (from when the job was created).  
      
    This result will contain a set of JSON objects (one object per line). Each object will contain a Tweet ID, the Tweet’s creation date (useful to locate Tweets organized by date), required action, the reason for the compliance action, and the date the user was suspended.

You will receive the following compliance event types in your results:

* deleted - indicates that the Tweet or User account was deleted
* deactivated - indicates that the Tweet or User account has been deactivated
* scrub\_geo - indicates that the geo information associated with the Tweet or User was removed
* protected - indicates the account that made the Tweet became private
* suspended - indicates the account that made the Tweet was suspended

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/quick-start)

[Jump to example requests](https://github.com/twitterdev/Twitter-API-v2-sample-code/tree/main/Batch-Compliance)

[Python client](https://github.com/twitterdev/compliant-client)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/compliance/jobs)