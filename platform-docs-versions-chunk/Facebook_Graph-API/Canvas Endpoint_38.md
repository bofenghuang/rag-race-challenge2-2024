platform: Facebook
topic: Graph-API
subtopic: Canvas Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Canvas Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/canvas-video/

# Canvas Video

## Reading

A video inside canvas

### Example

PHP Business SDKcURL

    use FacebookAds\Api;
    use FacebookAds\Http\RequestInterface;
    
    $params = array(
      'fields' => array(
        'id',
        'name',
        'video',
      ),
    );
    
    $data = Api::instance()->call(
      '/' . <CANVAS_VIDEO_ID>,
      RequestInterface::METHOD_GET,
      $params)->getContent();

    curl -G \
      --data-urlencode 'fields=[ 
        "id", 
        "name", 
        "video" 
      ]' \
      -d 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v2.11/<CANVAS_VIDEO_ID>

### Parameters

This endpoint doesn't have any parameters.