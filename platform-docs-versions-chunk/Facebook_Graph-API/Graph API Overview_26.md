platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/results


### Time-based Pagination

Time pagination is used to navigate through results data using Unix timestamps which point to specific times in a list of data.

When using an endpoint that uses time-based pagination, you see the following JSON response:

{
  "data": \[
     ... Endpoint data is here
  \],
  "paging": {
    "previous": "https://graph.facebook.com/{your-user-id}/feed?limit=25&since=1364849754",
    "next": "https://graph.facebook.com/{your-user-id}/feed?limit=25&until=1364587774"
  }
}

A time-paginated edge supports the following parameters:

* `until` : A Unix timestamp or [`strtotime`](http://l.facebook.com/l.php?u=http%3A%2F%2Fphp.net%2Fmanual%2Fen%2Ffunction.strtotime.php&h=AT1oRf6klz5KBdm8V-1Lv9vEjqRjGxdfpfYNttCcAhUD-U0qZewjRXVsUD5aHSj5Of6-X_HtrkXbrgqmrxD8tq69nB01NpnxZ3LQd1YIKj4V789jBmfcV1Q8YX71rtjHn-xkhtBsHGPfqMj5) data value that points to the end of the range of time-based data.
* `since` : A Unix timestamp or [`strtotime`](http://l.facebook.com/l.php?u=http%3A%2F%2Fphp.net%2Fmanual%2Fen%2Ffunction.strtotime.php&h=AT29_8c0aogneGoFngSwYR3cxu8QSlOlMl9I-BaQpU5qLioNrSvBjL1eY5uL9cHWZUrlotP0CgfgyNCMHxayX2zipFf1QFuZ6I12dRfebKF-AxrqIszspl3AdS9sY0zqD6YtlJx3Z5mmhmC3) data value that points to the start of the range of time-based data.
* `limit` : This is the maximum number of objects that _may_ be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
* `next` : The Graph API endpoint that will return the next page of data.
* `previous` : The Graph API endpoint that will return the previous page of data.

For consistent results, specify both `since` and `until` parameters. Also, it is recommended that the time difference is a maximum of 6 months.