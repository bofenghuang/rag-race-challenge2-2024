platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo


### Limitations

* The Profile Geo enrichment attempts to determine the best choice for the geographic place described in the profile location string. The result may not be accurate in all cases due to factors such as multiple places with similar names or ambiguous names.
* If a value is not provided in a user’s profile location field (actor.location), we will not attempt to make a classification.
* Precision Level: If a Profile Geo Enrichment can only be determined with confidence at the country or region level, lower-level geographies such as subRegion and locality will be omitted from the payload.
* The Profile Geo enrichment provides lat/long coordinates (a single point) that corresponds to the Precision Level of the enrichment’s results. These coordinates represent the geographic center of the enrichment location results. For example, if the Precision Level is at the Country level, then those coordinates are set to the geographic center of that Country.
* The PowerTrack operators provided for address properties (locality/region/country/country code) are intentionally granular to allow for many rule combinations. When attempting to target a specific location that shares a name with another location, consider combining address rules. For instance, the following would avoid matches for “San Francisco, Philippines”: profile\_locality:”San Francisco” profile\_region:California When building rules that target individual Profile Geo fields, keep in mind that each increased level of granularity will limit the results you see. In some cases when attempting to look at data from a city, you may wish to only rely on a region rule where the region offers significant overlap with the city, e.g. the city of Zurich, Switzerland can be effectively targeted along with surrounding areas with profile\_region:”Zurich”.
* Use with Native Geo Tweets: The Profile Geo enrichment provides an alternative type of geography for a Tweet, different from the native geo value in the payload. These two types of geography can be combined together to capture all of the possible tweets related to a given area (based on available geodata), though they are not conceptually equivalent.