platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/search-quality


### Representativeness

In cases where incomplete results are returned (recall < 100%), results may be useful provided they are not overly biased (that is, they are consistent with a random uniform sample of the complete results). We measured representativeness using a series of statistical tests for bias at the individual query level.

#### Query-level bias

For each test query we compared whether a summary statistic (mean, for example) calculated using the results from the Meta Content Library API reasonably approximated results obtained from the validation dataset (which has high recall). Across several data dimensions including engagement, exposure, and creator demographics, we performed a series of t-tests comparing means derived from the Meta Content Library API to means derived from the validation dataset. We then calculated the percent of queries which lacked statistically significant evidence of bias (p > 0.05). Finally, we calculated the mean of metrics across all dimensions.

We performed two versions of this test using methods which differed in their level of sensitivity to small differences between Meta Content Library API results and validation data. In the first version, we used a Welch’s T-test, which is appropriate for detecting major distributional differences between datasets that might affect inference about population-level traits. It is less sensitive to small differences between datasets and we expect most appropriate for research use cases involving trends and summaries.

The following table shows average daily percent of test queries generating non-biased results using a Welch’s T-test across endpoints from November 8th, 2023 to November 15th, 2023.

| Endpoint | Representativeness - Welch t-test |
| --- | --- |
| Facebook Page | 96% |
| Facebook group | 86% |
| Facebook event | 78% |
| Facebook post | 86% |
| Instagram account | 97% |
| Instagram post | 96% |

In the second version of the query-level bias test we compared Meta Content Library API and validation datasets using a pairwise t-test (incorporating covariance between samples). This test is more powered to detect differences between datasets and appropriate for assessing whether small subsets of entities may be missing or over-represented. For instance, this metric could highlight significant bias even with 98% recall and a negligible difference in means, due to any imbalance in the remaining data. Given known issues with the validation dataset failing to exclude some ineligible entities based on visibility criteria, we expect these measures to be more conservative and likely underestimates of representativeness.

The following table shows percent of test queries generating non-biased results using a paired t-test across endpoints from November 8th, 2023 to November 15th, 2023.

| Endpoint | Representativeness - paired t-test |
| --- | --- |
| Facebook Page | 80% |
| Facebook group | 54% |
| Facebook event | 41% |
| Facebook post | 53% |
| Instagram account | 74% |
| Instagram post | 64% |