platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/content-publishing


## Location Tags

You can use the [Pages Search API ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=6zzb9-5bY8QAX_nY52g&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBRGSoDbMfUe1dC6xxUblU-wz3raGSpfpjPYKA-ck1AaA&oe=65D572A2)](https://developers.facebook.com/docs/pages/searching) , be sure to include the \`location\` field in your query, to search for Pages whose names match a search string. Then, parse the results to identify any Pages that have been created for a physical location. If you include a Page's ID when publishing an image or video, it will be tagged with the location associated with that Page.

#### Limitations

To be eligible for tagging, a Page must have latitude and longitude location data.

Verify that the Page you want to use has latitude and longitude data in the response. Attempting to create a container using a Page that has no location data will fail with coded exception `INSTAGRAM_PLATFORM_API__INVALID_LOCATION_ID`.

Once you have the Page ID, assign it to the `location_id` parameter when publishing [single media](#single-media-posts) or [carousel](#carousel-posts) item containers.

[](#)