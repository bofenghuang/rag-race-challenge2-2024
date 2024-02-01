platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Table Schema Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Table Schema Documentation.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/table-schema


## Location data

Throughout the Ad Targeting dataset, we provide the location targeting chosen by an advertiser for the ad. Advertisers can input location targeting in a number of ways, for example by selecting zip codes, countries, Designated Market Areas (DMAs), pin drops (longitude and latitude), addresses, and places within a specified radius. To prevent inadvertently sharing granular location of people on Facebook, we've provided the location options chosen by advertisers when these levels have been set to **zip code level or greater**. For smaller geographic designations, we note the type of selection (such as an address, place, or location pin drop), the city it falls in, and the radius specified by the advertiser.

The following examples help illustrate the transformations. The left column shows the targeting selection by the advertiser; the right column shows the transformation found in the data set. You will see that addresses, pin drops, and places are redacted and replaced by the text "<address>", "<location>", and "<place>", respectively.

| Advertiser selection | Transformed dataset value |
| --- | --- |
| Seattle + 5 miles | `Seattle (+5 miles)` (no change) |
| 38 North Almaden blvd, San Jose +5 miles | `<address>, San Jose (+5 miles)` |
| 95110, San Jose | `95110, San Jose` (no change) |
| 95110, San Jose +5 miles | `95110, San Jose (+5 miles)` (no change) |
| 37.335080; -121.895480 + 5 miles | `<location>, San Jose (+5 miles)` |
| Acme park, San Jose (+1 mile) | `<place>, San Jose (+1 mile)` |

Whenever we cannot report a specific location, we replace it with `"Unknown Country"`, `<unknown location>`, or `<unknown place>` as in this example: `{"Unknown Country":{"":{"":["<unknown place> (+5 km)"]}}}`. This can happen for a number of reasons. A country, for example, could be unknown because the location is too close to a border to classify accurately, or because borders have changed. A place (such as a church or a school), could become unknown because the Facebook page from which the place's location was extracted was deleted.