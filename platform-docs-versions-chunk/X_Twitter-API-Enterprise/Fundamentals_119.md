platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo


### Profile Geo Data

| Enriched native field name | Example value | Description |
| --- | --- | --- |
| user.derived.locations.country | United States | The country location for where the user that created the Tweet is from. |
| user.derived.locations.country\_code | US  | A two-letter ISO-3166 country code that corresponds to the country location for where the user that created the Tweet is from. |
| user.derived.locations.locality | Birmingham | The locality location (generally city) for where the user that created the Tweet is from. |
| user.derived.locations.region | Alabama | The region location (generally state/province) for where the user that created the Tweet is from. |
| user.derived.locations.sub\_region | Jefferson County | The sub-region location (generally county) for where the user that created the Tweet is from. |
| user.derived.locations.full\_name | Birmingham, Alabama, United States | The full name (excluding sub-region) for where the user that created the Tweet is from. |
| User.derived.locations.geo | See Below | An array that includes a lat/long value for a coordinate that corresponds to the lowers granularity location for where the user that created the Tweet is from. |

The Historical PowerTrack, Search, and PowerTrack APIs supports filtering based on Profile Geo data. See the appropriate product documentation for more details on what operators are available for filtering on Profile Geo data.