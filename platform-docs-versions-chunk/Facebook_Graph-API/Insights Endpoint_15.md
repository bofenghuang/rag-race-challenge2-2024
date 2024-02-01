platform: Facebook
topic: Graph-API
subtopic: Insights Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Insights Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/insights


### Page User Demographics

| Metric Name | Description | Values for \`period\` |
| --- | --- | --- |
| `page_fans` | The total number of people who have liked your Page. | day |
| `page_fans_locale` | Aggregated language data about the people who like your Page based on the default language setting selected when accessing Facebook. | day |
| `page_fans_city` | Aggregated Facebook location data, sorted by city, about the people who like your Page. | day |
| `page_fans_country` | The number of people, aggregated per country, that like your Page. Only the 45 countries with the most people that like your Page are included. | day |
| `page_fans_gender_age` | The number of likes of your Facebook Page. | day |
| `page_fan_adds` | The number of new people who have liked your Page. | day |
| `page_fan_adds_unique` | The number of new people who have liked your Page. | day, week, days\_28 |
| `page_fans_by_like_source` | This is a breakdown of the number of Page likes from the most common places where people can like your Page. (See [possible types](#page-like-sources)) | day |
| `page_fans_by_like_source_unique` | The number of people who liked your Page, broken down by the most common places where people can like your Page. (See [possible types](#page-like-sources)) | day |
| `page_fan_removes` | Unlikes of your Page. | day |
| `page_fan_removes_unique*` | Unlikes of your Page. | day, week, days\_28 |
| `page_fans_by_unlike_source_unique` | The number of people who unliked your Page, broken down by the most common ways people can unlike your Page. | day |

#### Page Like Sources

Source types for `page_fans_by_like_source` and `page_fans_by_like_source_unique` metrics.

| Name | Description |
| --- | --- |
| `Ads` | Page likes that came from people who saw your Page or post in an ad. |
| `News Feed` | Page likes that came from people who saw content posted by your Page or about your Page in News Feed. |
| `Page Suggestions` | Page likes that came from people saw your Page in a list of suggested Pages. |
| `Restored Likes from Reactivated Accounts` | Page likes that came from people who reactivated their Facebook profile. |
| `Search` | Page likes that came from people who saw you Page or post in search. |
| `Your Page` | Page likes that came from people who visited your Page. |

#### Page Unlike Sources

Source types for `page_fans_by_unlike_source_unique` and `page_fans_by_unlike_source` metrics.

| Source Type Name | Description |
| --- | --- |
| `Deactivated or Memorialized Account Removals` | The Page likes that were removed due to deactivated or memorialized accounts. |
| `Other` | The Page likes that were removed due to reasons other than deactivated or memorialized accounts, suspicious accounts, unlikes from Page, Posts, or NewsFeed, or unlikes from search. |
| `Suspicious Account Removals` | The Page likes that were removed due to suspicious account activity. |
| `Unlikes from Page, Posts, or News Feed` | The Page likes that were removed from people who saw content posted by your Page or about your Page in News Feed. |
| `Unlikes from Search` | The Page likes that were removed from people who saw your Page or post in search. |