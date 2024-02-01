platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/field-expansion


## Field Aliases

Many nodes and edges allow you to provide aliases for fields by using the `as` parameter. This will return data using fields that you already have in your application logic.

For example, you can retrieve an image in two sizes and alias the returned object fields as `picture_small` and `picture_larger`:

me?fields=id,name,picture.width(100).height(100).as(picture\_small),picture.width(720).height(720).as(picture\_large)

On success, Graph API returns this result:

{
  "id": "993363923726",
  "name": "Benjamin Golub",
  "picture\_small": {
    "data": {
      "height": 100,
      "is\_silhouette": false,
      "url": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xft1/v/t1.0-1/p100x100/11700890\_10100330450676146\_2622493406845121288\_n.jpg?oh=82b9abe469c78486645783c9e70e8797&amp;oe=561D10AE&amp;\_\_gda\_\_=1444247939\_661c0f48363f1d1a7d42b6f836687a04",
      "width": 100
    }
  },
  "picture\_large": {
    "data": {
      "height": 720,
      "is\_silhouette": false,
      "url": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xft1/v/t1.0-1/11700890\_10100330450676146\_2622493406845121288\_n.jpg?oh=dd86551faa2de0cd6b359feb5665b0a5&amp;oe=561E0B46&amp;\_\_gda\_\_=1443979219\_f1abbbdfb0fb7dac361d7ae02b460638",
      "width": 720
    }
  }
}

Please note that not all nodes and edges support field aliasing. Endpoints that do not support aliasing will return an error. For example, the `User` node does not support aliasing, so if you tried to alias the `name` field as `my_name` you would receive an error like this:

{
  "error": {
    "message": "(#100) Unknown fields: my\_name.",
    "type": "OAuthException",
    "code": 100
  }
}