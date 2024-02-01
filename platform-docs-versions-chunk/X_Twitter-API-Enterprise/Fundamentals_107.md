platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls

Expanded and Enhanced URLs

## Expanded and Enhanced URLs

The Expanded and Enhanced URL enrichment automatically expands shortened URLs that are included in the body of a Tweet, and includes the resulting URL as metadata within the payload. In addition, this enrichment also provides HTML page metadata from the `title` and `description` of the destination page.

**Important Details:**

* To resolve a shortened link, our system sends HTTP HEAD requests to the URL provided and follows any redirects until it arrives at the final URL. This final URL (NOT the content of the page itself) is then included in the response payload.  
    
* The URL enrichment does add between 5-10 seconds latency to realtime streams
* For requests made to the Full Archive Search API, expanded URL enrichment data is only available for Tweets 13 months old or newer.  
    
* The URL enrichment is not available for Tweet links (including quote Tweets), Moments links, and profile links that are included within a Tweet.