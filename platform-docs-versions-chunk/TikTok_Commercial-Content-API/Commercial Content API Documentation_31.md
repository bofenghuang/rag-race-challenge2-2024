platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-details/


### RejectionInfo

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| reasons | list<string> | The reason that an ad has been rejected, when applicable. | \["The product/service promoted on the ad/landing page belongs to a prohibited industry of the targeted location(s) in your ad when we take our own business evaluation, user experience and the value of advertisement impact, etc. into consideration."\] |
| affected\_countries | list<string> | The affected region(s), if any, where the listed rejection reasons may apply to the ad. If an ad is rejected but no affected regions are specified, it may be rejected in all applicable regions. | \["Austria", "Belgium"\] |
| reporting\_source | string | The reporting or detection source that led to the ad's rejection(s), when applicable. | Users and third parties can report policy violations to us. We have detected this policy violation based on a report that the content violated our Advertising Policies. |
| automated\_notice | string | The notice that describes when TikTok's moderation decision relied on automated measures. This field returns a null value if the decision was based on a manual review. | We have used automated measures in making this decision. |