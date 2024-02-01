platform: Facebook
topic: Graph-API
subtopic: Canvas Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Canvas Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/canvas-carousel/

# Canvas Carousel

## Reading

A carousel inside a canvas

### Example

PHP Business SDKcURL

    use FacebookAds\Api;
    use FacebookAds\Http\RequestInterface;
    
    $params = array(
      'fields' => array(
        'child_elements',
        'id',
        'name',
      ),
    );
    
    $data = Api::instance()->call(
      '/' . <CANVAS_CAROUSEL_ID>,
      RequestInterface::METHOD_GET,
      $params)->getContent();

    curl -G \
      --data-urlencode 'fields=[ 
        "child_elements", 
        "id", 
        "name" 
      ]' \
      -d 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v2.11/<CANVAS_CAROUSEL_ID>

### Parameters

This endpoint doesn't have any parameters.